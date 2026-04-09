#!/usr/bin/env python3
"""
Ghana Business Email Extractor
Visits websites to find real contact emails for businesses.
"""

import urllib.request
import urllib.error
import ssl
import re
import json
import time
import sys
from urllib.parse import urljoin, urlparse
from pathlib import Path

# SSL context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Domains to skip - not real business emails
SKIP_EMAIL_DOMAINS = [
    'example.com', 'test.com', 'domain.com', 'email.com', 'wixpress.com',
    'sentry.io', 'googleapis.com', 'purl.org', 'schema.org', 'fontawesome.com',
    'bootstrapcdn.com', 'w3.org', 'jquery.com', 'google-analytics.com',
    'doubleclick.net', 'googleadservices.com', 'googleusercontent.com',
    'gravatar.com', 'wordpress.org', 'cloudflare.com', 'p3.amazonaws.com',
    'google.com', 'facebook.com', 'twitter.com', 'instagram.com',
    'linkedin.com', 'youtube.com', 'addthis.com', 'sharethis.com',
    'disqus.com', 'livefyre.com', 'typekit.net', 'fonts.googleapis.com',
    'cdnjs.cloudflare.com', 'unpkg.com', 'npmjs.com', 'github.com',
    'stackoverflow.com', 'microsoft.com', 'apple.com', 'amazon.com',
    'mapbox.com', 'leafletjs.com', 'olark.com', 'intercom.io',
    'hubspot.com', 'mailchimp.com', 'constantcontact.com',
    'recaptcha.net', 'hcaptcha.com', 'turnstile',
    'jetpack.com', 'yoast.com', 'wp.com', 'automattic.com',
]

def is_valid_business_email(email):
    """Check if email looks like a legitimate business contact email."""
    email_lower = email.lower().strip()
    
    # Skip no-reply emails
    if email_lower.startswith('noreply') or email_lower.startswith('no-reply'):
        return False
    # Skip system emails
    if email_lower.startswith('webmaster@') or email_lower.startswith('postmaster@'):
        return False
    # Skip placeholder emails
    skip_patterns = ['placeholder', 'lorem', 'ipsum', 'sample', 'yourdomain', 
                     'your.email', 'test123', 'xxxx', 'zzzz', 'aaaa']
    for p in skip_patterns:
        if p in email_lower:
            return False
    # Check domain
    domain = email_lower.split('@')[1] if '@' in email_lower else ''
    for skip in SKIP_EMAIL_DOMAINS:
        if skip in domain:
            return False
    
    return True

def fetch_page(url, timeout=15):
    """Fetch page content from URL."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'text' not in content_type.lower() and 'html' not in content_type.lower():
                return None
            # Check for redirect
            final_url = response.url
            return response.read().decode('utf-8', errors='ignore'), final_url
    except Exception as e:
        return None

def extract_emails_from_html(html):
    """Extract email addresses from HTML content."""
    if not html:
        return []
    
    emails = set()
    
    # Standard email pattern
    for email in re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', html):
        if is_valid_business_email(email):
            emails.add(email.lower())
    
    # Mailto links
    for email in re.findall(r'mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})', html):
        if is_valid_business_email(email):
            emails.add(email.lower())
    
    # Cloudflare encoded emails (data-cfemail)
    cf_emails = re.findall(r'data-cfemail="([a-f0-9]+)"', html)
    for encoded in cf_emails:
        try:
            decoded = decode_cf_email(encoded)
            if decoded and is_valid_business_email(decoded):
                emails.add(decoded.lower())
        except:
            pass
    
    # JavaScript encoded emails
    js_emails = re.findall(r"['\"]([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})['\"]", html)
    for email in js_emails:
        if is_valid_business_email(email):
            emails.add(email.lower())
    
    # Base64 encoded mailto
    b64_mailto = re.findall(r'atob\([\'"]([^\'"]+)[\'"]\)', html)
    for b64 in b64_mailto:
        try:
            import base64
            decoded = base64.b64decode(b64).decode('utf-8', errors='ignore')
            for email in re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', decoded):
                if is_valid_business_email(email):
                    emails.add(email.lower())
        except:
            pass
    
    return list(emails)

def decode_cf_email(encoded):
    """Decode Cloudflare email protection."""
    if not encoded or len(encoded) < 4:
        return None
    try:
        key = int(encoded[:2], 16)
        decoded = []
        for i in range(2, len(encoded), 2):
            char_code = int(encoded[i:i+2], 16) ^ key
            decoded.append(chr(char_code))
        email = ''.join(decoded)
        if '@' in email and '.' in email.split('@')[-1]:
            return email
    except:
        pass
    return None

def find_contact_urls(html, base_url):
    """Find contact page URLs in HTML."""
    contact_urls = set()
    
    # Look for contact links
    patterns = [
        r'href=["\']([^"\']*(?:contact|reach|inquir|get-intouch|get-in-touch)[^"\']*)["\']',
        r'href=["\']([^"\']*/contact/?)["\']',
    ]
    
    for pattern in patterns:
        for link in re.findall(pattern, html, re.IGNORECASE):
            full_url = urljoin(base_url, link)
            # Skip javascript and anchors
            if not full_url.startswith('javascript') and not full_url.startswith('#'):
                contact_urls.add(full_url.split('#')[0].split('?')[0])
    
    return list(contact_urls)

def process_website(business):
    """Process a single website to extract emails."""
    website = business['website']
    bname = business['business_name']
    
    result = {
        'business_name': bname,
        'website': website,
        'csv_file': business['csv_file'],
        'area': business.get('area', ''),
        'extracted_emails': [],
        'status': 'not_found',
        'notes': ''
    }
    
    # Skip known invalid sites
    skip_sites = ['kfc.com.gh', 'marriott.com', 'the-ascott.com', 'hilton.com',
                  'iom.int', 'jica.go.jp', 'ecobank.com', 'mtn.com.gh']
    domain = urlparse(website).netloc.lower()
    for skip in skip_sites:
        if skip in domain:
            result['status'] = 'skipped'
            result['notes'] = 'Corporate/international chain - contact not specific to Ghana location'
            return result
    
    # Skip embassy/government sites
    gov_keywords = ['embassy', 'consulate', 'hciaccra', 'ssnit.org', 'bost.com.gh',
                    'wishesalliance.org', 'westafrican-rescue.com']
    for kw in gov_keywords:
        if kw in website.lower():
            result['status'] = 'skipped'
            result['notes'] = 'Government/international organization'
            return result
    
    all_emails = set()
    pages_visited = []
    
    # 1. Try homepage
    page_result = fetch_page(website)
    if page_result is None:
        result['status'] = 'error'
        result['notes'] = 'Could not fetch page'
        return result
    
    html, final_url = page_result
    pages_visited.append('homepage')
    
    homepage_emails = extract_emails_from_html(html)
    all_emails.update(homepage_emails)
    
    # 2. Find and try contact pages
    contact_urls = find_contact_urls(html, final_url)
    
    # Always try /contact and /contact-us
    for suffix in ['/contact', '/contact-us', '/en/contact']:
        contact_url = final_url.rstrip('/') + suffix
        if contact_url not in contact_urls:
            contact_urls.append(contact_url)
    
    for c_url in contact_urls[:3]:  # Max 3 contact pages
        time.sleep(1)
        c_result = fetch_page(c_url)
        if c_result:
            c_html, c_final = c_result
            c_emails = extract_emails_from_html(c_html)
            all_emails.update(c_emails)
            pages_visited.append(c_url)
    
    # 3. Filter: prefer domain-specific emails
    site_domain = urlparse(final_url).netloc.lower()
    domain_emails = [e for e in all_emails if site_domain in e]
    other_emails = [e for e in all_emails if site_domain not in e]
    
    # Prioritize domain emails
    final_emails = domain_emails if domain_emails else other_emails
    
    if final_emails:
        result['extracted_emails'] = final_emails
        result['status'] = 'found'
        domain_note = '(domain-specific)' if domain_emails else '(third-party domain)'
        result['notes'] = f"Found {len(final_emails)} email(s) {domain_note} across {len(pages_visited)} page(s)"
    else:
        result['notes'] = f'Visited {len(pages_visited)} page(s), no emails found'
    
    return result

def main():
    queue_file = Path(__file__).parent / 'ghana_email_batch2_queue.json'
    output_file = Path(__file__).parent / 'ghana_emails_batch_remaining.json'
    
    if not queue_file.exists():
        print(f"Queue file not found: {queue_file}")
        sys.exit(1)
    
    with open(queue_file) as f:
        queue = json.load(f)
    
    print(f"Processing {len(queue)} websites...")
    results = []
    
    for i, business in enumerate(queue):
        print(f"\n[{i+1}/{len(queue)}] {business['business_name']}")
        print(f"  URL: {business['website']}")
        
        result = process_website(business)
        results.append(result)
        
        if result['status'] == 'found':
            print(f"  ✓ FOUND: {result['extracted_emails']}")
        elif result['status'] == 'skipped':
            print(f"  ⊘ SKIPPED: {result['notes']}")
        elif result['status'] == 'error':
            print(f"  ✗ ERROR: {result['notes']}")
        else:
            print(f"  - NOT FOUND: {result['notes']}")
        
        # Save progress after each site
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Delay between requests
        time.sleep(2)
    
    # Summary
    found = sum(1 for r in results if r['status'] == 'found')
    not_found = sum(1 for r in results if r['status'] == 'not_found')
    errors = sum(1 for r in results if r['status'] == 'error')
    skipped = sum(1 for r in results if r['status'] == 'skipped')
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total processed: {len(results)}")
    print(f"Emails found: {found}")
    print(f"Not found: {not_found}")
    print(f"Errors: {errors}")
    print(f"Skipped: {skipped}")
    print(f"\nResults saved to: {output_file}")

if __name__ == '__main__':
    main()
