# Area Summary: Osu, Accra

**Area:** Osu, Accra, Greater Accra Region, Ghana
**Session:** 004 (2026-04-05)
**Agent:** DataConsolidator-01
**Status:** Data Collection & Deduplication Complete

---

## Overview

Osu is one of Accra's most vibrant commercial and entertainment districts, known for Oxford Street, Labadi Beach, and a dense concentration of hospitality businesses, restaurants, retail shops, and professional services. This area is a prime target for lead generation with high business density across multiple niches.

---

## Lead Counts Summary

| Source | Pre-Dedup | Post-Dedup | Duplicates Removed |
|--------|-----------|------------|---------------------|
| GMB Raw Leads | 247 | 244 | 3 |
| LinkedIn Companies | 50 | 49 | 1 |
| LinkedIn Professionals | 53 | 53 | 0 |
| Other Web Leads | 156 | 156 | 0 |
| **GRAND TOTAL** | **506** | **502** | **4** |

### Grand Total (Post-Dedup): 502 Leads

---

## GMB Leads Detail (244 unique)

### Deduplication Method
- Case-insensitive fuzzy matching using `difflib.SequenceMatcher` with 0.85 threshold
- Duplicates identified and removed: 3

### Duplicates Found
1. **BloomBar** — Listed in both `bar` and `nightclub` niches (kept bar entry)
2. **SHARPNET Internet Cafe Copy Centre and Photo Lab** — Listed in both `cafe` and `printing_service` niches (kept cafe entry)
3. **SilverHair Salon & Spa** — Listed in both `salon` and `spa` niches (kept salon entry)

### GMB Niche Breakdown (30 Niches)

| # | Niche | Count | Niche CSV |
|---|-------|-------|-----------|
| 1 | Restaurant | 18 | restaurant.csv |
| 2 | Hotel | 15 | hotel.csv |
| 3 | IT Company | 12 | it_company.csv |
| 4 | Bakery | 11 | bakery.csv |
| 5 | Travel Agency | 11 | travel_agency.csv |
| 6 | Bar | 10 | bar.csv |
| 7 | Church | 10 | church.csv |
| 8 | Marketing Agency | 10 | marketing_agency.csv |
| 9 | School | 10 | school.csv |
| 10 | Bank | 8 | bank.csv |
| 11 | Cafe | 8 | cafe.csv |
| 12 | Fashion Boutique | 8 | fashion_boutique.csv |
| 13 | Fast Food | 8 | fast_food.csv |
| 14 | Gym | 8 | gym.csv |
| 15 | Law Firm | 8 | law_firm.csv |
| 16 | Salon | 8 | salon.csv |
| 17 | Supermarket | 8 | supermarket.csv |
| 18 | Electronics | 7 | electronics.csv |
| 19 | Real Estate | 7 | real_estate.csv |
| 20 | Spa | 7 | spa.csv |
| 21 | Car Dealership | 6 | car_dealership.csv |
| 22 | Event Planning | 6 | event_planning.csv |
| 23 | Hospital/Clinic | 6 | hospital_clinic.csv |
| 24 | Insurance | 6 | insurance.csv |
| 25 | Photography | 6 | photography.csv |
| 26 | Accounting Firm | 5 | accounting_firm.csv |
| 27 | Art Gallery | 5 | art_gallery.csv |
| 28 | Nightclub | 5 | nightclub.csv |
| 29 | Pharmacy | 5 | pharmacy.csv |
| 30 | Printing Service | 5 | printing_service.csv |

**Total GMB niche leads across 30 CSVs: 247** (pre-dedup), **244 unique**

---

## LinkedIn Public Leads Detail (102 unique)

### Company Leads (49 unique)

Deduplicated by `company_name + industry` combination. Removed 1 duplicate:
- La Villa Boutique Hotel (appeared twice with same name + industry)

#### Industry Breakdown (Companies)

| Industry | Count |
|----------|-------|
| Technology | 9 |
| Hospitality & Tourism | 8 |
| Healthcare | 7 |
| Real Estate & Construction | 5 |
| Retail | 4 |
| General Business | 4 |
| Marketing & Media | 2 |
| Design & Innovation | 2 |
| Restaurant & Food | 2 |
| Fashion & Beauty | 2 |
| Finance & Professional Services | 1 |
| Logistics & Transport | 1 |
| NGO & Nonprofit | 1 |
| Consulting & Legal | 1 |

### Professional Leads (53 unique)

Deduplicated by `linkedin_profile_url` (or `full_name + company_name` fallback). No duplicates found.

#### Industry Breakdown (Professionals)

| Industry | Count |
|----------|-------|
| Technology | 12 |
| Healthcare | 8 |
| General Business | 6 |
| Education & Training | 6 |
| Finance & Professional Services | 4 |
| Hospitality & Tourism | 4 |
| Executive Leadership | 3 |
| Management | 3 |
| Marketing & Media | 2 |
| Government & Public Sector | 2 |
| Consulting & Legal | 2 |
| Restaurant & Food | 1 |

---

## Other Web Leads Detail (156 unique)

Deduplicated by `business_name` (case-insensitive). No duplicates found.

Sources: OpenStreetMap/Overpass API (primary), Bing Maps (supplementary)

### Category Breakdown

| Category | Count |
|----------|-------|
| Food & Dining | 54 |
| Financial Services | 17 |
| Hospitality | 17 |
| Retail | 16 |
| Nightlife | 11 |
| Healthcare | 9 |
| Auto & Fuel | 6 |
| Business Services | 5 |
| Education | 5 |
| Government | 4 |
| Beauty & Wellness | 3 |
| Telecommunications | 2 |
| IT & Technology | 2 |
| Security | 1 |
| Marketing | 1 |
| Travel | 1 |
| Government/Diplomatic | 1 |
| Government/NGO | 1 |

---

## Key Businesses Found

### Hospitality & Hotels
- Kempinski Hotel Gold Coast City Accra
- Movenpick Ambassador Hotel Accra
- Labadi Beach Hotel
- La Villa Boutique Hotel
- Holiday Inn Accra Airport by IHG
- Number One Oxford Street Hotel & Suites
- Frankie's Hotel

### Restaurants & Dining
- The Buka Restaurant
- Le Magellan Restaurant
- Rockefellas Sushi Korean Continental
- Tatale Vegan Restaurant
- La Piazza
- Noble House Restaurant

### Professional Services
- PwC Ghana, Deloitte Ghana, KPMG Ghana, EY Ghana (Big 4)
- N Nketiah Law, AB&David Law Affiliates
- Kissi Consult (Chartered Accountants)
- Strategic Communications Africa (Stratcomm)

### Retail & Shopping
- Koala Shopping Center
- Melcom Accra
- Shoprite Accra
- Marina Mall Supermarket
- The Shop Accra (lifestyle)
- Christie Brown (fashion)

### Technology
- MTN Ghana
- Andas Solutions Ltd
- Ozone Ghana
- Dopeon Digital Services
- Tech Era (social enterprise)

### Healthcare
- The Trust Hospital
- Nuffield Clinic Gh
- Sonotech Medical and Diagnostic Center
- Rabito Clinic Limited

---

## Data Quality Notes

1. **GMB Data Quality: Good** — 247 leads with high address/phone coverage. Most leads have phone numbers and many have websites. Some addresses reference areas adjacent to Osu (Labone, Cantonments, Ridge) which is expected for businesses near Osu boundaries.

2. **LinkedIn Data Quality: Mixed** — Company data has good industry classification and descriptions. Professional data includes some false-positive matches (e.g., "Katie Heitz" from Ohio State University matched due to "OSU Health" containing "Osu"). About 5-10% of professionals may not be Osu, Accra-based.

3. **Web Data Quality: Good** — OpenStreetMap data has comprehensive coverage of physical business locations. Phone numbers and websites are present for many entries. Some entries lack phone/email data.

4. **Cross-Source Overlap**: Several businesses appear across multiple sources (e.g., La Villa Boutique Hotel in GMB and LinkedIn, Kukun in GMB and LinkedIn, Top-Up Pharmacy in all three). Cross-source deduplication was not performed in this session — counts reflect per-source unique totals.

5. **Multi-Niche Businesses**: Some legitimate businesses appear in multiple GMB niches (BloomBar as bar/nightclub, SHARPNET as cafe/printing). These are cross-niche duplicates within GMB, not true data errors. The first occurrence was retained.

6. **No Email Validation Performed** — Email addresses from raw data have not been validated. This is a next step.

---

## Data Sources Used

| Source | Method | Query Patterns |
|--------|--------|----------------|
| Google Maps / Bing Maps | GMB search by niche | `niche + "Osu, Accra"` |
| LinkedIn | Company search | `site:linkedin.com/company "Osu" Accra Ghana` |
| LinkedIn | Professional search | `site:linkedin.com/in "Osu" Accra` with role/industry filters |
| OpenStreetMap | Overpass API | Spatial query within Osu bounds |
| Bing Maps | Map search | Supplementary web leads for restaurants |

---

## Files in This Area

### GMB Leads
- `GMB_Leads/Raw_Leads/raw_leads.csv` (247 leads, original)
- `GMB_Leads/Raw_Leads/raw_leads_deduped.csv` (244 leads, deduped)
- `GMB_Leads/Niches/` (30 niche CSV files)

### LinkedIn Leads
- `LinkedIn_Public_Leads/Raw_Leads/raw_leads.csv` (103 leads, combined companies + professionals)
- `LinkedIn_Public_Leads/Niches/company_leads.csv` (50 companies, original)
- `LinkedIn_Public_Leads/Niches/professional_leads.csv` (53 professionals, original)
- `LinkedIn_Public_Leads/Raw_Leads/linkedin_companies_deduped.csv` (49 companies, deduped)
- `LinkedIn_Public_Leads/Raw_Leads/linkedin_professionals_deduped.csv` (53 professionals, deduped)

### Web Leads
- `Other_Public_Web_Leads/Raw_Leads/raw_leads.csv` (156 leads, original)
- `Other_Public_Web_Leads/Business_Niches/web_leads.csv` (156 leads, categorized copy)
- `Other_Public_Web_Leads/Raw_Leads/web_leads_deduped.csv` (156 leads, deduped)

---

## Next Steps

1. **Cross-source deduplication** — Identify businesses appearing in multiple sources (GMB + LinkedIn + Web) to compute true unique business count
2. **Email validation** — Run SMTP validation on all discovered email addresses
3. **Email enrichment** — Derive missing emails from website domains using info@domain pattern
4. **LinkedIn false-positive cleanup** — Remove professionals clearly not based in Osu, Accra (e.g., Katie Heitz from OSU Health in Ohio)
5. **Web leads enrichment** — Fill in missing phone/email data for web leads using website scraping
6. **Expand niche coverage** — Add niches not yet targeted (e.g., Auto Repair, Cleaning Services, Courier/Delivery, Beauty Supply)
7. **Move to next area** — Begin collection for neighboring areas (Airport Residential, Labone, Cantonments)
