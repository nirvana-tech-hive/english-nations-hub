#!/usr/bin/env python3
"""
Osu Accra GMB Lead Scraper - Using agent-browser via Bing Maps
Processes snapshot data and manages CSV output
"""
import csv
import os
import re
import subprocess
import json
import time

BASE_DIR = "/home/z/my-project/repo/countries/Ghana/Greater-Accra/Accra/Osu/GMB_Leads"
NICHES_DIR = os.path.join(BASE_DIR, "Niches")
RAW_DIR = os.path.join(BASE_DIR, "Raw_Leads")
DATE = "2026-04-05"

os.makedirs(NICHES_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

NICHES = {
    "restaurant": "restaurants Osu Accra Ghana",
    "bar": "bars pubs Osu Accra Ghana",
    "hotel": "hotels Osu Accra Ghana",
    "cafe": "cafes Osu Accra Ghana",
    "bakery": "bakeries Osu Accra Ghana",
    "fast_food": "fast food Osu Accra Ghana",
    "pharmacy": "pharmacy Osu Accra Ghana",
    "hospital_clinic": "hospital clinic Osu Accra Ghana",
    "gym": "gym fitness Osu Accra Ghana",
    "salon": "salon Osu Accra Ghana",
    "spa": "spa Osu Accra Ghana",
    "it_company": "IT companies Osu Accra Ghana",
    "law_firm": "law firms Osu Accra Ghana",
    "real_estate": "real estate agents Osu Accra Ghana",
    "marketing_agency": "marketing agencies Osu Accra Ghana",
    "accounting_firm": "accounting firms Osu Accra Ghana",
    "bank": "banks Osu Accra Ghana",
    "insurance": "insurance Osu Accra Ghana",
    "supermarket": "supermarkets Osu Accra Ghana",
    "fashion_boutique": "fashion boutiques Osu Accra Ghana",
    "electronics": "electronics Osu Accra Ghana",
    "car_dealership": "car dealerships Osu Accra Ghana",
    "printing_service": "printing services Osu Accra Ghana",
    "event_planning": "event planning Osu Accra Ghana",
    "photography": "photography Osu Accra Ghana",
    "church": "churches Osu Accra Ghana",
    "school": "schools Osu Accra Ghana",
    "travel_agency": "travel agencies Osu Accra Ghana",
    "nightclub": "nightclubs Osu Accra Ghana",
    "art_gallery": "art galleries Osu Accra Ghana",
}

CSV_HEADER = "business_name,niche,address,phone,whatsapp,website,email,source_url,date_collected"

def run_browser(cmd, timeout=15):
    """Run agent-browser command and return output"""
    try:
        result = subprocess.run(
            f"agent-browser {cmd}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        return f"ERROR: {e}"

def search_bing_maps(query):
    """Search Bing Maps and return snapshot"""
    import urllib.parse
    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.bing.com/maps/search?q={encoded}"
    run_browser(f'open "{url}"', timeout=30)
    time.sleep(4)
    output = run_browser("snapshot -c", timeout=15)
    return output

def parse_list_results(snapshot_text):
    """Parse business entries from Bing Maps compact snapshot"""
    results = []
    # Match button text patterns: "BusinessName rating info address phone"
    # Pattern: button "NAME RATING/5 (N reviews) TYPE · $$ ADDRESS ... PHONE"
    
    lines = snapshot_text.split('\n')
    current_name = ""
    current_phone = ""
    current_address = ""
    
    for line in lines:
        line = line.strip()
        # Look for button lines with business info
        if line.startswith('- button "') and '/5' in line:
            # Extract button content
            match = re.match(r'- button "([^"]+)"', line)
            if match:
                content = match.group(1)
                # Try to extract phone number
                phone_match = re.search(r'\+233[\s\d]+$', content)
                phone = phone_match.group(0).strip() if phone_match else ""
                
                # Extract rating
                rating_match = re.search(r'(\d\.?\d?)/5\s*\((\d+)\s*reviews?\)', content)
                rating = f"{rating_match.group(1)}/5" if rating_match else ""
                
                # Extract business name (everything before the rating)
                if rating_match:
                    name = content[:rating_match.start()].strip()
                    # Remove trailing punctuation
                    name = name.rstrip(' ,')
                    if name:
                        current_name = name
                        current_phone = phone
                        
                        # Extract address - between rating and phone
                        after_rating = content[rating_match.end():]
                        if phone:
                            address = after_rating[:after_rating.rfind(phone)].strip()
                        else:
                            address = after_rating.strip()
                        # Clean up address
                        address = re.sub(r'^\s*[·]\s*', '', address)
                        address = re.sub(r'\s*Closed.*$', '', address)
                        address = re.sub(r'\s*Open.*$', '', address)
                        address = re.sub(r'\s*Opens.*$', '', address)
                        address = re.sub(r'\s*Closes.*$', '', address)
                        address = address.strip(' ·$').strip()
                        current_address = address
                        
                        results.append({
                            'name': current_name,
                            'address': current_address,
                            'phone': current_phone,
                            'rating': rating
                        })
        elif line.startswith('- link "https://') and current_name:
            # Website link found near current business
            pass
    
    return results

def get_detail_info(idx):
    """Click on result item and get website details"""
    # Find the button ref for item index
    output = run_browser("snapshot -i", timeout=15)
    if not output:
        return "", ""
    
    # Find the nth listitem button
    lines = output.split('\n')
    target_ref = None
    count = 0
    
    for line in lines:
        if 'listitem' in line and f'Item {idx+1}' in line:
            # Look for the next button on subsequent lines
            pass
        if 'button "' in line and '/5' in line and count == idx:
            ref_match = re.search(r'\[ref=([^\]]+)\]', line)
            if ref_match:
                target_ref = f"@{ref_match.group(1)}"
                break
        if 'button "' in line and '/5' in line:
            count += 1
    
    if not target_ref:
        # Try alternative: look for listitem with correct item number
        for i, line in enumerate(lines):
            if f'Item {idx+1} of' in line:
                # Check next few lines for a button
                for j in range(i+1, min(i+5, len(lines))):
                    ref_match = re.search(r'\[ref=([^\]]+)\]', lines[j])
                    if ref_match:
                        target_ref = f"@{ref_match.group(1)}"
                        break
                break
    
    if not target_ref:
        return "", ""
    
    run_browser(f"click {target_ref}", timeout=10)
    time.sleep(2)
    
    output = run_browser("snapshot -c", timeout=15)
    website = ""
    email = ""
    
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith('- link "https://') and not any(x in line for x in ['bing.com', 'microsoft.com', 'tripadvisor', 'facebook', 'openstreetmap']):
            url_match = re.match(r'- link "(https?://[^"]+)"', line)
            if url_match:
                website = url_match.group(1)
        if '@' in line and '.com' in line and 'StaticText' in line:
            email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', line)
            if email_match:
                email = email_match.group(0)
    
    # Go back - click the list area
    time.sleep(1)
    run_browser("snapshot -i", timeout=10)
    # Click back on the list
    output2 = run_browser("snapshot -i", timeout=10)
    for line in output2.split('\n'):
        if 'Close details card' in line:
            ref_match = re.search(r'\[ref=([^\]]+)\]', line)
            if ref_match:
                run_browser(f"click @{ref_match.group(1)}", timeout=10)
                time.sleep(1)
                break
    
    return website, email

def save_csv(niche_key, leads):
    """Save leads to CSV file"""
    filepath = os.path.join(NICHES_DIR, f"{niche_key}.csv")
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER.split(','))
        for lead in leads:
            writer.writerow([
                lead.get('business_name', ''),
                lead.get('niche', niche_key),
                lead.get('address', ''),
                lead.get('phone', ''),
                lead.get('whatsapp', ''),
                lead.get('website', ''),
                lead.get('email', ''),
                lead.get('source_url', 'https://www.bing.com/maps'),
                DATE
            ])
    return len(leads)

def save_raw_all(all_leads):
    """Save all leads to raw file"""
    filepath = os.path.join(RAW_DIR, "raw_leads.csv")
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER.split(','))
        for lead in all_leads:
            writer.writerow([
                lead.get('business_name', ''),
                lead.get('niche', ''),
                lead.get('address', ''),
                lead.get('phone', ''),
                lead.get('whatsapp', ''),
                lead.get('website', ''),
                lead.get('email', ''),
                lead.get('source_url', 'https://www.bing.com/maps'),
                DATE
            ])
    return len(all_leads)

if __name__ == "__main__":
    all_leads = []
    seen_names = set()
    
    # Get list of already-processed niches
    done_file = os.path.join(BASE_DIR, ".done_niches.txt")
    done_niches = set()
    if os.path.exists(done_file):
        with open(done_file) as f:
            done_niches = set(line.strip() for line in f if line.strip())
    
    for niche_key, query in NICHES.items():
        if niche_key in done_niches:
            print(f"SKIP {niche_key} (already done)")
            # Load existing leads
            filepath = os.path.join(NICHES_DIR, f"{niche_key}.csv")
            if os.path.exists(filepath):
                with open(filepath, encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        all_leads.append(row)
            continue
        
        print(f"\n=== SEARCHING: {niche_key} ===")
        print(f"Query: {query}")
        
        snapshot = search_bing_maps(query)
        results = parse_list_results(snapshot)
        print(f"  Found {len(results)} results from list")
        
        leads = []
        for i, r in enumerate(results):
            name = r['name']
            if name in seen_names:
                continue
            seen_names.add(name)
            
            lead = {
                'business_name': name,
                'niche': niche_key,
                'address': r.get('address', ''),
                'phone': r.get('phone', ''),
                'whatsapp': '',
                'website': '',
                'email': '',
                'source_url': 'https://www.bing.com/maps',
            }
            
            # Try to get detail info (website)
            print(f"  [{i+1}] {name}")
            try:
                website, email = get_detail_info(i)
                if website:
                    lead['website'] = website
                if email:
                    lead['email'] = email
                if website:
                    print(f"       -> Website: {website}")
            except Exception as e:
                print(f"       -> Detail error: {e}")
            
            leads.append(lead)
        
        count = save_csv(niche_key, leads)
        print(f"  Saved {count} leads to {niche_key}.csv")
        all_leads.extend(leads)
        
        # Mark as done
        with open(done_file, 'a') as f:
            f.write(niche_key + '\n')
        
        # Save raw after each niche
        save_raw_all(all_leads)
        print(f"  Total leads so far: {len(all_leads)}")
    
    print(f"\n=== FINAL SUMMARY ===")
    print(f"Total leads collected: {len(all_leads)}")
    save_raw_all(all_leads)
