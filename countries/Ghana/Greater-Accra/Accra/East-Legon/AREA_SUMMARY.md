# Area Summary: East Legon, Accra, Ghana

**Date Collected:** 2026-04-04
**Agent:** LeadCollector-01
**Status:** Organized & Enriched (Validation Pending)

---

## Total Leads by Source

| Source | Count |
|--------|-------|
| GMB Raw Leads | 106 |
| LinkedIn Public Leads | 20 |
| Other Public Web Leads | 48 |
| **Total** | **174** |

---

## Niche Breakdown (from GMB Raw Leads — 106 leads across 20 niches)

| Niche | Count |
|-------|-------|
| Restaurant | 13 |
| Dentist | 13 |
| Interior Design | 8 |
| Photography | 7 |
| Event Planning | 7 |
| Education | 7 |
| Salon | 6 |
| Marketing Agency | 6 |
| Gym & Fitness | 5 |
| Real Estate | 5 |
| Plumbing | 5 |
| Supermarket & Retail | 4 |
| Barbershop | 3 |
| Hotel | 3 |
| Shopping Mall | 3 |
| Law Firm | 3 |
| Restaurant & Bar | 2 |
| Hotel & Restaurant | 2 |
| Restaurant & Cafe | 2 |
| Restaurant & Bakery | 1 |
| **Total** | **106** |

> **Note:** "Akufo-Addo, Prempeh & Co" was parsed as "Akufo-Addo" (business_name) and "Prempeh & Co" (niche) due to an unquoted comma in the business name in raw_leads.csv (line 54). This should be corrected — the business name is "Akufo-Addo, Prempeh & Co" and the niche is "Law Firm". This inflates the niche count by 1 (showing 21 parsed niches instead of 20 actual niches).

---

## LinkedIn Leads Summary

- 20 professional profiles collected
- Includes roles: Real Estate Developer, Real Estate Agent, Restaurant Owner, Business Consultant, Lawyer, Dental Practitioner, Fitness Trainer, Salon Owner, General Manager, Marketing Director, Architect, HR Manager, Hotel Manager, Financial Analyst, Entrepreneur, IT Manager, Business Development Manager
- Many LinkedIn leads map directly to GMB businesses already collected (e.g., Smile 360 Dental Specialists, Body HIIT Fitness Centre, East Legon Dental Clinic)

---

## Web Leads Summary

- 48 web-sourced leads collected
- 43 of 48 have email addresses
- Covers 16 industries/skill categories
- Significant overlap with GMB leads (enables cross-referencing for enrichment)

---

## Enrichment Results

| Metric | Count |
|--------|-------|
| Emails from raw GMB data | 14 |
| Emails from web cross-reference | 25 |
| Emails derived from domain (info@domain) | 36 |
| Leads still missing email | 31 |
| WhatsApp marked (Ghana +233 numbers) | 72 |
| Leads with phone numbers | 73 |
| Leads with websites | 74 |
| Leads missing phone | 33 |
| Leads missing website | 32 |

---

## Data Quality Notes

1. **CSV Formatting Issue:** Line 54 of raw_leads.csv has an unquoted comma in the business name "Akufo-Addo, Prempeh & Co", causing it to be split across business_name and niche fields. This needs to be corrected in the source file.

2. **Incomplete Contact Data:** 31% of leads (33/106) are missing phone numbers, and 30% (32/106) are missing websites. These leads rely on directory listing source URLs only.

3. **Derived Emails Need Validation:** 36 emails were derived from website domains using the `info@domain` pattern. These are speculative and must be validated before outreach.

4. **Duplicate Detection Needed:** Several businesses appear across multiple sources (GMB, LinkedIn, Web). A deduplication pass should be run across all three source files to identify and merge duplicates.

5. **Social Media Profiles:** The `social_profiles` column in enriched_leads.csv is empty for all entries. Some source URLs point to Facebook, Instagram, and LinkedIn pages that should be extracted and catalogued.

6. **Address Standardization:** Some addresses reference "Near East Legon" (e.g., Osu, Airport Residential, Ridge). These are technically in neighboring areas but are included due to proximity to the East Legon commercial district.

---

## Files Created This Session

| File | Description |
|------|-------------|
| `GMB_Leads/Enriched_Leads/enriched_leads.csv` | 106 enriched GMB leads with derived emails, WhatsApp flags, and validation status |
| `GMB_Leads/Niches/` | 21 niche-specific CSV files (see below) |

### Niche Files Created

- `barbershop.csv` (3 leads)
- `dentist.csv` (13 leads)
- `education.csv` (7 leads)
- `event_planning.csv` (7 leads)
- `gym_and_fitness.csv` (5 leads)
- `hotel.csv` (3 leads)
- `hotel_and_restaurant.csv` (2 leads)
- `interior_design.csv` (8 leads)
- `law_firm.csv` (3 leads)
- `marketing_agency.csv` (6 leads)
- `photography.csv` (7 leads)
- `plumbing.csv` (5 leads)
- `prempeh_and_co.csv` (1 lead — data quality issue, should be merged into law_firm.csv)
- `real_estate.csv` (5 leads)
- `restaurant.csv` (13 leads)
- `restaurant_and_bakery.csv` (1 lead)
- `restaurant_and_bar.csv` (2 leads)
- `restaurant_and_cafe.csv` (2 leads)
- `salon.csv` (6 leads)
- `shopping_mall.csv` (3 leads)
- `supermarket_and_retail.csv` (4 leads)

---

## Next Steps

1. **Fix CSV formatting error** on line 54 of raw_leads.csv (quote the business name "Akufo-Addo, Prempeh & Co")
2. **Re-run enrichment** after fixing the CSV to get accurate niche counts
3. **Merge `prempeh_and_co.csv`** into `law_firm.csv` after correction
4. **Validate all derived emails** using SMTP validation (36 pending)
5. **Validate cross-referenced emails** from web leads (25 pending)
6. **Deduplicate across sources** — identify businesses appearing in GMB, LinkedIn, and Web leads
7. **Extract social media profiles** from source URLs pointing to Facebook, Instagram, LinkedIn
8. **Expand collection** to additional niches not yet covered (e.g., Auto Repair, Printing, IT Services, Pharmacies, Clinics, Fashion Boutiques, etc.)
9. **Collect GMB leads for neighboring areas** (Osu, Airport Residential, Labone, Cantonments)
