#!/usr/bin/env python3
"""
Nigeria Website Email Extraction Script
Visits business websites to find real email addresses.
Uses page_reader approach: main page + contact pages.
"""

import json
import re
import time
import csv
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip install --break-system-packages requests beautifulsoup4")
    import requests
    from bs4 import BeautifulSoup

TOOLS_DIR = Path("/home/z/my-project/english-nations-hub/tools")
BASE_DIR = Path("/home/z/my-project/english-nations-hub/countries/Nigeria")

EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)

# Skip these domains (not useful for email extraction)
SKIP_DOMAINS = [
    'facebook.com', 'instagram.com', 'twitter.com', 'x.com',
    'linkedin.com', 'tiktok.com', 'youtube.com', 'wa.me',
    'gov.ng', 'google.com/maps', 'maps.google.com',
    'tripadvisor.com', 'yelp.com', 'radissonhotels.com',
    'marriott.com', 'hardrock.com', 'accenture.com',
    'citigroup.com', 'toyota.com', 'shoprite.ng',
    'startupblink.com', 'startuplagos.net',
    'italawa.com.ng',  # directory listing, not business site
]

# Common email-like patterns that are NOT real emails
FALSE_POSITIVES = [
    'example.com', 'email.com', 'domain.com', 'yourdomain.com',
    'company.com', 'yoursite.com', 'website.com', 'test.com',
    'sample.com', 'mydomain.com', 'mail.com',
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

def is_skip_url(url):
    """Check if URL should be skipped."""
    url_lower = url.lower()
    for skip in SKIP_DOMAINS:
        if skip in url_lower:
            return True
    return False

def is_valid_email(email):
    """Validate that an email looks real (not a false positive)."""
    email = email.lower().strip()
    if len(email) < 6 or len(email) > 60:
        return False
    for fp in FALSE_POSITIVES:
        if fp in email:
            return False
    # Must have at least one character before @
    if email.startswith('@'):
        return False
    return True

def extract_emails_from_text(text):
    """Extract valid emails from text."""
    if not text:
        return []
    emails = EMAIL_PATTERN.findall(text)
    valid = [e.lower() for e in emails if is_valid_email(e)]
    return list(set(valid))

def get_contact_urls(base_url):
    """Generate possible contact page URLs."""
    urls = []
    base = base_url.rstrip('/')
    urls.append(base)  # Main page
    urls.append(f"{base}/contact")
    urls.append(f"{base}/contact-us")
    urls.append(f"{base}/contactus")
    urls.append(f"{base}/about")
    urls.append(f"{base}/about-us")
    return urls

def fetch_page(url, timeout=10):
    """Fetch a webpage and return content."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        pass
    return None

def extract_emails_from_website(url):
    """Visit a website and extract emails from main + contact pages."""
    all_emails = set()
    pages_visited = []
    
    if is_skip_url(url):
        return [], [], True
    
    contact_urls = get_contact_urls(url)
    
    for page_url in contact_urls:
        content = fetch_page(page_url)
        if content:
            pages_visited.append(page_url)
            # Extract from raw text
            emails = extract_emails_from_text(content)
            all_emails.update(emails)
            
            # Also parse HTML for mailto links and visible text
            try:
                soup = BeautifulSoup(content, 'html.parser')
                # Check mailto links
                for a_tag in soup.find_all('a', href=True):
                    href = a_tag['href']
                    if 'mailto:' in href.lower():
                        email = href.split(':', 1)[1].split('?')[0].strip()
                        if is_valid_email(email):
                            all_emails.add(email.lower())
                
                # Check meta tags
                for meta in soup.find_all('meta'):
                    content_attr = meta.get('content', '')
                    emails = extract_emails_from_text(content_attr)
                    all_emails.update(emails)
            except Exception:
                pass
            
            # If we found emails on main page, no need to visit contact
            if len(all_emails) > 0 and pages_visited.index(page_url) == 0:
                break
        
        time.sleep(1)  # Be polite
    
    return list(all_emails), pages_visited, False

def load_websites_to_visit():
    """Load the list of websites needing email extraction."""
    filepath = TOOLS_DIR / 'nigeria_websites_needing_email.json'
    if not filepath.exists():
        print("ERROR: nigeria_websites_needing_email.json not found!")
        return []
    
    with open(filepath) as f:
        data = json.load(f)
    
    # Filter out already-known emails and duplicates
    # Load existing emails from enriched CSVs
    existing_emails = set()
    for csv_file in BASE_DIR.rglob("*.csv"):
        try:
            with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            emails = EMAIL_PATTERN.findall(content)
            existing_emails.update(e.lower() for e in emails)
        except Exception:
            pass
    
    # Filter businesses
    businesses = data['businesses']
    to_visit = []
    visited_urls = set()
    
    for biz in businesses:
        url = biz['website']
        url_key = url.lower().rstrip('/')
        if url_key in visited_urls:
            continue
        if is_skip_url(url):
            continue
        visited_urls.add(url_key)
        to_visit.append(biz)
    
    print(f"  Total businesses to visit: {len(to_visit)}")
    print(f"  Existing emails in CSVs: {len(existing_emails)}")
    return to_visit

def process_business(biz):
    """Process a single business - visit website and extract emails."""
    url = biz['website']
    emails, pages_visited, skipped = extract_emails_from_website(url)
    
    return {
        'business_name': biz['business_name'],
        'website': url,
        'business_niche': biz.get('business_niche', ''),
        'city_area': biz.get('city_area', ''),
        'file': biz.get('file', ''),
        'row': biz.get('row', 0),
        'emails_found': emails,
        'pages_visited': pages_visited,
        'skipped': skipped,
        'phone': biz.get('phone', '')
    }

def main():
    print("=" * 70)
    print("NIGERIA WEBSITE EMAIL EXTRACTION")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}")
    
    businesses = load_websites_to_visit()
    if not businesses:
        print("No businesses to visit!")
        return
    
    results = []
    emails_found_total = 0
    sites_visited = 0
    sites_skipped = 0
    sites_with_emails = 0
    
    # Process at least 40 websites
    target = min(len(businesses), 45)
    print(f"\n--- Visiting up to {target} websites ---\n")
    
    for i, biz in enumerate(businesses[:target]):
        print(f"  [{i+1}/{target}] {biz['business_name'][:40]:40s} -> {biz['website'][:50]}")
        result = process_business(biz)
        results.append(result)
        
        if result['skipped']:
            sites_skipped += 1
            print(f"           SKIPPED (skip list)")
        elif result['emails_found']:
            sites_visited += 1
            sites_with_emails += 1
            emails_found_total += len(result['emails_found'])
            print(f"           FOUND {len(result['emails_found'])} email(s): {', '.join(result['emails_found'][:3])}")
        else:
            sites_visited += 1
            print(f"           No emails found")
        
        time.sleep(2)  # 2-second delay between requests
    
    print(f"\n--- Extraction Summary ---")
    print(f"  Sites processed: {sites_visited + sites_skipped}")
    print(f"  Sites visited: {sites_visited}")
    print(f"  Sites skipped: {sites_skipped}")
    print(f"  Sites with emails: {sites_with_emails}")
    print(f"  Total emails found: {emails_found_total}")
    
    # Save results
    output = {
        'generated': datetime.now().isoformat(),
        'summary': {
            'sites_processed': sites_visited + sites_skipped,
            'sites_visited': sites_visited,
            'sites_skipped': sites_skipped,
            'sites_with_emails': sites_with_emails,
            'total_emails_found': emails_found_total
        },
        'results': results,
        'businesses_with_emails': [r for r in results if r['emails_found']]
    }
    
    with open(TOOLS_DIR / 'nigeria_emails_found.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Saved: nigeria_emails_found.json")
    
    # Print all emails found
    print(f"\n--- All Emails Found ({emails_found_total}) ---")
    for r in results:
        if r['emails_found']:
            for email in r['emails_found']:
                print(f"  {email:45s} <- {r['business_name']}")
    
    print(f"\n{'=' * 70}")
    print(f"Completed: {datetime.now().isoformat()}")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()
