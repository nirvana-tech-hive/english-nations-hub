# Lead Collection Methods — Comprehensive Guide

**Document Version:** 1.0  
**Classification:** Operational Reference Document  
**Audience:** Autonomous Lead Collection Agents  
**Repository:** English Nations Hub  
**Last Updated:** June 2025  
**Companion Documents:** `AGENT_FRAMEWORK.md`, `DISCOVERY_QUERIES_500_PLUS.md`

---

## Table of Contents

1. [Overview](#overview)
2. [Method 1: Google My Business Collection](#method-1-google-my-business-collection)
3. [Method 2: LinkedIn Public Profile Discovery](#method-2-linkedin-public-profile-discovery)
4. [Method 3: Other Public Web Sources](#method-3-other-public-web-sources)
5. [Cross-Source Enrichment](#cross-source-enrichment)
6. [Session Planning](#session-planning)

---

## Overview

The English Nations Hub repository relies on **three primary collection ecosystems** to build its geographically organized lead intelligence database. Each method targets a fundamentally different class of publicly available data and produces lead profiles with distinct characteristics, strengths, and enrichment potential. When used together, these three methods provide maximum coverage — capturing businesses with physical premises, individual professionals, freelancers, creative workers, and organizations that maintain no presence on either Google Maps or LinkedIn.

### The Three Ecosystems at a Glance

| Method | Primary Source | Best For | Typical Yield | Key Data Points |
|--------|---------------|----------|---------------|-----------------|
| **Google My Business (GMB)** | Google Maps, Google Business Profiles | Brick-and-mortar businesses, local service providers | High per area (20–100+ leads per niche) | Address, phone, website, reviews, hours, WhatsApp |
| **LinkedIn Public Profiles** | LinkedIn (via search engine indexing) | Individual professionals, B2B contacts, executives | Medium per area (10–50+ per niche) | Name, title, company, skills, email (sometimes), profile URL |
| **Other Public Web** | Directories, portfolios, freelancer platforms, event pages, social media, government registries | Businesses without GMB, freelancers, creatives, niche professionals | Variable (5–40+ per niche) | Email, phone, website, portfolio, source URL, source type |

### Why All Three Methods Are Essential

No single collection method provides comprehensive coverage of all leads within a geographic area. Consider the following gaps that each method fills for the others:

- **A freelance graphic designer** in Accra may have no GMB listing and no LinkedIn profile, but maintains a Behance portfolio with contact details — only Method 3 captures this lead.
- **A dental clinic** in Victoria Island, Lagos, has a verified GMB listing with full contact details but the practice owner's personal email is visible only on their LinkedIn profile — Methods 1 and 2 together capture the complete picture.
- **A software startup** in Austin, Texas, has no physical office (no GMB), the founders keep LinkedIn private, but the company is listed on Clutch.co, Crunchbase, and has a website with team bios — Method 3 is the sole discovery channel.
- **A real estate agency** in Sydney, Australia, appears on Google Maps, has agent profiles on LinkedIn, and is also listed on Realestate.com.au and the local chamber of commerce directory — all three methods provide overlapping and complementary data.

**The operational principle is clear: agents should employ all three methods for every target area to achieve maximum coverage.** A lead missed by one method may be captured by another. Cross-referencing across methods also enables data enrichment — combining an address from GMB with an email from LinkedIn and a phone number from a web directory produces a far more valuable lead record than any single source alone.

### Data Profile Comparison

Each method produces leads with a characteristic data profile. Understanding these profiles helps agents set realistic expectations and prioritize enrichment efforts:

| Data Field | GMB Availability | LinkedIn Availability | Other Web Availability |
|------------|-----------------|-----------------------|----------------------|
| Business/Person Name | Very High (95%+) | Very High (95%+) | High (80%+) |
| Physical Address | Very High (90%+) | Low (10%–20%) | Medium (30%–50%) |
| Phone Number | High (80%+) | Low (5%–15%) | Medium (40%–60%) |
| Email Address | Low (15%–25%) | Low–Medium (10%–30%) | High (50%–70%) |
| Website URL | Medium–High (60%+) | Low–Medium (20%–40%) | High (70%+) |
| Social Media Links | Medium (30%–50%) | Very High (90%+) | Medium (40%–60%) |
| Professional Title/Skills | Low (10%–20%) | Very High (90%+) | Medium (40%–60%) |
| Reviews/Ratings | High (70%+) | Low (endorsements only) | Low (varies by source) |
| Geographic Precision | High (street address) | Medium (city level) | Variable |
| WhatsApp Number | Low–Medium (10%–30%) | Very Low (<5%) | Medium (15%–40%) |

---

## Method 1: Google My Business Collection

Google My Business (GMB) is the single most productive collection method for **businesses with physical locations**. Every business that has claimed or been assigned a Google Business Profile appears on Google Maps and in local search results, making Google Maps the most comprehensive public directory of local businesses in the world. For the English Nations Hub, GMB collection is the backbone of local business lead intelligence across all 15 covered countries.

### What Data Is Available

GMB listings expose a rich set of structured and unstructured data fields. The availability of each field varies by listing, but agents should attempt to capture every visible piece of information:

#### Core Listing Data

| Field | Description | Availability |
|-------|-------------|-------------|
| **Business Name** | The official trading name as displayed on the listing | Nearly universal (99%+) |
| **Primary Category** | Google's assigned business category (e.g., "Dental Clinic", "Italian Restaurant") | Nearly universal (99%+) |
| **Secondary Categories** | Additional categories the business has selected | Common (60%–70%) |
| **Full Address** | Street address, city, state/province, postal code, country | High (90%+) |
| **Phone Number** | Primary publicly listed phone number | High (80%+) |
| **Website URL** | Link to the business's website | Medium–High (60%+) |
| **Opening Hours** | Structured hours of operation, including special hours | High (85%+) |
| **Google Maps URL** | Direct link to the listing on Google Maps | Always available |
| **CID / Place ID** | Google's internal identifier for the listing (visible in the URL) | Always available |

#### User-Generated Content

| Field | Description | Availability |
|-------|-------------|-------------|
| **Customer Reviews** | Text reviews from customers, with dates and ratings | Common (50%–70% of listings have reviews) |
| **Star Rating** | Aggregate rating on a 1–5 scale | Common (50%–70%) |
| **Review Count** | Total number of reviews | Common (50%–70%) |
| **Owner Responses** | Replies from the business owner to reviews | Variable (10%–30%) |
| **Q&A Section** | Public questions and answers about the business | Variable (5%–15%) |
| **User-Uploaded Photos** | Customer and business photos | Common (60%+) |

#### Additional Discoverable Data

| Field | Description | How to Discover |
|-------|-------------|-----------------|
| **WhatsApp Link** | Direct WhatsApp chat link (increasingly common, especially in Africa, South Asia, and Latin America) | Look for "Chat" button on mobile Maps; check listing description for wa.me links |
| **Social Media Links** | Facebook, Instagram, Twitter/X profiles linked from the listing | Often embedded in the listing description or under the "Website" field as a social URL |
| **Email Address** | Contact email (rarely displayed directly on GMB, but sometimes in description or Q&A) | Check listing description text, Q&A answers from owner, and linked website |
| **Price Range** | Economic tier indicator ($ to $$$$) | Visible on many restaurant and hospitality listings |
| **Service Options** | Delivery, takeout, dine-in, online booking indicators | Visible as attribute badges on the listing |
| **Accessibility** | Wheelchair accessible, other accessibility features | Visible as attribute badges |
| **Popular Times** | Hourly busyness data | Visible on the listing (informational, not a contact data point) |

### Collection Strategies

#### Strategy 1: Direct Google Maps Search by Niche + City Area

This is the primary and most intuitive GMB collection method. Agents perform a direct search on Google Maps using structured queries combining the business type with the geographic area.

**Query format:**
```
"[business type]" in "[city area], [city]"
```

**Examples:**
```
"dentist" in "Victoria Island, Lagos"
"plumber" in "Downtown, Houston"
"marketing agency" in "CBD, Sydney"
"restaurant" in "City Centre, Manchester"
```

**Technique:**
1. Open Google Maps in a browser or use the Maps API.
2. Enter the structured query.
3. Zoom to the specific city area boundary.
4. Scroll through all results, noting businesses that fall within the target area.
5. Google Maps may return results beyond the exact area — agents must verify each listing's address falls within the target City Area folder's geographic boundaries.
6. Click into each listing to extract full details from the business profile panel.

#### Strategy 2: Google Search with Location Modifiers

Standard Google web search can surface GMB listings within search results. The local pack (the map + three listings shown at the top of search results for local queries) provides quick access to high-ranking businesses.

**Query format:**
```
"[business type]" "[city area]" "[city]" near me
"[business type]" in "[city area]" "[city]"
"best [business type]" "[city area]"
"[business type]" "[city]" "[state]" open now
```

**Examples:**
```
"best dentist" "Victoria Island" "Lagos"
"plumber" "Downtown Houston" near me
"restaurant" "City Centre Manchester" reviews
"car repair" "Austin Texas" phone number
```

**Technique:**
1. Execute the query on Google web search.
2. Identify the local pack results (map + listings panel).
3. Click "More businesses" on the local pack to expand to Google Maps.
4. Note any businesses that appear in organic search results but not in the local pack — these may have web listings without GMB profiles, which should be collected under Method 3.

#### Strategy 3: Google Maps API-Based Extraction

For agents with access to the Google Places API or Google Maps Platform, programmatic extraction offers significantly higher throughput than manual browsing.

**API endpoint approach:**
1. Use the **Places API (New)** with a text search specifying the niche and location.
2. Set `locationBias` to a circular or rectangular area matching the target City Area's boundaries.
3. Paginate through results using `nextPageToken`.
4. For each place ID returned, call the **Place Details** endpoint to retrieve full listing information.

**Data fields to request:**
```json
{
  "fields": [
    "displayName", "formattedAddress", "internationalPhoneNumber",
    "websiteUri", "regularOpeningHours", "rating", "userRatingCount",
    "types", "businessStatus", "editorialSummary", "photos"
  ]
}
```

**Rate limiting considerations:**
- Google Places API has a per-day quota depending on the billing plan.
- Free tier: limited requests; paid tier scales up.
- Agents should batch requests efficiently and implement error handling for quota exhaustion.
- Stagger requests to avoid rate limiting (1 request per second is a safe default).

#### Strategy 4: Category Browsing Within Google Maps

Google Maps organizes businesses into hierarchical categories. Browsing by category within a geographic area can reveal businesses that keyword searches might miss.

**Technique:**
1. Navigate to the target city area in Google Maps.
2. Use the category filter buttons (visible below the search bar on mobile, or in the left panel on desktop).
3. Common browsable categories include: Restaurants, Cafes, Hotels, Gas Stations, ATMs, Pharmacies, Hospitals, Grocery Stores, Shopping Malls, Gyms, Parks, Schools, and more.
4. Each category can be further refined with subcategories (e.g., Restaurants → Italian, Chinese, Fast Food).
5. Scroll through all results in the category view, filtering by the target area.

#### Strategy 5: Review-Based Discovery

Business reviews on GMB often reference related businesses, competitors, or complementary service providers. Mining reviews can uncover leads that direct searches miss.

**Technique:**
1. Find a well-known business in the target area and niche.
2. Read through customer reviews.
3. Look for review text mentioning other businesses ("I also tried [Business Name] down the street...", "After [Business A] closed, I found [Business B]...").
4. Check the reviewer's profile — frequent reviewers in an area often review multiple local businesses, effectively creating a chain of discoverable leads.
5. Owner responses sometimes reference partner businesses or related services.

### Step-by-Step Collection Process

The following 10-step workflow provides a systematic, repeatable process for GMB lead collection. Agents should follow this workflow for each target City Area and niche combination.

#### Step 1: Define the Target Scope

- Identify the exact City Area folder being populated (e.g., `countries/Nigeria/Lagos/Lagos-Island/Victoria-Island/`).
- Select the target business niche (e.g., "Dental Clinics").
- Determine the geographic boundaries of the City Area (refer to the repository's geographic hierarchy and any supplementary boundary data).
- Set a collection goal (e.g., "Collect all dental clinics within Victoria Island").

#### Step 2: Construct the Search Query

- Build a primary search query: `"dental clinic" in "Victoria Island, Lagos"`.
- Prepare 2–3 alternative queries to ensure comprehensive coverage:
  - `"dentist" in "Victoria Island, Lagos"`
  - `"dental care" in "Lagos Island"`
  - `"orthodontist" in "Victoria Island"`
- Record all queries used in the `Search_Operators_Used/` log for reproducibility.

#### Step 3: Execute the Primary Search on Google Maps

- Navigate to Google Maps (maps.google.com).
- Enter the primary query.
- Zoom to the target area boundaries.
- Note the total number of results returned.

#### Step 4: Systematically Extract All Results

- Scroll through every listing result on the map.
- For each listing, extract the core data fields (Business Name, Category, Address, Phone, Website, Rating, Review Count).
- Verify that the listing's address falls within the target City Area boundaries.
- If the address is in a different area, note it for collection under the correct area later (do not discard).
- Record the Google Maps URL for each listing.

#### Step 5: Click Into Each Listing for Detailed Extraction

- Open each listing's full profile panel.
- Extract additional data: opening hours, secondary categories, social media links, WhatsApp presence.
- Read the listing description for embedded contact information.
- Check for a WhatsApp "Chat" button (strongly indicative of WhatsApp availability).
- Note the Google Maps CID (from the URL: `google.com/maps/?cid=XXXXXXXXX`).

#### Step 6: Check the Q&A Section for Hidden Contact Data

- Open the Questions & Answers section of each listing.
- Look for owner responses that include email addresses or alternative phone numbers.
- Look for customer questions about booking, pricing, or contact methods that elicited informative responses.
- Record any additional contact details discovered.

#### Step 7: Identify WhatsApp-Enabled Businesses

- Businesses with WhatsApp contact options display a "Chat" button on their Google Maps listing (visible in the mobile app and sometimes on desktop).
- Some listings include wa.me links or WhatsApp numbers in their description text.
- If a listing has a phone number, test whether it is a WhatsApp number by constructing the URL: `https://wa.me/{phone_number_in_international_format}` — note that agents should record this as a potential WhatsApp contact but should verify through actual message delivery testing during enrichment.
- Record WhatsApp availability as: "Yes (button visible)", "Yes (in description)", "Possible (phone number may be WhatsApp)", or "No / Not Available".

#### Step 8: Extract and Record Website URLs

- Every listing that has a website link should be recorded.
- The website URL is the primary enrichment vector — it enables discovery of email addresses, additional phone numbers, social media profiles, team member information, and service details.
- Record the website URL exactly as it appears on the listing (preserving http/https and www prefixes).
- Flag listings with websites for enrichment (Step 10).

#### Step 9: Store Raw Leads

- Transfer all extracted data into the `GMB_Leads/Raw_Leads/raw_leads.csv` file.
- Follow the CSV format specified in `AGENT_FRAMEWORK.md` Section 5.
- Include all required fields: Business Name, Business Niche, Address, City Area, Phone Number, WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL, Date Collected.
- Use the current date (YYYY-MM-DD) for the Date Collected field.
- Do not leave any required field blank — use "Not Available" or "Not Listed" for missing values.

#### Step 10: Perform Selective Enrichment

- Prioritize enrichment for leads with the highest potential value:
  - **Priority 1:** Leads with websites (highest enrichment potential).
  - **Priority 2:** Leads with high ratings (4.0+) and significant review counts — indicate active, established businesses.
  - **Priority 3:** Leads with WhatsApp indicators — direct messaging is a high-value contact channel.
  - **Priority 4:** Leads with social media links — often yield additional contact information.
- For each prioritized lead, visit the linked website and extract:
  - Email addresses (from contact pages, footers, headers, and "About" pages).
  - Additional phone numbers or WhatsApp numbers.
  - Extended social media profiles.
  - Team member names and roles (useful for personalized outreach).
- Store enriched data in `GMB_Leads/Enriched_Leads/enriched_leads.csv`.
- Validate discovered email addresses using the protocol described in `AGENT_FRAMEWORK.md` Section 10.

### Data Quality Assurance

Maintaining high data quality is essential for the repository's credibility and usability. Every GMB lead should pass through the following quality checks:

#### Operational Status Verification

- **Check for "Permanently Closed" labels:** Google Maps displays a "Permanently closed" tag on defunct business listings. These leads should still be collected (per the data preservation principle) but should be flagged with a status note.
- **Check for "Temporarily Closed" labels:** These businesses may resume operations — mark as "Temporarily Closed" and retain.
- **Verify recent activity:** Listings with reviews from the current or previous year are likely still operational. Listings with no reviews in 3+ years may be dormant but should still be recorded.
- **Check the website:** If a website is listed, a quick visit confirms whether the business is still active.

#### Duplicate Detection

- **Within GMB results:** The same business may appear under slightly different names or at slightly different addresses (e.g., "Joe's Plumbing" vs. "Joe's Plumbing & Heating"). Check phone numbers and addresses to confirm or rule out duplicates.
- **Cross-method duplicates:** A business found via GMB may also appear in LinkedIn or Other Web results. Follow the duplicate handling protocol in `AGENT_FRAMEWORK.md` Section 9.
- **Multiple locations:** Chain businesses (restaurants, banks, pharmacies) often have multiple GMB listings. Each location is a separate lead, but they should be linked with a note indicating they are part of the same chain.

#### Geographic Accuracy Confirmation

- Verify that each listing's address falls within the target City Area's boundaries.
- Some listings may use colloquial or outdated area names that don't match the repository's folder structure. Use judgment to map the address to the most appropriate City Area.
- If an address cannot be confidently placed in a specific area, use the `City_General/` fallback folder.

#### Data Completeness Scoring

For quality tracking purposes, agents should calculate a **data completeness score** for each collected lead:

| Field Present | Points |
|---------------|--------|
| Business Name | 10 |
| Address | 10 |
| Phone Number | 10 |
| Website URL | 10 |
| Email Address | 15 |
| WhatsApp | 10 |
| Social Media Links | 10 |
| Rating/Reviews | 10 |
| Opening Hours | 5 |
| Google Maps URL | 10 |
| **Maximum Score** | **100** |

**Scoring interpretation:**
- **90–100:** Fully enriched lead — high outreach readiness.
- **70–89:** Well-populated lead — may need minor enrichment.
- **50–69:** Partial lead — enrichment recommended.
- **30–49:** Basic lead — significant enrichment opportunity.
- **Below 30:** Minimal lead — name and address only, enrichment essential.

Agents should track average completeness scores across their collection sessions and use this metric to identify niches or areas that need more thorough enrichment.

### Expected Yield Per City Area

Yield estimates vary significantly by niche, geographic area, and country. The following table provides baseline expectations for a typical collection session:

| Niche Category | Estimated Leads per City Area | Time Estimate (per niche) | Notes |
|---------------|-------------------------------|---------------------------|-------|
| Restaurants | 30–100+ | 20–40 minutes | Extremely dense category; subdivide by cuisine type |
| Dentists / Dental Clinics | 10–40 | 15–25 minutes | Concentrated in commercial areas |
| Plumbers / Electricians | 15–50 | 15–30 minutes | Service-area businesses may have addresses outside target area |
| Real Estate Agencies | 5–25 | 10–20 minutes | Often concentrated in business districts |
| Marketing / Digital Agencies | 5–30 | 15–25 minutes | Higher yield in metropolitan city areas |
| Hotels / Lodging | 5–40 | 15–25 minutes | Highly variable by tourism activity |
| Schools / Educational Institutions | 5–30 | 15–20 minutes | Fairly stable inventory |
| Law Firms | 10–40 | 15–25 minutes | Concentrated in commercial and government districts |
| Hair Salons / Barbershops | 20–80+ | 20–35 minutes | Very high density in residential and commercial areas |
| Gyms / Fitness Centers | 5–25 | 10–20 minutes | Concentrated in commercial strips |

**Note:** These estimates assume a metropolitan city area (not a rural area). Rural areas may yield 30–70% fewer leads per niche. Capital cities and major commercial districts (Victoria Island, Sandton, Manhattan, City of London) tend to yield at the higher end of these ranges.

---

## Method 2: LinkedIn Public Profile Discovery

LinkedIn is the world's largest professional network, with over 900 million members across 200+ countries. While much of LinkedIn's data is behind authentication walls, a significant volume of **publicly indexable profile data** is accessible through search engines — and it is this publicly visible data that Method 2 targets. This method is essential for discovering **individual professionals, executives, decision-makers, and skilled workers** who may not appear in any business directory.

### What Data Is Available

LinkedIn profiles that are visible to search engines (i.e., not restricted to "Connections Only" or fully private) expose the following data fields:

#### Core Profile Data

| Field | Description | Public Availability |
|-------|-------------|-------------------|
| **Full Name** | First and last name as displayed on the profile | Very High (85%–95%) |
| **Professional Headline** | The tagline below the name (e.g., "Senior Software Engineer at Google \| Python \| ML") | Very High (85%–95%) |
| **Current Company** | Name of the user's current employer | High (70%–85%) |
| **Current Title** | Job title at current company | High (70%–85%) |
| **Location** | City/area and country as set by the user | High (75%–90%) |
| **Profile URL** | Direct URL to the LinkedIn profile (linkedin.com/in/username) | Always available (if indexed) |
| **Profile Photo** | May appear in search results | Variable |

#### Skills and Endorsements

| Field | Description | Public Availability |
|-------|-------------|-------------------|
| **Top Skills** | Skills listed on the profile with endorsement counts | Medium (40%–60% of public profiles) |
| **Skill Endorsements** | Number of endorsements per skill | Medium (40%–60%) |
| **Certifications** | Professional certifications listed | Low–Medium (20%–40%) |

#### Contact Information

| Field | Description | Public Availability |
|-------|-------------|-------------------|
| **Email Address** | Personal or work email displayed on the profile | Low (5%–15% of profiles — many users keep this hidden) |
| **Website** | Personal or company website link | Low–Medium (15%–30%) |
| **Twitter/X Handle** | Linked Twitter account | Low (10%–20%) |
| **Phone Number** | Rarely displayed publicly | Very Low (<5%) |

#### Experience and Background

| Field | Description | Public Availability |
|-------|-------------|-------------------|
| **Current Position** | Job title, company, and dates | High (70%–85%) |
| **Past Positions** | Previous employment history | Medium (50%–70%) |
| **Education** | University/college and degree | Medium (50%–70%) |
| **Summary / About** | The "About" section with professional bio | Low–Medium (30%–50%) |

### Collection Strategies

#### Strategy 1: Google Search Operators Targeting LinkedIn

This is the primary discovery method for LinkedIn leads. Google indexes a large volume of LinkedIn profile data, and targeted search operators enable precise discovery of professionals by niche, location, and title.

**Core operator pattern:**
```
site:linkedin.com/in "[keyword]" "[location]"
```

**Advanced operator patterns:**
```
site:linkedin.com/in "[profession]" "[city]" "[country]"
site:linkedin.com/in "[title]" "[city]" -intitle:profiles
site:linkedin.com/in "[skill]" "[city]" "open to work"
site:linkedin.com/in "[niche]" "[city]" "founder" OR "ceo" OR "owner"
```

**Key principles:**
- Always include `site:linkedin.com/in` to restrict results to individual profiles (not company pages or job listings).
- Use `"[city]"` in quotes for precise geographic targeting.
- Combine niche keywords with professional titles and skill terms.
- Use `-intitle:profiles` to filter out LinkedIn directory pages that list multiple profiles but don't link to individual ones.
- Add `"open to work"` or `"available"` to find professionals actively seeking opportunities.

#### Strategy 2: Professional Title + Location Searches

Targeting specific job titles combined with location produces highly relevant results for B2B outreach.

**Examples:**
```
site:linkedin.com/in "marketing manager" "Accra"
site:linkedin.com/in "software engineer" "Lagos"
site:linkedin.com/in "real estate agent" "Sydney"
site:linkedin.com/in "dentist" "Johannesburg"
site:linkedin.com/in "graphic designer" "Austin"
site:linkedin.com/in "financial advisor" "Toronto"
```

**Tips for maximum results:**
- Include title variations: `"CEO" OR "Chief Executive" OR "Founder" OR "Owner"`
- Include seniority modifiers: `"senior" OR "lead" OR "head" OR "principal"`
- Include role variants: `"developer" OR "engineer" OR "programmer"`
- Search at city level, state level, and country level to capture leads with imprecise location settings.

#### Strategy 3: Company Page Discovery

Discovering LinkedIn company pages provides access to employee lists, company size, industry classification, and — critically — links to individual employee profiles.

**Search patterns:**
```
site:linkedin.com/company "[company name]" "[city]"
site:linkedin.com/company "[niche]" "[city]" "employees"
site:linkedin.com/company "[niche]" "[city]" "services"
```

**Technique:**
1. Discover company pages matching the target niche and area.
2. From each company page, identify key personnel (visible in search snippet or public page data).
3. Construct individual profile search queries based on discovered employee names.
4. Cross-reference discovered companies with GMB listings for data enrichment.

#### Strategy 4: "People Also Viewed" Chain Discovery

LinkedIn displays a "People also viewed" section on public profiles. While this section may not always be visible in search results, it can be exploited when browsing profiles directly.

**Technique:**
1. Start with a known LinkedIn profile in the target niche and location.
2. View the profile page (if publicly accessible).
3. Check the "People also viewed" section for related profiles in the same area and profession.
4. Follow the chain to discover additional profiles iteratively.
5. Record each discovered profile URL.

**Note:** This method requires direct profile access and may be limited by LinkedIn's visibility settings. It is most effective when used as a supplementary discovery channel alongside search operator-based methods.

#### Strategy 5: LinkedIn Public Directory Browsing

LinkedIn maintains public directory pages that list profiles by name, company, or school. These pages can be surfaced through search engines.

**Search patterns:**
```
site:linkedin.com/directory "[company name]"
site:linkedin.com/directory "[university name]" "[city]"
site:linkedin.com/pub "[first name]" "[last name]" "[city]"
```

**Note:** LinkedIn's public directory structure has changed over time and access may be restricted. Agents should use this as a supplementary strategy.

### Search Operator Templates

The following 20+ ready-to-use search operator templates are organized by discovery category. Replace `{niche}`, `{city}`, `{state}`, and `{country}` placeholders with actual values.

#### By Profession (8 templates)

```
site:linkedin.com/in "{niche}" "{city}"
site:linkedin.com/in "{niche}" "{city}" "{state}"
site:linkedin.com/in "{niche}" "{city}" "experience"
site:linkedin.com/in "{niche}" "{city}" "skills"
site:linkedin.com/in "{niche}" "{city}" "certified" OR "certification"
site:linkedin.com/in "{niche}" "{city}" "freelance" OR "self-employed"
site:linkedin.com/in "{niche}" "{city}" "available" OR "open to work"
site:linkedin.com/in "{niche}" "{city}" "years experience"
```

#### By Title / Seniority (6 templates)

```
site:linkedin.com/in "senior {niche}" "{city}"
site:linkedin.com/in "lead {niche}" "{city}"
site:linkedin.com/in "head of {niche}" "{city}"
site:linkedin.com/in "{niche} manager" "{city}"
site:linkedin.com/in "{niche} director" "{city}"
site:linkedin.com/in "chief {niche}" OR "vp {niche}" "{city}"
```

#### By Company Type (4 templates)

```
site:linkedin.com/in "{niche}" "{city}" "startup"
site:linkedin.com/in "{niche}" "{city}" "agency" OR "firm"
site:linkedin.com/in "{niche}" "{city}" "freelance" OR "independent"
site:linkedin.com/in "{niche}" "{city}" "contractor" OR "consultant"
```

#### By Contact Availability (4 templates)

```
site:linkedin.com/in "{niche}" "{city}" "@" OR "email"
site:linkedin.com/in "{niche}" "{city}" "@gmail.com" OR "@yahoo.com" OR "@outlook.com"
site:linkedin.com/in "{niche}" "{city}" "contact me" OR "reach me"
site:linkedin.com/in "{niche}" "{city}" "website" OR "portfolio"
```

#### By Location Specificity (4 templates)

```
site:linkedin.com/in "{niche}" "{city}, {state}"
site:linkedin.com/in "{niche}" "{city}" "{country}"
site:linkedin.com/in "{niche}" "greater {city}" OR "{city} area"
site:linkedin.com/in "{niche}" "{state}" -"{city}" (for state-level leads)
```

### Ethical Considerations

LinkedIn data collection must adhere to strict ethical guidelines. The English Nations Hub's lead collection is limited to **publicly visible, search-engine-indexable data only**. The following rules are non-negotiable:

1. **Only collect publicly visible data.** If a profile requires authentication to view, its data must not be collected. Search engine results (Google snippets) represent the boundary of what is considered publicly visible.

2. **Respect LinkedIn's Terms of Service.** Automated scraping of LinkedIn pages using bots, scrapers, or tools that bypass rate limits or authentication is prohibited. All discovery must occur through standard search engine queries (Google, Bing, etc.).

3. **No credential sharing or login-based access.** Agents must never use LinkedIn usernames, passwords, session cookies, or authentication tokens to access restricted profile data. Collection is strictly limited to what is available without logging in.

4. **No personal account creation for scraping.** Agents should not create LinkedIn accounts for the purpose of accessing additional profile data beyond what is publicly indexable.

5. **Data minimization.** Only collect data that is relevant to lead intelligence purposes. Do not collect personal details such as profile photos, connection lists, or activity feeds that have no relevance to business outreach.

6. **Source traceability.** Every LinkedIn lead must record the source search query and the profile URL. This enables auditing and ensures compliance.

7. **Honor opt-outs.** If a profile's public visibility changes after collection (e.g., the user sets their profile to private), the existing data may be retained but agents should note the profile's changed status.

### Expected Yield Per City Area

LinkedIn yield varies significantly by profession, city size, and country. The following table provides baseline expectations:

| Profession Category | Estimated Profiles per City Area | Notes |
|--------------------|----------------------------------|-------|
| Software Developers / Engineers | 20–80+ | Very high LinkedIn adoption in tech |
| Marketing Professionals | 15–50+ | High adoption, especially in digital marketing |
| Real Estate Agents | 10–40 | Moderate LinkedIn adoption; varies by market |
| Financial Advisors / Accountants | 10–30 | Moderate adoption; higher in corporate finance |
| Designers (Graphic, UI/UX) | 15–60+ | Good LinkedIn presence; supplemented by portfolio platforms |
| Lawyers / Attorneys | 5–25 | Moderate adoption; varies significantly by country |
| Healthcare Professionals | 5–20 | Lower LinkedIn adoption for clinical roles |
| Entrepreneurs / Founders | 10–40 | Higher LinkedIn adoption among startup founders |
| HR / Recruitment Professionals | 10–30 | High adoption — LinkedIn is a primary professional tool for this group |
| Consultants | 10–30 | High adoption; consultants actively maintain LinkedIn presence |

**Country-level considerations:**
- **United States, United Kingdom, Canada, Australia:** Highest LinkedIn penetration — expect yields at the upper end of ranges.
- **Nigeria, Ghana, South Africa:** Growing LinkedIn adoption — yields may be lower but are increasing rapidly, especially among tech and business professionals.
- **Jamaica, Trinidad and Tobago, Barbados, Bahamas, Belize, Guyana:** Lower overall LinkedIn penetration — yields will be at the lower end of ranges.

---

## Method 3: Other Public Web Sources

Method 3 is the most diverse and expansive collection channel. It encompasses **every publicly accessible web source** beyond Google Maps and LinkedIn. This category captures leads that neither GMB nor LinkedIn would reveal — including businesses without physical locations, freelancers on specialized platforms, creative professionals on portfolio sites, industry association members, guest authors, event speakers, and more. The breadth of this category is both its greatest strength and its greatest challenge: the number of potential sources is enormous, requiring agents to be systematic and strategic about which sources to prioritize.

### Source Categories

The following 10 source categories represent the highest-value targets for Method 3 collection. Each category has a distinct data profile, collection approach, and yield potential.

#### 1. Business Websites (Contact Pages)

**What it is:** Direct business websites with contact pages, "About Us" pages, and "Our Team" pages.

**Data typically available:** Email addresses (info@, contact@, personal emails), phone numbers, WhatsApp numbers, physical address, social media links, team member names and roles, business description.

**How to discover:**
```
"{niche}" "{city}" inurl:contact
"{niche}" "{city}" inurl:about
"{niche}" "{city}" "contact us" OR "get in touch"
"{niche}" "{city}" "our team" OR "meet the team"
```

**Extraction strategy:** Once a business website is discovered, navigate to the contact page, footer, "About" page, and any team/staff directory pages. Extract all email addresses, phone numbers, and social media links. Check for WhatsApp floating buttons or "Chat with us" widgets.

**Geographic verification:** Confirm the business's stated location (on the contact page or in the footer) matches the target City Area. Look for local phone numbers, local addresses, or city name mentions in the website copy.

#### 2. Professional Directories (Yelp, Yellow Pages, etc.)

**What it is:** Online business directories that aggregate listings from multiple sources, typically with user reviews and contact information.

**Major directories by region:**

| Region | Primary Directories |
|--------|-------------------|
| USA | Yelp, Yellow Pages (YP.com), BBB.org, Angi, HomeAdvisor, Thumbtack |
| UK | Yell.com, Trustpilot, FreeIndex, Scoot |
| Canada | Yellow Pages Canada, BBB Canada, Homestars |
| Australia | TrueLocal, Yellow Pages Australia, ProductReview |
| Nigeria | Vconnect, Nigeria Yellow Pages, BusinessList.com.ng |
| Ghana | Ghana Yellow Pages, Ghanaweb Business Directory |
| South Africa | Yellow Pages SA, Brabys, Cylex |

**Data typically available:** Business name, address, phone number, website URL, email (sometimes), reviews, ratings, category, operating hours.

**Collection strategy:** Use site-specific search operators to mine each directory:
```
site:yelp.com "{niche}" "{city}"
site:yellowpages.com "{niche}" "{city}"
site:vconnect.com "{niche}" "{city}"
```

#### 3. Portfolio Platforms (Behance, Dribbble)

**What it is:** Creative portfolio platforms where designers, photographers, illustrators, and other creatives showcase their work.

**Major platforms:**
- **Behance** (behance.net) — Adobe's platform for designers, illustrators, photographers.
- **Dribbble** (dribbble.com) — Designer portfolios, especially UI/UX and graphic design.
- **DeviantArt** (deviantart.com) — Broad creative community.
- **Cargo Collective** (cargo.site) — Portfolio builder platform.
- **Adobe Portfolio** (myportfolio.com) — Adobe's portfolio platform.

**Data typically available:** Name, discipline/specialty, email (often in bio), personal website, location (sometimes), social media links, work samples.

**Search operators:**
```
site:behance.net "{profession}" "{city}"
site:dribbble.com "{profession}" "{city}" "@" OR "email"
site:behance.net "{city}" "hire me" OR "available for work"
```

#### 4. Freelancer Platforms (Upwork, Fiverr)

**What it is:** Online freelance marketplaces where professionals offer services. Public profile pages often contain portfolio links, contact information, and skill descriptions.

**Major platforms:**
- **Upwork** (upwork.com) — General freelance marketplace.
- **Fiverr** (fiverr.com) — Gig-based freelance marketplace.
- **Toptal** (toptal.com) — Premium freelance network (screened professionals).
- **PeoplePerHour** (peopleperhour.com) — UK-based freelance platform.
- **Freelancer.com** (freelancer.com) — Global freelance marketplace.
- **99designs** (99designs.com) — Design-specific freelance platform.

**Data typically available:** Professional name, skill category, hourly rate or gig price, portfolio link, rating/review score, location (city/country), response time, languages spoken.

**Search operators:**
```
site:upwork.com "{niche}" "{city}"
site:fiverr.com "{niche}" "{country}"
site:toptal.com "{niche}" "{country}"
```

**Note:** Many freelancer platforms restrict direct email exchange to prevent bypassing platform fees. However, email addresses sometimes appear in portfolio links, gig images, or profile descriptions.

#### 5. Event / Conference Pages

**What it is:** Conference websites, event speaker directories, workshop facilitator pages, and trade show exhibitor lists.

**Data typically available:** Speaker name, professional title, company, bio, headshot, email (for speaker inquiries), social media links, website.

**Search operators:**
```
"{niche}" conference "{city}" "speaker" "email"
"{niche}" "summit" "{city}" "speakers"
"{niche}" "{city}" "workshop" "facilitator" "contact"
"{niche}" "{city}" "exhibitor list" OR "sponsor list"
```

**Extraction strategy:** Event pages often publish speaker bios with contact details for media inquiries. These contacts are high-value leads — speakers at industry events are typically established professionals or thought leaders. Collect both the speaker information and any linked social or web profiles.

#### 6. GitHub (for Tech Professionals)

**What it is:** The world's largest code hosting platform, with 100+ million developers. GitHub profiles and repository README files often contain contact information.

**Data typically available:** Developer name, username, location (city/country), email (in profile or README), website/blog URL, organization membership, repository portfolio, programming languages used.

**Search operators:**
```
site:github.com "{city}" "developer" OR "engineer"
site:github.com "{city}" "email" OR "@"
site:github.com "{niche}" "{country}" "hire me" OR "available"
```

**Extraction strategy:** GitHub profiles have a standardized structure. Check the profile README (if present) for contact details, personal website links, and availability status. Check pinned repositories for portfolio projects. Note: GitHub users set their own location, which may be imprecise — verify with other data points.

#### 7. Industry Association Member Directories

**What it is:** Professional associations, trade bodies, and industry groups often maintain publicly accessible member directories on their websites.

**Examples:**
- Bar associations (lawyers)
- Medical boards and dental associations
- Chambers of commerce
- Real estate boards
- Engineering councils
- Architectural institutes
- Marketing associations

**Data typically available:** Member name, company, specialization, phone number, email (often), website, certification status, membership level.

**Search operators:**
```
"{niche}" association "{city}" "member directory"
"{niche}" "{city}" "chamber of commerce" "members"
"{niche}" "{state}" "board" OR "association" "directory"
"{niche}" "{city}" "member list" OR "find a {niche}"
```

#### 8. Local Chamber of Commerce Listings

**What it is:** Chambers of commerce maintain online member directories that list local businesses. These directories are publicly accessible and contain structured business information.

**Data typically available:** Business name, contact person, address, phone, email, website, business category, membership tier, years in business.

**Search operators:**
```
site:chamberofcommerce.com "{niche}" "{city}"
"{city}" "chamber of commerce" "{niche}" directory
"{city}" "chamber" "member directory" "{niche}"
```

#### 9. Blog Author Bio Pages

**What it is:** Guest blog posts, industry blog author bios, and contributor pages frequently contain detailed contact and professional information.

**Data typically available:** Author name, professional title, company, email (sometimes), website, social media links, LinkedIn profile, brief professional bio.

**Search operators:**
```
"{niche}" "{city}" "guest post" OR "guest author" OR "contributor"
"{niche}" "{city}" "about the author" OR "author bio"
"{niche}" "{city}" "written by" "email" OR "contact"
"{niche}" blog "{city}" "author" "bio"
```

#### 10. Guest Post Author Pages

**What it is:** Similar to blog author pages but focused on guest contribution networks. Authors who contribute to multiple industry publications often leave detailed bios with contact information.

**Data typically available:** Author name, title, company, headshot, bio paragraph, email, social links, personal website.

**Search operators:**
```
"guest post" "{niche}" "{city}" "bio" OR "author"
"contributing writer" "{niche}" "{city}" "contact"
"columnist" "{niche}" "{city}" "email"
```

### Collection Strategy Per Source

Each source type requires a tailored collection approach. The following framework provides source-specific guidance:

#### For Business Websites

1. **Discover** business websites through Google search operators targeting contact pages.
2. **Visit** the website and immediately check the footer for email, phone, and social links.
3. **Navigate** to the Contact page for form-based contact info and direct contact details.
4. **Navigate** to the About page for team member information and business background.
5. **Navigate** to any Team/Staff page for individual professional profiles.
6. **Check** for floating WhatsApp or live chat widgets.
7. **Verify** the business location by checking the address on the contact page.
8. **Record** the exact source URL (the page where the lead was discovered).
9. **Cross-reference** the discovered business against GMB data (if available) for enrichment.

#### For Professional Directories

1. **Target** 2–3 primary directories relevant to the target country.
2. **Search** each directory for the target niche + city area.
3. **Extract** all visible listing data (name, phone, address, website, email, rating).
4. **Follow** website links to business websites for additional contact details.
5. **Record** the directory listing URL as the primary source URL.
6. **Note** the directory name in the "Source Type" field.

#### For Portfolio Platforms

1. **Search** Behance, Dribbble, and other portfolio sites for the target profession + location.
2. **Extract** the professional's name, discipline, bio, and any listed contact info.
3. **Follow** external website links for complete contact details.
4. **Verify** geographic relevance — many portfolio users list only their country, not their city.
5. **Record** the portfolio profile URL as the source.

#### For Freelancer Platforms

1. **Search** Upwork, Fiverr, and other platforms for the target service + location.
2. **Extract** the freelancer's display name, service category, and rating.
3. **Check** for portfolio links or personal website URLs in the profile.
4. **Note** that direct email exchange may be restricted — record whatever is publicly available.
5. **Use the freelancer's name and listed skills** to search for additional contact info on the open web (cross-enrichment).

#### For Event / Conference Pages

1. **Search** for industry events, conferences, and workshops in the target city.
2. **Navigate** to the speaker directory or agenda page.
3. **Extract** speaker names, titles, companies, and bios.
4. **Follow** speaker social media links and website URLs for direct contact information.
5. **Record** the event page URL as the source.

### Advanced Techniques

#### Document Harvesting (PDF, DOCX, XLSX)

Publicly hosted documents are a goldmine for lead data. Businesses and organizations frequently publish member lists, vendor directories, exhibitor lists, brochures, and annual reports as downloadable documents.

**Search operators for document discovery:**
```
"{niche}" "{city}" filetype:pdf
"{niche}" "{city}" "member list" filetype:xlsx
"{niche}" "{city}" "directory" filetype:pdf
"{niche}" "{city}" "contact list" filetype:xls OR filetype:xlsx
"{niche}" "{city}" "brochure" "email" filetype:pdf
```

**Extraction strategy:**
1. Download the document.
2. Extract text using a PDF parser or document reader.
3. Search the extracted text for email address patterns (`[word]@[domain].[tld]`).
4. Search for phone number patterns (international formats: `+XXX XXX XXXXXXX`).
5. Parse tabular data from spreadsheets for structured contact lists.
6. Record the document URL as the source.

#### Backlink Analysis for Contact Discovery

Backlink analysis involves examining the websites that link to a target business or professional's website. Sites that link to a business often contain contextual information about the business (mentions in blog posts, directory listings, partner pages).

**Technique:**
1. Identify a target business's website from a GMB listing or other source.
2. Use a backlink checker (or search `link:{website_url}` on Google/Bing) to discover referring pages.
3. Visit referring pages to extract additional contact information, mentions, or related businesses.
4. This technique is particularly useful for discovering industry relationships and partnership opportunities.

#### Cached Page Mining

When a live web page is unavailable (due to server downtime, site restructuring, or content removal), cached versions may still exist.

**Technique:**
1. Use Google's cache operator: `cache:{url}`
2. Use the Wayback Machine (web.archive.org) to access historical snapshots of pages.
3. Extract contact data from cached or archived versions.
4. Record that the data was sourced from a cached/archived version and note the original URL.

#### Wayback Machine Historical Data

The Internet Archive's Wayback Machine preserves snapshots of web pages over time. This is invaluable for recovering contact information from businesses that have changed their website or gone offline.

**Technique:**
1. Enter the target URL in the Wayback Machine (web.archive.org).
2. Browse the available snapshots chronologically.
3. Access snapshots from when the business was active.
4. Extract contact information from historical versions of contact pages.
5. Record the archive snapshot URL as the source.

---

## Cross-Source Enrichment

Cross-source enrichment is the process of **combining data from multiple collection methods** to build the most complete possible contact profile for each lead. A single lead may be discoverable through two or all three collection methods, each providing different data points. Merging these data points produces a superior lead record.

### Enrichment Priority Order

When enriching a lead, data should be sourced in the following priority order (highest to lowest reliability):

| Priority | Source | Data Strength | Notes |
|----------|--------|--------------|-------|
| 1 | Business's own website | Very High | Most authoritative and current source |
| 2 | GMB listing | High | Google-verified, frequently updated |
| 3 | Professional directory listing | Medium–High | Third-party verified (varies by directory) |
| 4 | LinkedIn profile | Medium | Self-reported, may be outdated |
| 5 | Social media profiles | Medium | May contain informal or personal contact info |
| 6 | Freelancer platforms | Low–Medium | May be restricted or partial |
| 7 | Cached/archived pages | Low | May be outdated but useful for historical data |
| 8 | Third-party mentions | Low | Indirect data, requires verification |

### Building a Complete Contact Profile

A fully enriched lead record should include data from as many sources as possible. Here is the ideal enrichment workflow:

1. **Start with the initial discovery source** (whichever method first identified the lead).
2. **Search for the same lead on Google Maps/GMB** — if found, merge address, phone, website, and review data.
3. **Search for the lead on LinkedIn** using `site:linkedin.com/in "{name}" "{city}"` — if found, merge professional title, company, skills, and any additional contact info.
4. **Visit the lead's website** (if available) — extract email addresses, additional phone numbers, WhatsApp links, team member info, and social media profiles from contact pages, footers, and about pages.
5. **Search for the lead on social media** — check Facebook, Instagram, Twitter/X for business pages or personal profiles with additional contact details.
6. **Search for the lead on directories** — check Yelp, Yellow Pages, and other relevant directories for additional listings with different or supplementary data.
7. **Check for document mentions** — search for the business name or professional name in publicly hosted PDFs, spreadsheets, or other documents.
8. **Consolidate** all discovered data into a single enriched record, noting the source of each data point.

### Cross-Reference Example

Consider a lead initially discovered via GMB:

**Initial GMB Record:**
- Business Name: Accra Digital Hub
- Category: Marketing Agency
- Address: 12 Oxford Street, Osu, Accra
- Phone: +233 30 277 8899
- Website: accradigitalhub.com (listed)
- Rating: 4.5 (23 reviews)

**After Cross-Source Enrichment:**

| Data Field | GMB Source | LinkedIn Source | Website Source | Social Media Source |
|------------|-----------|-----------------|----------------|-------------------|
| Business Name | Accra Digital Hub | Accra Digital Hub | Accra Digital Hub | Accra Digital Hub |
| Primary Contact | — | Kwame Mensah (CEO) | Kwame Mensah, CEO | @accradigitalhub |
| Email | — | kwame@accradigitalhub.com | info@accradigitalhub.com, kwame@accradigitalhub.com | — |
| Phone | +233 30 277 8899 | — | +233 30 277 8899, +233 24 555 1234 | — |
| WhatsApp | Possible | — | +233 24 555 1234 (listed on site) | +233 24 555 1234 (in Instagram bio) |
| Website | accradigitalhub.com | accradigitalhub.com | accradigitalhub.com | Link in bio |
| Social Media | — | — | Facebook, Twitter, Instagram | facebook.com/accradigitalhub, instagram.com/accradigitalhub |
| Team Members | — | 5 employees listed | "Our Team" page with 7 staff | — |
| Services | Digital Marketing | Marketing, SEO, PPC | Full service list on website | Highlights in posts |

The enriched record is dramatically more valuable than the initial GMB record alone — it includes direct contact details for the CEO, a verified WhatsApp number, social media profiles, team member information, and a complete service list.

### Deduplication During Cross-Source Enrichment

When merging data from multiple sources, follow the duplicate handling protocol from `AGENT_FRAMEWORK.md` Section 9:

- **Match on email address** (highest confidence — same person or business).
- **Match on phone number** (high confidence after normalization).
- **Match on website domain** (high confidence — same business).
- **Match on LinkedIn URL** (exact match — same individual).
- **Match on business name + address** (medium-high confidence).
- When in doubt, **merge rather than discard** — preserve all data and flag as a potential duplicate for later review.

---

## Session Planning

Effective session planning maximizes the productivity of each lead collection session. A well-planned session targets a specific geographic area, allocates time across all three collection methods, prioritizes high-yield niches, and tracks progress against defined targets.

### How to Plan a Collection Session for One City Area

#### Phase 1: Pre-Session Research (5–10 minutes)

1. **Review the target City Area folder** — check what data already exists to avoid redundant collection.
2. **Identify uncovered niches** — cross-reference the niche list from `AGENT_FRAMEWORK.md` Section 8 against existing data in the City Area folder.
3. **Assess the area's characteristics** — is it a commercial district (high business density), residential area (service businesses), or mixed use? This informs niche prioritization.
4. **Review any existing leads** for the area — note data quality gaps and enrichment opportunities.

#### Phase 2: Session Goal Setting (2–3 minutes)

Define clear, measurable goals for the session:

| Goal Type | Example | Target |
|-----------|---------|--------|
| Raw lead count | Total new raw leads across all methods | 50–100 new leads |
| Niche coverage | Number of niches with at least 5 leads | Cover 10+ niches |
| Enrichment count | Number of existing leads enriched | Enrich 20+ existing raw leads |
| Email discovery | Number of leads with email addresses | Add emails to 15+ leads |
| WhatsApp discovery | Number of leads with confirmed WhatsApp | Identify 10+ WhatsApp contacts |
| Geographic coverage | City Area folders populated | Populate 2–3 new City Areas |

#### Phase 3: Time Allocation

The following time allocation framework is recommended for a **60-minute focused collection session** targeting one City Area:

| Time Block | Duration | Activity | Method |
|-----------|----------|----------|--------|
| Block 1 | 15 minutes | GMB collection — primary niche search | Method 1 |
| Block 2 | 10 minutes | GMB — secondary niche searches + WhatsApp identification | Method 1 |
| Block 3 | 10 minutes | GMB raw lead recording and initial enrichment (website visits) | Method 1 + Enrichment |
| Block 4 | 10 minutes | LinkedIn public profile discovery via search operators | Method 2 |
| Block 5 | 5 minutes | LinkedIn lead recording and niche filing | Method 2 |
| Block 6 | 10 minutes | Other Public Web — directory mining + website contact extraction | Method 3 |

**For a 120-minute session,** double each block's duration and add additional time for cross-source enrichment.

#### Phase 4: Prioritization Framework

When time is limited, agents should prioritize collection activities using the following framework:

**Tier 1 — Highest Priority (always do first):**
- Niches with the highest business density in the target area (restaurants, healthcare, professional services).
- Niches that are known to have high email availability (marketing agencies, consultants, tech companies).
- GMB collection for the area (highest yield per unit time).

**Tier 2 — High Priority (do if time allows):**
- LinkedIn collection for professional niches (B2B outreach targets).
- Enrichment of existing raw leads (converting raw leads to enriched leads).
- Cross-source enrichment of leads discovered via multiple methods.

**Tier 3 — Medium Priority (schedule for future sessions):**
- Lower-density niches in the area.
- Other Web source mining beyond the top directories.
- Document harvesting and advanced techniques.

**Tier 4 — Low Priority (backlog for future sessions):**
- Cached/archived page mining.
- Backlink analysis.
- Wayback Machine historical data recovery.

#### Phase 5: Daily / Weekly Targets

For sustained repository growth, agents should maintain consistent collection cadence. The following targets provide baseline expectations:

**Daily Session Targets (60–120 minutes):**

| Metric | Minimum Target | Stretch Target |
|--------|---------------|----------------|
| New raw leads | 30 | 75 |
| Enriched leads (existing) | 10 | 30 |
| Email addresses discovered | 10 | 25 |
| WhatsApp contacts identified | 5 | 15 |
| Niches covered | 5 | 12 |
| City Areas touched | 1 | 3 |

**Weekly Targets (5 sessions):**

| Metric | Minimum Target | Stretch Target |
|--------|---------------|----------------|
| Total new raw leads | 150 | 375 |
| Total enriched leads | 50 | 150 |
| Total emails discovered | 50 | 125 |
| Niches covered per area | 15 | 40 |
| City Areas fully populated | 2 | 5 |

**Monthly Targets (20 sessions):**

| Metric | Minimum Target | Stretch Target |
|--------|---------------|----------------|
| Total new raw leads | 600 | 1,500 |
| Total enriched leads | 200 | 600 |
| Unique niches across all areas | 30 | 50 |
| City Areas fully populated | 8 | 20 |

#### Phase 6: Progress Tracking

At the end of each session, agents should record:

1. **City Area(s) worked on** — which geographic folders were targeted.
2. **Niches covered** — which business categories were searched.
3. **Leads collected per method** — breakdown by GMB, LinkedIn, and Other Web.
4. **Leads enriched** — count of raw leads upgraded to enriched status.
5. **Data quality metrics** — average completeness score, email validation results.
6. **Issues encountered** — any problems, gaps, or anomalies observed.
7. **Search operators used** — log of all search queries executed (stored in `Search_Operators_Used/` folders).

This tracking data enables session-to-session comparison, identifies productivity trends, and supports optimization of collection strategies over time.

### Session Template

The following template can be used to plan and document each collection session:

```
========================================
SESSION LOG
========================================
Date:            [YYYY-MM-DD]
Agent:           [Agent identifier]
Duration:        [HH:MM]
Target Area:     [City, State, Country — City Area]
Niches Targeted: [List niches]
========================================
METHOD 1: GMB
----------------------------------------
Queries used:    [List or reference log file]
Leads collected: [Count]
Enriched:        [Count]
Emails found:    [Count]
WhatsApp found:  [Count]
Time spent:      [HH:MM]
----------------------------------------
METHOD 2: LINKEDIN
----------------------------------------
Queries used:    [List or reference log file]
Profiles found:  [Count]
Emails visible:  [Count]
Time spent:      [HH:MM]
----------------------------------------
METHOD 3: OTHER WEB
----------------------------------------
Sources mined:   [List directories, platforms, etc.]
Leads collected: [Count]
Emails found:    [Count]
Time spent:      [HH:MM]
--------------------------------========
CROSS-SOURCE ENRICHMENT
----------------------------------------
Leads enriched:  [Count]
Duplicates found: [Count]
Merged records:  [Count]
--------------------------------========
SESSION SUMMARY
----------------------------------------
Total new leads: [Count]
Total enriched:  [Count]
Avg completeness: [Score / 100]
Issues/Notes:    [Free text]
Next session plan: [Brief plan for next session]
========================================
```

---

## Document Reference Summary

| Topic | Document | Section |
|-------|----------|---------|
| Folder structure and data format standards | `AGENT_FRAMEWORK.md` | Sections 3–7 |
| Comprehensive niche list (50+ niches) | `AGENT_FRAMEWORK.md` | Section 8 |
| Duplicate handling protocol | `AGENT_FRAMEWORK.md` | Section 9 |
| Email validation protocol | `AGENT_FRAMEWORK.md` | Section 10 |
| 500+ prebuilt search queries | `DISCOVERY_QUERIES_500_PLUS.md` | All categories |
| Google search operators playbook | `AGENT_FRAMEWORK.md` | Section 14 |
| Operational autonomy guidelines | `AGENT_FRAMEWORK.md` | Section 15 |

---

*This document is a living reference. Agents should suggest updates and improvements based on operational experience. Last reviewed: June 2025.*
