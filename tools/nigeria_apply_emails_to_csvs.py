#!/usr/bin/env python3
"""
Apply emails found from website visits to original Nigeria CSV files.
Matches businesses by name across raw_leads.csv, niche CSVs, and enriched CSVs.
"""

import json
import csv
import os
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/home/z/my-project/english-nations-hub/countries/Nigeria")
TOOLS_DIR = Path("/home/z/my-project/english-nations-hub/tools")

EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}')

def load_emails_found():
    """Load the compiled emails found from website visits."""
    filepath = TOOLS_DIR / 'nigeria_emails_found.json'
    with open(filepath) as f:
        data = json.load(f)
    
    # Build a lookup: business_name_lower -> list of emails
    email_lookup = {}
    for r in data['businesses_with_emails']:
        name = r['business_name'].lower().strip()
        if name not in email_lookup:
            email_lookup[name] = []
        email_lookup[name].extend(r['emails_found'])
    
    # Deduplicate
    for name in email_lookup:
        email_lookup[name] = list(set(email_lookup[name]))
    
    return email_lookup

def fuzzy_match(business_name, lookup_names):
    """Try to match a business name to the lookup."""
    name_lower = business_name.lower().strip()
    
    # Exact match
    if name_lower in lookup_names:
        return name_lower
    
    # Remove common suffixes for matching
    name_clean = name_lower
    for suffix in ['@ victoria island', '@ ikeja', '(lekki phase 1)', '(lekki)', 
                    '(victoria island branch)', 'ltd', 'limited', 'nigeria']:
        name_clean = name_clean.replace(suffix, '').strip()
    
    for lookup_name in lookup_names:
        if lookup_name in name_clean or name_clean in lookup_name:
            return lookup_name
        if name_clean.replace(' ', '') in lookup_name.replace(' ', ''):
            return lookup_name
    
    return None

def process_csv_file(filepath, email_lookup, updates_count):
    """Process a single CSV file and add emails where found."""
    filepath = Path(filepath)
    relative = filepath.relative_to(BASE_DIR)
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        lines = content.split('\n')
        if len(lines) < 2:
            return updates_count
        
        reader = csv.reader(lines)
        headers = next(reader)
        rows = list(reader)
        
        # Detect CSV type
        has_email_col = False
        email_col_idx = None
        has_validation_col = False
        validation_col_idx = None
        has_website_col = False
        website_col_idx = None
        
        for idx, h in enumerate(headers):
            h_lower = h.lower().strip()
            if h_lower == 'email address' or h_lower == 'email':
                has_email_col = True
                email_col_idx = idx
            elif 'email validation' in h_lower:
                has_validation_col = True
                validation_col_idx = idx
            elif h_lower == 'website':
                has_website_col = True
                website_col_idx = idx
        
        modified = False
        
        for row_idx, row in enumerate(rows):
            if not row:
                continue
            
            business_name = row[0].strip() if row else ''
            if not business_name:
                continue
            
            # Skip if already has email
            if has_email_col and email_col_idx is not None and email_col_idx < len(row):
                existing_email = row[email_col_idx].strip()
                if existing_email and existing_email not in ('Not Available', 'N/A', ''):
                    continue
            
            # Also check all cells for existing emails
            row_text = ' '.join(row)
            existing_emails = EMAIL_PATTERN.findall(row_text)
            if existing_emails:
                continue
            
            # Try to match
            match_key = fuzzy_match(business_name, email_lookup.keys())
            if match_key:
                emails = email_lookup[match_key]
                if emails:
                    # Determine the website column
                    website_val = ''
                    if has_website_col and website_col_idx is not None and website_col_idx < len(row):
                        website_val = row[website_col_idx].strip()
                    elif len(row) > 6:
                        website_val = row[6].strip()
                    
                    # For enriched CSVs (have email col): update email col
                    if has_email_col and email_col_idx is not None and email_col_idx < len(row):
                        row[email_col_idx] = '; '.join(emails)
                        if has_validation_col and validation_col_idx is not None and validation_col_idx < len(row):
                            row[validation_col_idx] = 'Verified (found on website)'
                        modified = True
                        updates_count += 1
                        print(f"  [{relative}] Updated '{business_name}' with emails: {', '.join(emails[:2])}")
                    
                    # For raw/niche CSVs (no email col): add email to a note or skip
                    # We'll add it to enriched CSVs via the name match
                    # For raw CSVs, we note the enrichment but don't add columns
                    
        if modified:
            # Write back
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)
        
        return updates_count
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")
        return updates_count

def update_enriched_csvs(email_lookup):
    """Update enriched CSVs with found emails."""
    print("\n--- Updating Enriched CSVs ---")
    updates = 0
    
    for enriched_file in BASE_DIR.rglob("enriched_leads.csv"):
        updates = process_csv_file(enriched_file, email_lookup, updates)
    
    return updates

def update_other_web_csvs(email_lookup):
    """Update other web leads CSVs."""
    print("\n--- Updating Other Web Leads CSVs ---")
    updates = 0
    
    for web_file in BASE_DIR.rglob("*_web.csv"):
        updates = process_csv_file(web_file, email_lookup, updates)
    
    return updates

def update_it_companies_csvs(email_lookup):
    """Update IT companies and tech CSVs."""
    print("\n--- Updating Tech/IT CSVs ---")
    updates = 0
    
    for csv_file in BASE_DIR.rglob("it_companies.csv"):
        updates = process_csv_file(csv_file, email_lookup, updates)
    for csv_file in BASE_DIR.rglob("tech_startups_web.csv"):
        updates = process_csv_file(csv_file, email_lookup, updates)
    
    return updates

def create_raw_leads_enrichment(email_lookup):
    """For raw_leads.csv and niche CSVs that don't have email columns,
    create a supplementary enrichment file."""
    print("\n--- Creating Raw Leads Enrichment Notes ---")
    
    enrichments = []
    
    for csv_file in BASE_DIR.rglob("raw_leads.csv"):
        relative = str(csv_file.relative_to(BASE_DIR))
        try:
            with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.reader(f)
                headers = next(reader)
                
                for row_idx, row in enumerate(reader):
                    if not row:
                        continue
                    business_name = row[0].strip() if row else ''
                    if not business_name:
                        continue
                    
                    match_key = fuzzy_match(business_name, email_lookup.keys())
                    if match_key:
                        emails = email_lookup[match_key]
                        enrichments.append({
                            'file': relative,
                            'row': row_idx + 2,
                            'business_name': business_name,
                            'business_niche': row[1] if len(row) > 1 else '',
                            'city_area': row[3] if len(row) > 3 else '',
                            'website': row[6] if len(row) > 6 else '',
                            'emails_found': emails,
                            'enrichment': f'Emails found via website visit: {"; ".join(emails)}'
                        })
                        print(f"  [{relative}] '{business_name}': {', '.join(emails[:2])}")
        except Exception as e:
            print(f"  Error: {csv_file}: {e}")
    
    # Also process niche CSVs
    niche_csvs = [
        'hotels_lodging.csv', 'dental_clinics.csv', 'restaurants.csv',
        'law_firms.csv', 'banks_credit_unions.csv', 'real_estate.csv',
        'real_estate_agencies.csv', 'marketing_agencies.csv',
        'marketing_advertising_agencies.csv', 'it_companies.csv',
        'schools.csv', 'pharmacies.csv', 'gyms_fitness.csv',
        'salons_barbershops.csv', 'event_planning.csv', 'auto_dealers.csv',
        'shopping.csv', 'hospitals_medical_centers.csv',
        'consulting_firms.csv', 'financial_advisors_planners.csv',
        'it_managed_service_providers.csv',
    ]
    
    for niche_name in niche_csvs:
        for csv_file in BASE_DIR.rglob(niche_name):
            if csv_file.name == 'it_companies.csv' and 'Niches' in str(csv_file):
                relative = str(csv_file.relative_to(BASE_DIR))
                try:
                    with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
                        reader = csv.reader(f)
                        headers = next(reader)
                        
                        for row_idx, row in enumerate(reader):
                            if not row:
                                continue
                            business_name = row[0].strip() if row else ''
                            if not business_name:
                                continue
                            
                            match_key = fuzzy_match(business_name, email_lookup.keys())
                            if match_key:
                                emails = email_lookup[match_key]
                                enrichments.append({
                                    'file': relative,
                                    'row': row_idx + 2,
                                    'business_name': business_name,
                                    'business_niche': row[1] if len(row) > 1 else '',
                                    'city_area': row[3] if len(row) > 3 else '',
                                    'website': row[6] if len(row) > 6 else '',
                                    'emails_found': emails,
                                    'enrichment': f'Emails found via website visit: {"; ".join(emails)}'
                                })
                                print(f"  [{relative}] '{business_name}': {', '.join(emails[:2])}")
                except Exception as e:
                    print(f"  Error: {csv_file}: {e}")
    
    return enrichments

def main():
    print("=" * 70)
    print("NIGERIA CSV EMAIL UPDATE")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}")
    
    email_lookup = load_emails_found()
    print(f"Loaded {len(email_lookup)} businesses with emails from website visits")
    
    # Update enriched CSVs
    enriched_updates = update_enriched_csvs(email_lookup)
    
    # Update other web CSVs
    web_updates = update_other_web_csvs(email_lookup)
    
    # Update tech CSVs
    tech_updates = update_it_companies_csvs(email_lookup)
    
    # Create enrichment notes for raw/niche CSVs
    enrichments = create_raw_leads_enrichment(email_lookup)
    
    total_updated = enriched_updates + web_updates + tech_updates
    
    print(f"\n--- Summary ---")
    print(f"  Enriched CSVs updated: {enriched_updates}")
    print(f"  Other Web CSVs updated: {web_updates}")
    print(f"  Tech CSVs updated: {tech_updates}")
    print(f"  Total rows updated with emails: {total_updated}")
    print(f"  Raw/Niche CSV enrichment entries: {len(enrichments)}")
    
    # Save enrichment data
    if enrichments:
        output = {
            'generated': datetime.now().isoformat(),
            'total_enrichments': len(enrichments),
            'enrichments': enrichments
        }
        with open(TOOLS_DIR / 'nigeria_raw_leads_enrichment.json', 'w') as f:
            json.dump(output, f, indent=2)
        print(f"  Saved: nigeria_raw_leads_enrichment.json")
    
    print(f"\n{'=' * 70}")
    print(f"Completed: {datetime.now().isoformat()}")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()
