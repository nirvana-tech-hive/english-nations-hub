# GMB Lead Scraping Report: Airport Residential, Accra, Ghana

**Date Collected:** 2026-04-05  
**Area:** Airport Residential Area, Accra, Greater Accra Region, Ghana  
**Bounding Box:** Lat 5.600-5.630, Lon -0.190 to -0.150  

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **Total Leads** | **378** |
| **Niches Covered** | **32** |
| **Leads with Phone** | 39 |
| **Leads with Website** | 41 |
| **Leads with Address** | 68 |
| **Leads with Any Contact Info** | 93 |

---

## Leads by Niche

| Niche | Leads |
|-------|-------|
| restaurants | 45 |
| embassies | 38 |
| hotels | 28 |
| consulting_firms | 25 |
| banks | 21 |
| it_companies | 19 |
| schools | 14 |
| airlines_offices | 13 |
| supermarkets | 13 |
| hospitals_clinics | 11 |
| real_estate | 11 |
| gym_fitness | 10 |
| law_firms | 10 |
| pharmacy | 9 |
| travel_agencies | 9 |
| accounting_firms | 8 |
| car_dealerships | 8 |
| fast_food | 8 |
| marketing_agencies | 8 |
| salon_spa | 8 |
| bars_lounges | 7 |
| event_planning | 7 |
| photography_studios | 7 |
| printing_services | 7 |
| bakeries | 6 |
| cafes | 6 |
| electronics_stores | 6 |
| fashion_boutiques | 5 |
| insurance | 4 |
| shopping_malls | 4 |
| government | 1 |

---

## Data Sources Used

1. **OpenStreetMap/Overpass API** — Primary source for business names, addresses, phones, websites
2. **Google Maps** — Search results for business names and additional listings
3. **Nominatim API** — Supplementary geocoded business data
4. **LinkedIn** — Corporate headquarters and company identification

---

## Key Findings

### High-Concentration Niches (Premium Area)
- **Restaurants (45):** Airport Residential has a vibrant dining scene with premium restaurants like 805 Restaurant, Tunnel Lounge, La Chaumière, Gold Coast
- **Embassies/Diplomatic (38):** Confirms the area's status as a diplomatic district — embassies of Spain, Egypt, Saudi Arabia, Brazil, Angola, Zimbabwe, Cuba, Sudan, Morocco, and many more
- **Hotels (28):** Strong hospitality presence including Accra Marriott, Airside Hotel, Villa Monticello, Ibis Styles, Best Western Premier
- **Banks (21):** Major Ghanaian and international banks — Ecobank, CalBank, Absa, Stanbic, GT Bank, Société Générale, Fidelity

### Professional Services Hub
- **Consulting firms (25), IT companies (19), Law firms (10)** — Reflects the corporate HQ concentration
- **Accounting firms (8):** Including MGIO.A.K, Abstractus, Elixir Audits

### Retail & Lifestyle
- **Supermarkets (13):** Shoprite, Melcom, Koala, Marina Mall
- **Car dealerships (8):** Mercedes, Japan Motors, Silver Star Auto, Mazda, Tata Motors

---

## Issues Encountered

1. **Google Maps detail panel**: Click-through to get individual business details (phone/website) was unreliable — the detail sidebar didn't consistently open
2. **Overpass API timeouts**: The main endpoint was intermittently overloaded; had to retry queries
3. **DuckDuckGo/Yahoo CAPTCHAs**: Automated search engines blocked bot access
4. **Browser session management**: Agent-browser sessions were occasionally lost between shell recreations
5. **Google Maps locale**: Results displayed in Chinese (Traditional) which affected detail extraction

---

## Recommendations for Enrichment

1. **Phone/Email enrichment**: Use web scraping on each business website to find contact details
2. **WhatsApp numbers**: Many Ghanaian businesses use WhatsApp — scrape from websites
3. **Google Maps Places API**: If API key available, get structured data for all 378 businesses
4. **Social media**: Cross-reference with Facebook/Instagram pages for additional contact info
5. **Deduplication**: Some businesses may appear in multiple niche files (e.g., "805 Restaurants" in both restaurants and cafes)
