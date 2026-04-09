#!/usr/bin/env python3
"""
DNS MX validation for all Kenya and South Africa emails.
Scans all CSV files, validates emails via DNS MX records,
updates email_validation_status column in each CSV.
"""

import csv
import re
import os
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    import dns.resolver
except ImportError:
    print("Installing dnspython...")
    os.system("pip install dnspython --break-system-packages")
    import dns.resolver

BASE_DIR = Path("/home/z/my-project/english-nations-hub/countries")

COUNTRIES = {
    "Kenya": BASE_DIR / "Kenya",
    "South-Africa": BASE_DIR / "South-Africa",
}

EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)

# Cache: domain -> validation result
dns_cache = {}

def extract_emails_from_text(text):
    """Extract all email addresses from a text string."""
    if not text or str(text).strip() in ('', 'Not Available', 'N/A', 'not available', 'none', 'None', '-'):
        return []
    return EMAIL_PATTERN.findall(str(text))

def get_domain_from_email(email):
    """Extract domain from email address."""
    match = re.search(r'@([a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})', email)
    return match.group(1).lower() if match else None

def is_valid_email_format(email):
    """Basic email format check."""
    return bool(EMAIL_PATTERN.fullmatch(email.strip()))

def validate_email_dns(email):
    """
    Validate email by checking DNS MX records (with A record fallback).
    Returns: 'valid_mx', 'valid_a_record', 'invalid_no_mx', or 'invalid_format'
    """
    email = email.strip().lower()
    if not is_valid_email_format(email):
        return 'invalid_format'

    domain = get_domain_from_email(email)
    if not domain:
        return 'invalid_format'

    # Check cache
    if domain in dns_cache:
        return dns_cache[domain]

    # Check MX records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX', lifetime=5)
        if mx_records:
            dns_cache[domain] = 'valid_mx'
            return 'valid_mx'
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        pass
    except dns.resolver.NoNameservers:
        dns_cache[domain] = 'invalid_no_mx'
        return 'invalid_no_mx'
    except Exception:
        pass

    # Fallback: check A record
    try:
        a_records = dns.resolver.resolve(domain, 'A', lifetime=5)
        if a_records:
            dns_cache[domain] = 'valid_a_record'
            return 'valid_a_record'
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        dns_cache[domain] = 'invalid_no_mx'
        return 'invalid_no_mx'
    except Exception:
        pass

    dns_cache[domain] = 'invalid_no_mx'
    return 'invalid_no_mx'

def find_email_columns(headers):
    """Find all column indices where column name contains 'email' (case-insensitive), excluding validation columns."""
    email_cols = []
    validation_col = None
    for idx, h in enumerate(headers):
        h_lower = h.lower().strip()
        if 'email' in h_lower and 'validation' not in h_lower and 'status' not in h_lower and 'source' not in h_lower:
            email_cols.append(idx)
        if 'email_validation_status' == h_lower or 'email validation status' == h_lower:
            validation_col = idx
    return email_cols, validation_col

def process_country(country_name, country_dir):
    """Process all CSV files for a country. Returns summary dict."""
    if not country_dir.exists():
        print(f"  WARNING: Directory does not exist: {country_dir}")
        return None

    csv_files = sorted(country_dir.rglob("*.csv"))
    print(f"\n{'='*70}")
    print(f"  {country_name.upper()}")
    print(f"{'='*70}")
    print(f"  Found {len(csv_files)} CSV files")

    all_unique_emails = set()
    email_status = {}  # email -> status
    files_updated = []
    files_skipped = []
    files_no_emails = []
    total_rows_processed = 0

    for csv_file in csv_files:
        rel_path = csv_file.relative_to(BASE_DIR)

        try:
            with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.reader(f)
                headers = next(reader)
                rows = list(reader)
        except Exception as e:
            print(f"  ERROR reading {rel_path}: {e}")
            files_skipped.append(str(rel_path))
            continue

        email_cols, validation_col = find_email_columns(headers)

        if not email_cols:
            files_no_emails.append(str(rel_path))
            continue

        # Collect all emails from email columns in this file
        file_emails = {}  # row_idx -> list of emails found
        for row_idx, row in enumerate(rows):
            if not row:
                continue
            row_emails = []
            for col in email_cols:
                if col < len(row):
                    found = extract_emails_from_text(row[col])
                    row_emails.extend(found)
            # Deduplicate within row
            unique_row = list(set(e.strip().lower() for e in row_emails))
            if unique_row:
                file_emails[row_idx] = unique_row
                for em in unique_row:
                    all_unique_emails.add(em)

        if not file_emails:
            files_no_emails.append(str(rel_path))
            continue

        total_rows_processed += len(file_emails)

        # Validate all emails (using cache)
        for em in all_unique_emails:
            if em not in email_status:
                email_status[em] = validate_email_dns(em)

        # Determine best validation status per row
        row_statuses = {}
        for row_idx, emails in file_emails.items():
            best = None
            for em in emails:
                st = email_status.get(em, 'invalid_format')
                if st == 'valid_mx':
                    best = 'valid_mx'
                    break
                elif st == 'valid_a_record' and best != 'valid_mx':
                    best = 'valid_a_record'
                elif st == 'invalid_no_mx' and best is None:
                    best = 'invalid_no_mx'
                elif st == 'invalid_format' and best is None:
                    best = 'invalid_format'
            row_statuses[row_idx] = best or 'invalid_format'

        # If no validation column exists, add one
        needs_new_col = validation_col is None
        if needs_new_col:
            headers.append('email_validation_status')

        # Write updated file
        try:
            with open(csv_file, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                for row_idx, row in enumerate(rows):
                    if row_idx in row_statuses:
                        if needs_new_col:
                            row.append(row_statuses[row_idx])
                        else:
                            # Ensure row has enough columns
                            while len(row) <= validation_col:
                                row.append('')
                            row[validation_col] = row_statuses[row_idx]
                    else:
                        if needs_new_col:
                            row.append('')
                    writer.writerow(row)
            files_updated.append(str(rel_path))
        except Exception as e:
            print(f"  ERROR writing {rel_path}: {e}")
            files_skipped.append(str(rel_path))

        # Progress
        if len(files_updated) % 10 == 0 or len(files_updated) == len(csv_files):
            print(f"  Processed {len(files_updated)}/{len(csv_files)} files...")

    # Tally results
    valid_mx_count = sum(1 for s in email_status.values() if s == 'valid_mx')
    valid_a_count = sum(1 for s in email_status.values() if s == 'valid_a_record')
    invalid_no_mx_count = sum(1 for s in email_status.values() if s == 'invalid_no_mx')
    invalid_format_count = sum(1 for s in email_status.values() if s == 'invalid_format')

    summary = {
        'country': country_name,
        'total_csvs': len(csv_files),
        'files_updated': len(files_updated),
        'files_skipped': len(files_skipped),
        'files_no_emails': len(files_no_emails),
        'total_unique_emails': len(all_unique_emails),
        'total_rows_with_emails': total_rows_processed,
        'valid_mx': valid_mx_count,
        'valid_a_record': valid_a_count,
        'invalid_no_mx': invalid_no_mx_count,
        'invalid_format': invalid_format_count,
        'dns_cache_size': len(dns_cache),
        'files_updated_list': files_updated,
    }

    print(f"\n  --- {country_name} Summary ---")
    print(f"  Total CSV files:        {summary['total_csvs']}")
    print(f"  Files with emails:      {summary['files_updated']}")
    print(f"  Files skipped (error):  {summary['files_skipped']}")
    print(f"  Files with no emails:   {summary['files_no_emails']}")
    print(f"  Rows with emails:       {summary['total_rows_with_emails']}")
    print(f"  Unique emails:          {summary['total_unique_emails']}")
    print(f"  Valid (MX records):     {summary['valid_mx']}")
    print(f"  Valid (A record only):  {summary['valid_a_record']}")
    print(f"  Invalid (no MX/A):      {summary['invalid_no_mx']}")
    print(f"  Invalid (bad format):   {summary['invalid_format']}")
    valid_total = summary['valid_mx'] + summary['valid_a_record']
    invalid_total = summary['invalid_no_mx'] + summary['invalid_format']
    print(f"  VALID TOTAL:            {valid_total} ({valid_total*100//max(summary['total_unique_emails'],1)}%)")
    print(f"  INVALID TOTAL:          {invalid_total} ({invalid_total*100//max(summary['total_unique_emails'],1)}%)")

    return summary

def main():
    print("=" * 70)
    print("  DNS MX VALIDATION: KENYA & SOUTH AFRICA EMAILS")
    print("=" * 70)
    print(f"  Started: {datetime.now().isoformat()}")

    summaries = []
    for country_name, country_dir in COUNTRIES.items():
        summary = process_country(country_name, country_dir)
        if summary:
            summaries.append(summary)
        time.sleep(1)  # Brief pause between countries

    # Grand totals
    print(f"\n{'='*70}")
    print("  GRAND TOTAL")
    print(f"{'='*70}")
    total_emails = sum(s['total_unique_emails'] for s in summaries)
    total_valid_mx = sum(s['valid_mx'] for s in summaries)
    total_valid_a = sum(s['valid_a_record'] for s in summaries)
    total_invalid_mx = sum(s['invalid_no_mx'] for s in summaries)
    total_invalid_fmt = sum(s['invalid_format'] for s in summaries)
    total_files_updated = sum(s['files_updated'] for s in summaries)

    print(f"  Total unique emails:   {total_emails}")
    print(f"  Valid (MX):            {total_valid_mx}")
    print(f"  Valid (A record):       {total_valid_a}")
    print(f"  Invalid (no MX/A):      {total_invalid_mx}")
    print(f"  Invalid (bad format):   {total_invalid_fmt}")
    valid = total_valid_mx + total_valid_a
    invalid = total_invalid_mx + total_invalid_fmt
    print(f"  OVERALL VALID:         {valid}/{total_emails} ({valid*100//max(total_emails,1)}%)")
    print(f"  Files updated:         {total_files_updated}")
    print(f"  DNS cache entries:     {len(dns_cache)}")
    print(f"  Completed: {datetime.now().isoformat()}")

    # Return summaries for worklog
    return summaries

if __name__ == '__main__':
    main()
