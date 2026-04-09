#!/usr/bin/env python3
"""
Nigeria DNS Email Validation Script
Scans all Nigeria CSV files, validates emails via DNS MX records,
identifies businesses with websites but no emails.
"""

import csv
import json
import re
import os
from pathlib import Path
from datetime import datetime

try:
    import dns.resolver
except ImportError:
    print("Installing dnspython...")
    os.system("pip install dnspython")
    import dns.resolver

BASE_DIR = Path("/home/z/my-project/english-nations-hub/countries/Nigeria")
TOOLS_DIR = Path("/home/z/my-project/english-nations-hub/tools")

# Email regex pattern
EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)

# Domains to skip (social media, government)
SKIP_DOMAINS = [
    'facebook.com', 'instagram.com', 'twitter.com', 'x.com',
    'linkedin.com', 'tiktok.com', 'youtube.com', 'wa.me',
    'gov.ng', 'facebook.com', 'google.com/maps', 'maps.google.com',
    'tripadvisor.com', 'yelp.com'
]

def extract_emails(text):
    """Extract all email addresses from a text string."""
    if not text or text.strip() in ('', 'Not Available', 'N/A', 'not available'):
        return []
    return EMAIL_PATTERN.findall(str(text))

def get_domain_from_email(email):
    """Extract domain from email address."""
    match = re.search(r'@([a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})', email)
    return match.group(1).lower() if match else None

def validate_email_dns(email):
    """
    Validate email by checking DNS MX and A records.
    Returns: (status, details)
    """
    email = email.strip().lower()
    domain = get_domain_from_email(email)
    if not domain:
        return ('invalid_format', 'Could not extract domain')
    
    # Check MX records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            mx_hosts = [str(r.exchange).rstrip('.') for r in mx_records]
            return ('valid_mx', f'MX records found: {mx_hosts}')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except dns.resolver.NoNameservers:
        return ('no_mail_server', f'No nameservers available for {domain}')
    except Exception as e:
        pass
    
    # Check A record fallback
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        if a_records:
            ips = [str(r) for r in a_records]
            return ('valid_a_record', f'No MX but A record found: {ips}')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return ('no_mail_server', f'No MX or A records for {domain}')
    except Exception as e:
        return ('no_mail_server', f'DNS lookup error: {str(e)}')
    
    return ('no_mail_server', f'No DNS records found for {domain}')

def is_valid_website(url):
    """Check if URL is a valid business website (not social media)."""
    if not url or url.strip() in ('', 'Not Available', 'N/A', 'not available'):
        return False
    url_lower = url.lower()
    for skip in SKIP_DOMAINS:
        if skip in url_lower:
            return False
    if url_lower.startswith('http://') or url_lower.startswith('https://'):
        return True
    return False

def find_email_column(headers):
    """Find the email column name in CSV headers."""
    headers_lower = [h.lower().strip() for h in headers]
    for idx, h in enumerate(headers_lower):
        if 'email' in h and 'validation' not in h and 'source' not in h:
            return idx
    return None

def find_website_column(headers):
    """Find the website column name in CSV headers."""
    headers_lower = [h.lower().strip() for h in headers]
    for idx, h in enumerate(headers_lower):
        if h == 'website' or h == 'website/portfolio' or h == 'website (verified)':
            return idx
    return None

def find_validation_status_column(headers):
    """Find the email validation status column."""
    headers_lower = [h.lower().strip() for h in headers]
    for idx, h in enumerate(headers_lower):
        if 'email validation' in h or h == 'email validation status':
            return idx
    return None

def find_email_address_column(headers):
    """Find the main email address column (for enriched CSVs)."""
    headers_lower = [h.lower().strip() for h in headers]
    for idx, h in enumerate(headers_lower):
        if h == 'email address' or h == 'email':
            return idx
    return None

def process_csv_file(filepath):
    """Process a single CSV file and return results."""
    filepath = Path(filepath)
    relative_path = filepath.relative_to(BASE_DIR)
    results = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            headers = next(reader)
            
            email_col = find_email_address_column(headers)
            validation_col = find_validation_status_column(headers)
            website_col = find_website_column(headers)
            
            # Also scan ALL columns for emails
            all_emails_found = []
            businesses_needing_website_visit = []
            validation_updates = []
            
            for row_idx, row in enumerate(reader):
                if not row:
                    continue
                
                business_name = row[0] if row else 'Unknown'
                
                # Collect emails from all columns
                row_emails = []
                for col_idx, cell in enumerate(row):
                    found = extract_emails(cell)
                    row_emails.extend(found)
                
                # Validate each unique email
                unique_emails = list(set(e.lower() for e in row_emails))
                email_results = []
                for email in unique_emails:
                    status, detail = validate_email_dns(email)
                    email_results.append({
                        'email': email,
                        'status': status,
                        'detail': detail
                    })
                    all_emails_found.append({
                        'file': str(relative_path),
                        'row': row_idx + 2,
                        'business_name': business_name,
                        'email': email,
                        'status': status,
                        'detail': detail
                    })
                
                # Check if business has website but no emails
                website_url = None
                if website_col and website_col < len(row):
                    website_url = row[website_col]
                elif len(row) > 6:  # Standard GMB format: col 6 is Website
                    website_url = row[6]
                
                # Also check for verified website column
                if not website_url or website_url.strip() in ('Not Available', ''):
                    # Check for "Website (Verified)" column
                    for col_idx, h in enumerate(headers):
                        if 'website' in h.lower() and 'verified' in h.lower() and col_idx < len(row):
                            if row[col_idx].strip() not in ('Not Available', '', 'N/A'):
                                website_url = row[col_idx]
                                break
                
                # Check email from specific column
                has_email = len(unique_emails) > 0
                if not has_email and email_col is not None and email_col < len(row):
                    cell_emails = extract_emails(row[email_col])
                    if cell_emails:
                        has_email = True
                
                if is_valid_website(website_url) and not has_email:
                    area = 'Unknown'
                    if len(row) > 3:
                        area = row[3]
                    businesses_needing_website_visit.append({
                        'file': str(relative_path),
                        'row': row_idx + 2,
                        'business_name': business_name,
                        'business_niche': row[1] if len(row) > 1 else '',
                        'address': row[2] if len(row) > 2 else '',
                        'city_area': area,
                        'website': website_url,
                        'phone': row[4] if len(row) > 4 else ''
                    })
                
                # Track validation updates needed
                if validation_col is not None and email_results:
                    # Find the best status for this row
                    best_status = 'N/A'
                    for er in email_results:
                        if er['status'] in ('valid_mx', 'valid_a_record'):
                            best_status = f"valid_{er['status'].replace('valid_', '')}"
                            break
                        elif er['status'] == 'no_mail_server' and best_status == 'N/A':
                            best_status = 'no_mail_server'
                    
                    if best_status != 'N/A':
                        validation_updates.append({
                            'file': str(filepath),
                            'row': row_idx + 2,
                            'col': validation_col,
                            'new_value': best_status,
                            'emails_validated': [er['email'] for er in email_results]
                        })
            
            return {
                'file': str(relative_path),
                'total_emails_found': len(all_emails_found),
                'email_details': all_emails_found,
                'businesses_needing_website_visit': businesses_needing_website_visit,
                'validation_updates': validation_updates,
                'has_validation_column': validation_col is not None,
                'headers': headers
            }
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return {
            'file': str(relative_path),
            'error': str(e),
            'total_emails_found': 0,
            'email_details': [],
            'businesses_needing_website_visit': [],
            'validation_updates': [],
            'has_validation_column': False,
            'headers': []
        }

def apply_validation_updates(updates_by_file):
    """Apply validation updates to CSV files."""
    for filepath_str, updates in updates_by_file.items():
        filepath = Path(filepath_str)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            lines = content.split('\n')
            
            # Find the header to confirm column
            reader = csv.reader(lines)
            headers = next(reader)
            rows = list(reader)
            
            for update in updates:
                row_idx = update['row'] - 2  # Convert to 0-based
                col_idx = update['col']
                if row_idx < len(rows) and col_idx < len(rows[row_idx]):
                    old_val = rows[row_idx][col_idx]
                    if old_val.strip() in ('Pending Validation', 'N/A', ''):
                        rows[row_idx][col_idx] = update['new_value']
            
            # Write back
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)
            
            print(f"  Updated {len(updates)} rows in {filepath.name}")
        except Exception as e:
            print(f"  Error updating {filepath}: {e}")

def main():
    print("=" * 70)
    print("NIGERIA DNS EMAIL VALIDATION")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}")
    
    # Find all CSV files
    csv_files = list(BASE_DIR.rglob("*.csv"))
    print(f"\nFound {len(csv_files)} CSV files in Nigeria directory")
    
    # Process all files
    all_results = []
    all_emails = []
    all_needing_visits = []
    updates_by_file = {}
    
    # Priority areas
    priority_areas = ['Victoria-Island', 'Ikeja', 'Lekki']
    
    print("\n--- Processing CSV Files ---")
    for csv_file in csv_files:
        relative = str(csv_file.relative_to(BASE_DIR))
        result = process_csv_file(csv_file)
        all_results.append(result)
        
        all_emails.extend(result.get('email_details', []))
        all_needing_visits.extend(result.get('businesses_needing_website_visit', []))
        
        if result.get('validation_updates'):
            file_key = str(csv_file)
            if file_key not in updates_by_file:
                updates_by_file[file_key] = []
            updates_by_file[file_key].extend(result['validation_updates'])
        
        print(f"  {relative}: {result['total_emails_found']} emails, "
              f"{len(result.get('businesses_needing_website_visit', []))} need visit")
    
    # Categorize email results
    valid_mx = [e for e in all_emails if e['status'] == 'valid_mx']
    valid_a = [e for e in all_emails if e['status'] == 'valid_a_record']
    no_mail = [e for e in all_emails if e['status'] == 'no_mail_server']
    invalid = [e for e in all_emails if e['status'] == 'invalid_format']
    
    print(f"\n--- Email Validation Summary ---")
    print(f"  Total unique emails found: {len(all_emails)}")
    print(f"  Valid (MX records): {len(valid_mx)}")
    print(f"  Valid (A record only): {len(valid_a)}")
    print(f"  No mail server: {len(no_mail)}")
    print(f"  Invalid format: {len(invalid)}")
    
    # Deduplicate businesses needing visits (by website URL)
    seen_websites = set()
    deduped_needing_visits = []
    for biz in all_needing_visits:
        url_key = biz['website'].lower().rstrip('/')
        if url_key not in seen_websites:
            seen_websites.add(url_key)
            deduped_needing_visits.append(biz)
    
    print(f"\n--- Businesses Needing Website Visits ---")
    print(f"  Total (before dedup): {len(all_needing_visits)}")
    print(f"  Unique websites: {len(deduped_needing_visits)}")
    
    # Sort by priority area
    def sort_key(biz):
        for i, area in enumerate(priority_areas):
            if area.lower() in biz['city_area'].lower() or area.lower() in biz['file'].lower():
                return i
        return len(priority_areas)
    
    deduped_needing_visits.sort(key=sort_key)
    
    # Priority area breakdown
    print(f"\n  By area:")
    for area in priority_areas:
        count = len([b for b in deduped_needing_visits if area.lower() in b['city_area'].lower() or area.lower() in b['file'].lower()])
        print(f"    {area}: {count}")
    
    # Build results JSON
    validation_results = {
        'generated': datetime.now().isoformat(),
        'summary': {
            'total_csvs_processed': len(csv_files),
            'total_emails_found': len(all_emails),
            'valid_mx': len(valid_mx),
            'valid_a_record': len(valid_a),
            'no_mail_server': len(no_mail),
            'invalid_format': len(invalid),
            'businesses_needing_visit': len(deduped_needing_visits)
        },
        'email_validations': all_emails,
        'valid_mx_emails': [e['email'] for e in valid_mx],
        'valid_a_record_emails': [e['email'] for e in valid_a],
        'no_mail_server_emails': [{'email': e['email'], 'detail': e['detail']} for e in no_mail],
    }
    
    websites_needing = {
        'generated': datetime.now().isoformat(),
        'total': len(deduped_needing_visits),
        'businesses': deduped_needing_visits
    }
    
    # Apply validation updates to CSVs
    print(f"\n--- Applying Validation Updates to CSVs ---")
    apply_validation_updates(updates_by_file)
    
    # Save results
    with open(TOOLS_DIR / 'nigeria_dns_validation_results.json', 'w') as f:
        json.dump(validation_results, f, indent=2)
    print(f"\n  Saved: nigeria_dns_validation_results.json")
    
    with open(TOOLS_DIR / 'nigeria_websites_needing_email.json', 'w') as f:
        json.dump(websites_needing, f, indent=2)
    print(f"  Saved: nigeria_websites_needing_email.json")
    
    # Print top websites to visit
    print(f"\n--- Top 50 Websites to Visit (Priority Order) ---")
    for i, biz in enumerate(deduped_needing_visits[:50]):
        print(f"  {i+1}. [{biz['city_area']}] {biz['business_name']} - {biz['website']}")
    
    print(f"\n{'=' * 70}")
    print(f"Completed: {datetime.now().isoformat()}")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()
