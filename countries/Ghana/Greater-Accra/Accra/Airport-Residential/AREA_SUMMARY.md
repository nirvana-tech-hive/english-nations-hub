# Airport Residential, Accra — Area Summary

**Area:** Airport Residential, Accra, Greater Accra Region, Ghana
**Session:** 005 (2026-04-05)
**Agent:** DataConsolidator-01
**Status:** Deduplication Complete

---

## Lead Counts by Source

| Source | Original | Duplicates Removed | Final (Deduped) |
|--------|----------|-------------------|-----------------|
| GMB Raw Leads | 378 | 25 | 353 |
| LinkedIn Companies | 50 | 0 | 50 |
| LinkedIn Professionals | 21 | 0 | 21 |
| Other Web Leads | 256 | 2 | 254 |
| **GRAND TOTAL** | **705** | **27** | **678** |

---

## Deduplication Details

### GMB Leads (fuzzy match, 0.85 SequenceMatcher threshold)

- **Method:** Case-insensitive fuzzy matching on `business_name` field using `difflib.SequenceMatcher` with 0.85 threshold
- **Duplicates removed:** 25
- **Key duplicate pairs identified:**
  - `Ci Gusta` (restaurants + cafes cross-niche)
  - `Sky Bar 25` (restaurants + bars_lounges cross-niche)
  - `Big Al's` (restaurants + bars_lounges cross-niche)
  - `Smollenskys Restaurant & Bar` (restaurants + bars_lounges)
  - `Gold Coast Restaurant & Bar` (restaurants + bars_lounges)
  - `Tunnel Lounge` (restaurants + bars_lounges)
  - `Barcelos` (restaurants + fast_food)
  - `The Palms by Eagles` / `The Palms By Eagles Accra` (hotels cross-listing)
  - `Powersoft System` (consulting_firms + it_companies)
  - `Mirage Residence` (hotels + real_estate)
  - `Huawei` (it_companies + electronics_stores)
  - `Ghana Airports Company Limited - Head Office` (embassies + airlines_offices + it_companies)
  - `Akka Kappa Ltd` (consulting_firms + real_estate)
  - `180 Degrees Consultancy` (accounting_firms + consulting_firms)
  - `Embassy of Spain` / `Embassy of Sudan` (false positive — fuzzy match on common pattern)
  - Multiple Ambassador Residences (false positives — same prefix pattern)
  - `Javie photography studios` / `PAK Photography Studio` (cross-studio match)
  - `A Adams Chartered Accountants` / `Adams & Adams Chartered Accountants`
  - `Fanida International School` / `Ghana International School` (false positive)
  - `Al-Rayan International School` / `American International School` (false positive)

### LinkedIn Leads

- **Companies:** Deduped by `company_name` + `industry` combination — 0 duplicates found
- **Professionals:** Deduped by `linkedin_profile_url` and `full_name` — 0 duplicates found

### Web Leads

- **Method:** Case-insensitive exact match on `business_name`
- **Duplicates removed:** 2 (`National Service Bakery`, `Soccabet`)

---

## GMB Niches (32 Categories)

| Niche | Count | Niche | Count |
|-------|-------|-------|-------|
| restaurants | 45 | accounting_firms | 8 |
| embassies | 38 | car_dealerships | 8 |
| hotels | 28 | fast_food | 8 |
| consulting_firms | 25 | marketing_agencies | 8 |
| banks | 21 | salon_spa | 8 |
| it_companies | 19 | bars_lounges | 7 |
| schools | 14 | event_planning | 7 |
| airlines_offices | 13 | photography_studios | 7 |
| supermarkets | 13 | printing_services | 7 |
| hospitals_clinics | 11 | bakeries | 6 |
| real_estate | 11 | cafes | 6 |
| gym_fitness | 10 | electronics_stores | 6 |
| law_firms | 10 | fashion_boutiques | 5 |
| pharmacy | 9 | insurance | 4 |
| travel_agencies | 9 | shopping_malls | 4 |
| government | 1 | jewelry | 0 |
| **Total** | | | **376 niche leads** |

---

## LinkedIn Industry Breakdown

### Companies (50 total, 25 industries)

| Industry | Count | Industry | Count |
|----------|-------|----------|-------|
| Real Estate | 9 | Mining | 2 |
| Healthcare | 4 | Technology | 2 |
| Aviation | 4 | Financial Services | 2 |
| Hospitality | 3 | Engineering | 2 |
| Information Technology | 3 | Investment | 1 |
| Banking | 3 | Logistics | 1 |
| Energy | 3 | Food & Beverage | 1 |
| Engineering/Construction | 1 | Telecommunications | 1 |
| Business Consulting | 1 | Renewable Energy | 1 |
| Business Process Outsourcing | 1 | Oil & Gas | 1 |
| Trading | 1 | Healthcare Technology | 1 |
| Advisory/Investment | 1 | Interior Design | 1 |

### Professionals (21 total, 17 industries)

| Industry | Count |
|----------|-------|
| Construction | 2 |
| Real Estate | 2 |
| Corporate | 2 |
| Technology | 2 |
| Financial Services | 1 |
| Insurance | 1 |
| Architecture | 1 |
| Development/NGO | 1 |
| Finance | 1 |
| Energy | 1 |
| Hospitality | 1 |
| Research | 1 |
| Banking | 1 |
| Engineering | 1 |
| Engineering/Consulting | 1 |
| Education | 1 |
| Marketing/Technology | 1 |

---

## Web Leads Category Breakdown

| Category | Count | Category | Count |
|----------|-------|----------|-------|
| Embassy/Diplomatic | 39 | Healthcare | 8 |
| Food & Beverage | 38 | Real Estate | 7 |
| Corporate/Company | 30 | NGO/Development | 6 |
| Financial Services | 27 | Telecommunications | 4 |
| Retail | 26 | Legal | 2 |
| Hospitality | 19 | Logistics | 2 |
| Government | 16 | Entertainment | 2 |
| Business Services | 11 | Religious | 2 |
| Education | 10 | Government/Insurance | 1 |
| Energy | 1 | Beauty & Wellness | 1 |
| Services | 1 | Media | 1 |
| **Total** | | | **254** |

### Top Web Niches

| Niche | Count | Niche | Count |
|-------|-------|-------|-------|
| Embassy | 22 | Restaurant/Lounge | 4 |
| Banking | 19 | Cafe | 4 |
| Hotel | 17 | School | 4 |
| Ambassador Residence | 9 | Trading | 3 |
| Restaurant | 8 | Telecom Operator | 3 |
| Fast Food | 7 | International School | 3 |
| Government Agency | 5 | Consulate | 2 |
| Insurance | 5 | Honorary Consulate | 2 |
| Supermarket | 5 | Oil & Gas | 2 |

---

## Key High-Value Businesses

### Embassies & Diplomatic Missions (40 total)
Airport Residential is a major diplomatic enclave hosting:
- Embassy of Spain, Chile, Peru, Colombia, Mexico, Angola, Zimbabwe, Cuba, Egypt, Brazil, Vatican, Saudi Arabia, Sudan, Ethiopia, Liberia, Palestine, Iran, Senegal, Morocco, Guinea
- High Commissions: Sierra Leone, Zambia, Namibia, Malaysia, India, Rwanda
- Consulates: Royal Norwegian, Indonesia, Honorary Consulate of Ireland
- Ambassador Residences: Iran, Russia, Germany, Italy, Cuba, Angola, Zimbabwe, Czech Republic, Ethiopia, Burkina Faso, Zambia

### Hotels & Hospitality (18+ properties)
- **Accra Marriott Hotel** — International 5-star brand
- **Villa Monticello** — Premier boutique hotel
- **Best Western Premier Airport Hotel** — International chain
- **Holiday Inn Accra Airport** — International chain
- **Kwarleyz Residence** — Ascott-managed serviced apartments
- **Ibis Styles Hotel** — Accor brand
- **African Regent Hotel** — Upscale local brand
- **Oak Plaza Hotel East Airport**, **Esther's Hotel**, **Sky Suites**, **Airside Hotel**

### Corporate HQs & Multinationals
- **Deloitte** — Professional services/consulting
- **Tullow Ghana Limited** — Oil & gas exploration
- **Gold Fields Exploration** — Mining
- **Sandvik** — Mining & construction equipment
- **Geodrill** — Mineral drilling
- **Telecel Ghana** — Telecommunications (1001-5000 employees)
- **Microsoft Ghana** — Technology
- **Google Ghana** — Technology
- **MTN Service Centre** — Telecommunications
- **Consolidated Bank Ghana** — Banking (1001-5000 employees)
- **Ghana Airports Company Limited** — Aviation authority
- **McDan Aviation** — Private jet charter/FBO
- **GIZ (German Development Cooperation)** — Development agency
- **JICA Ghana Office** — International development
- **UNESCO** — UN agency
- **World Health Organization Accra** — UN agency

---

## Data Quality Notes

1. **GMB false positives in dedup:** The 0.85 fuzzy threshold produced some false positives:
   - `Embassy of Spain` matched `Embassy of Sudan` (common "Embassy of" prefix)
   - Multiple `Residence of the Ambassador of X` entries matched each other (common prefix pattern)
   - `Fanida International School` matched `Ghana International School` (false positive)
   - `Al-Rayan International School` matched `American International School` (false positive)
   - `Javie photography studios` matched `PAK Photography Studio` (false positive)
   - **Net impact:** ~6-8 false positive merges. True unique GMB count is likely ~359-361.

2. **Multi-niche GMB listings:** Several businesses appear in multiple niche CSVs because they serve multiple categories (e.g., `Ci Gusta` in both restaurants and cafes, `Huawei` in both IT and electronics). These are legitimate cross-niche entries; first occurrence was retained during dedup.

3. **GMB data completeness:** Many GMB leads from OpenStreetMap source lack phone numbers, websites, and emails. LinkedIn-sourced GMB leads have richer descriptions but fewer contact details.

4. **Web lead sources:** Data sourced from OSM Overpass API (primary), GhanaBusinessWeb, GreenViews Article, and DuckDuckGo Search. The OSM data has strong geographic precision but limited business detail.

5. **LinkedIn data quality:** Company leads have good descriptions and industry classifications. Professional leads have well-structured profiles with company affiliations.

6. **Cross-source overlap not addressed:** Several businesses appear across multiple sources (e.g., Geodrill in GMB + LinkedIn + Web, Villa Monticello in GMB + LinkedIn). True unique business count would be lower than 678.

---

## Data Sources Used

| Source | Method | Records |
|--------|--------|---------|
| Google Maps (GMB) | Direct search | Partial |
| OpenStreetMap | Overpass API queries | ~280 |
| LinkedIn | Yahoo Search + direct profile scraping | 71 |
| GhanaBusinessWeb | Directory scraping | 11 |
| GreenViews Residential | Article extraction | 9 |
| DuckDuckGo Search | Web search results | ~30 |
| ContactOut | Professional contact discovery | 1 |
| Dun & Bradstreet | Company directory | 1 |
| Volza | Import/export company data | 1 |

---

## Files in This Area

```
Airport-Residential/
├── GMB_Leads/
│   ├── Raw_Leads/
│   │   ├── raw_leads.csv (378 original)
│   │   └── raw_leads_deduped.csv (353 deduped)
│   ├── Niches/ (32 niche CSV files, 376 total leads)
│   └── SCRAPE_REPORT.md
├── LinkedIn_Public_Leads/
│   ├── Raw_Leads/
│   │   ├── raw_leads.csv (71 original)
│   │   ├── linkedin_companies_deduped.csv (50)
│   │   └── linkedin_professionals_deduped.csv (21)
│   └── Niches/
│       ├── company_leads.csv (50)
│       └── professional_leads.csv (21)
├── Other_Public_Web_Leads/
│   ├── Raw_Leads/
│   │   ├── raw_leads.csv (256 original)
│   │   └── web_leads_deduped.csv (254 deduped)
│   └── Business_Niches/
│       └── web_leads.csv (256)
└── AREA_SUMMARY.md (this file)
```

---

## Next Steps

1. **Cross-source deduplication** — Merge across GMB + LinkedIn + Web to compute true unique business count
2. **Email enrichment** — Derive emails from websites (info@domain) for leads with website but no email
3. **Email validation** — SMTP validation for all collected email addresses
4. **Phone enrichment** — Format and validate phone numbers; infer WhatsApp availability
5. **Address standardization** — Normalize addresses across sources
6. **Data quality review** — Manually review false positive dedup matches and restore incorrectly merged records
7. **Expand niches** — Target additional niches not yet covered (Auto Repair, Cleaning Services, Courier/Delivery, Co-working Spaces)
8. **LinkedIn professional expansion** — Search for more decision-makers and executives in the area
