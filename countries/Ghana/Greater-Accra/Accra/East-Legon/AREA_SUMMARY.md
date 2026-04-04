# Area Summary: East Legon, Accra, Ghana

**Last Updated:** 2026-04-05
**Sessions Completed:** 3 (Session 002: 2026-04-04, Session 003: 2026-04-05)
**Agents:** LeadCollector-01, DataConsolidator-01
**Status:** Expanded & Deduplicated (Enrichment & Validation Pending)

---

## Total Leads by Source

| Source | Count | Change |
|--------|-------|--------|
| GMB Raw Leads (Master) | 193 | +87 new (from 88 collected, 1 dup removed) |
| GMB Enriched Leads | 106 | unchanged (new leads not yet enriched) |
| LinkedIn Companies | 59 | +39 new (20 mapped from old professionals + 40 new companies - 1 overlap) |
| LinkedIn Professionals | 55 | +35 new (20 old + 35 new, 0 duplicates) |
| **Total LinkedIn** | **114** | **+75 new** |
| Other Web Leads (Master) | 88 | +40 new (0 duplicates found) |
| **GRAND TOTAL** | **395** | **+202 new this session** |

### Pre-Session Totals (2026-04-04)
| Source | Count |
|--------|-------|
| GMB Raw Leads | 106 |
| LinkedIn Public Leads | 20 |
| Other Public Web Leads | 48 |
| **Previous Total** | **174** |

---

## GMB Niche Breakdown (from raw_leads_master.csv — 193 leads)

### Properly Categorized Leads (106 leads, 21 niches)

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
| Prempeh & Co (data quality issue) | 1 |
| **Subtotal** | **106** |

### Uncategorized New Leads (87 leads — address in niche field)

> **Data Quality Issue:** 87 of the 88 new GMB leads from `raw_leads_all_niches.csv` have the business address in the `niche` field instead of a proper niche category. These leads are valid but require niche re-classification. They are also captured in their respective niche CSV files under the `Niches/` directory.

---

## All 37 Niches (Niche CSV Files in GMB_Leads/Niches/)

### Session 002 Niches (21 files)
1. `barbershop.csv` — 3 leads
2. `dentist.csv` — 13 leads
3. `education.csv` — 7 leads
4. `event_planning.csv` — 7 leads
5. `gym_and_fitness.csv` — 5 leads
6. `hotel.csv` — 3 leads
7. `hotel_and_restaurant.csv` — 2 leads
8. `interior_design.csv` — 8 leads
9. `law_firm.csv` — 3 leads
10. `marketing_agency.csv` — 6 leads
11. `photography.csv` — 7 leads
12. `plumbing.csv` — 5 leads
13. `prempeh_and_co.csv` — 1 lead (data quality issue, should merge into law_firm.csv)
14. `real_estate.csv` — 5 leads
15. `restaurant.csv` — 13 leads
16. `restaurant_and_bakery.csv` — 1 lead
17. `restaurant_and_bar.csv` — 2 leads
18. `restaurant_and_cafe.csv` — 2 leads
19. `salon.csv` — 6 leads
20. `shopping_mall.csv` — 3 leads
21. `supermarket_and_retail.csv` — 4 leads

### Session 003 Niches (15 new files)
22. `bank.csv` — 6 leads
23. `car_wash.csv` — 5 leads
24. `church.csv` — 4 leads
25. `electrician.csv` — 4 leads
26. `fashion_boutique.csv` — 5 leads
27. `hardware_store.csv` — 4 leads
28. `hospital_clinic.csv` — 7 leads
29. `insurance.csv` — 5 leads
30. `laundry_dry_cleaning.csv` — 4 leads
31. `petrol_station.csv` — 5 leads
32. `pharmacy.csv` — 8 leads
33. `printing_services.csv` — 4 leads
34. `tech_it.csv` — 17 leads
35. `tech_startups.csv` — 5 leads
36. `travel_agency.csv` — 5 leads

**Total Niche Files:** 36 (note: task specified 37 but 36 actual CSV files found)

---

## LinkedIn Leads Summary

### Companies (59 unique)
- 20 companies mapped from Session 002 professional profiles (company name field)
- 40 new companies from Session 003 (company_leads_new.csv)
- 1 duplicate detected and removed (overlap between old professional company names and new company data)
- Industries covered: Real Estate, Legal Services, Fashion, Hospitality, IT, Education, Healthcare, Financial Services, Business Consulting, Retail, Food & Beverage, and more
- Employee ranges: 2-10 (small), 11-50 (medium), 51-200 (large), 201-500 (enterprise), 501-1000+

### Professionals (55 unique)
- 20 professionals from Session 002 (diverse roles across East Legon businesses)
- 35 new professionals from Session 003 (professional_leads_new.csv)
- 0 duplicates (all unique LinkedIn profile URLs)
- Roles include: Software Engineers, Business Development Managers, Entrepreneurs, Marketing Directors, Healthcare Professionals, Business Services professionals

---

## Web Leads Summary (Master)

- **88 total web-sourced leads** after deduplication (48 old + 40 new, 0 duplicates found)
- Sources: ghanabusinessweb.com, bing.com
- Categories covered: Hotel & Hospitality, Education, Real Estate, Retail, Business Services, Restaurant, Financial Services, Technology, Food & Beverage, Healthcare, Logistics, Security, Agriculture, Hair & Beauty
- Unified schema merges old (8 columns) and new (16 columns) formats

---

## Enrichment Results (Session 002 — not yet updated for new leads)

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

1. **New GMB Niche Field Malformed:** 87 of 88 new leads in `raw_leads_all_niches.csv` have the business address in the `niche` column instead of a proper niche category. These leads ARE correctly categorized in their individual niche CSV files under `GMB_Leads/Niches/` (bank.csv, tech_it.csv, pharmacy.csv, etc.), but the master CSV `raw_leads_all_niches.csv` itself has this issue.

2. **CSV Formatting Issue (Unresolved):** Line 54 of the original `raw_leads.csv` still has an unquoted comma in the business name "Akufo-Addo, Prempeh & Co", creating a phantom niche file (`prempeh_and_co.csv`).

3. **Duplicate Detection:** Case-insensitive fuzzy matching (0.90 threshold) was applied:
   - GMB: 1 duplicate found ("Fresh and Ready Cleaners" appeared in both old and new files)
   - LinkedIn: 1 company overlap detected between professional profile company names and new company data
   - Web: 0 duplicates found between old and new web leads

4. **New Leads Not Yet Enriched:** The 87 new GMB leads have not been run through the enrichment pipeline (email derivation, WhatsApp flagging, web cross-referencing). The `enriched_leads.csv` still contains only the original 106 leads.

5. **Derived Emails Need Validation:** 36 emails were derived from website domains using the `info@domain` pattern. These are speculative and must be validated before outreach.

6. **Cross-Source Overlap:** Many businesses appear across multiple sources (GMB, LinkedIn, Web). A cross-source deduplication pass should identify the same business across different data files for a true unique business count.

7. **Social Media Profiles:** The `social_profiles` column in enriched_leads.csv is empty for all entries. Source URLs pointing to Facebook, Instagram, and LinkedIn pages should be extracted.

---

## Files Created/Modified This Session (Session 003)

| File | Description |
|------|-------------|
| `GMB_Leads/Raw_Leads/raw_leads_master.csv` | **NEW** — 193 deduplicated GMB leads (merged from 106 old + 88 new - 1 dup) |
| `GMB_Leads/Raw_Leads/raw_leads_all_niches.csv` | Pre-existing — 88 new raw GMB leads |
| `GMB_Leads/Niches/*.csv` (15 new files) | Pre-existing — bank, car_wash, church, electrician, fashion_boutique, hardware_store, hospital_clinic, insurance, laundry_dry_cleaning, petrol_station, pharmacy, printing_services, tech_it, tech_startups, travel_agency |
| `LinkedIn_Public_Leads/Niches/linkedin_all_companies.csv` | **NEW** — 59 unique companies (20 mapped from old professionals + 40 new) |
| `LinkedIn_Public_Leads/Niches/linkedin_all_professionals.csv` | **NEW** — 55 unique professionals (20 old + 35 new, deduped by URL) |
| `LinkedIn_Public_Leads/Niches/company_leads_new.csv` | Pre-existing — 40 new company leads |
| `LinkedIn_Public_Leads/Niches/professional_leads_new.csv` | Pre-existing — 35 new professional leads |
| `Other_Public_Web_Leads/Business_Niches/web_leads_master.csv` | **NEW** — 88 deduplicated web leads (48 old + 40 new, unified schema) |
| `Other_Public_Web_Leads/Business_Niches/web_leads_new.csv` | Pre-existing — 40 new web leads |

---

## Next Steps

1. **Fix GMB niche field** for 87 new leads — re-map the address data in the niche column to the correct niche categories (many are already captured in individual niche CSVs)
2. **Run enrichment pipeline** on all 193 GMB master leads to update `enriched_leads.csv`
3. **Fix CSV formatting error** on line 54 of original `raw_leads.csv` (quote "Akufo-Addo, Prempeh & Co")
4. **Merge `prempeh_and_co.csv`** into `law_firm.csv` after correction
5. **Validate all derived emails** using SMTP validation (36+ pending from original, plus new leads)
6. **Cross-source deduplication** — identify businesses appearing in GMB, LinkedIn, and Web leads for a true unique business count
7. **Extract social media profiles** from source URLs
8. **Expand collection** to additional niches (Auto Repair, Cleaning Services, Courier/Delivery, etc.)
9. **Begin collection for neighboring areas** (Osu, Airport Residential, Labone, Cantonments)
