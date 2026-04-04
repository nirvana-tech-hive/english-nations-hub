# Google Search Operators Playbook — Agent Reference Guide

**Document Version:** 1.0
**Classification:** Operational Reference — Lead Discovery
**Audience:** Autonomous Lead Collection Agents
**Repository:** English Nations Hub
**Companion Document:** [DISCOVERY_QUERIES_500_PLUS.md](./DISCOVERY_QUERIES_500_PLUS.md)
**Last Updated:** June 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Core Operators Reference](#core-operators-reference)
3. [Operator Combination Principles](#operator-combination-principles)
4. [Lead Discovery Query Patterns](#lead-discovery-query-patterns)
   - [Pattern 1: Email Extraction](#pattern-1-email-extraction)
   - [Pattern 2: Phone Number Discovery](#pattern-2-phone-number-discovery)
   - [Pattern 3: LinkedIn Profile Mining](#pattern-3-linkedin-profile-mining)
   - [Pattern 4: Business Website Discovery](#pattern-4-business-website-discovery)
   - [Pattern 5: Document-Based Discovery](#pattern-5-document-based-discovery)
   - [Pattern 6: Social Media Contact Mining](#pattern-6-social-media-contact-mining)
   - [Pattern 7: Directory & Listing Mining](#pattern-7-directory--listing-mining)
   - [Pattern 8: Freelancer & Remote Worker Discovery](#pattern-8-freelancer--remote-worker-discovery)
5. [Advanced Query Techniques](#advanced-query-techniques)
6. [Query Testing Protocol](#query-testing-protocol)
7. [Rate Limiting & Best Practices](#rate-limiting--best-practices)
8. [Query Logging](#query-logging)

---

## Overview

Google search operators are the **primary discovery tool** for autonomous agents operating within the English Nations Hub repository. While the average user treats Google as a simple question-answering engine, agents must learn to think like **advanced search engineers** — leveraging operators as precision instruments that can uncover leads completely invisible to normal searches.

This playbook serves three critical functions:

1. **Reference Manual** — A complete catalog of every Google search operator that agents can deploy, with syntax rules, behavioral descriptions, and practical lead discovery use cases.

2. **Strategic Guide** — Principles and methodologies for combining operators into multi-layered queries that systematically uncover email addresses, phone numbers, social profiles, business websites, and other contact intelligence.

3. **Bridge to DISCOVERY_QUERIES_500_PLUS.md** — This playbook explains *why* and *how* each query in the 500+ query master playbook works. Agents should study this document to understand operator mechanics, then execute queries from the companion file.

### Why Operators Matter for Lead Discovery

- **Precision**: Operators let agents filter billions of web pages down to the exact subset containing contact information for a specific niche in a specific city.
- **Efficiency**: A well-crafted operator query can surface 50+ qualified leads in a single search, versus manually browsing hundreds of irrelevant pages.
- **Coverage**: Different operators expose different data sources. `site:` targets specific platforms, `filetype:` uncovers document-embedded contacts, `intitle:` catches contact pages — no single operator covers everything.
- **Reproducibility**: Operator-based queries are deterministic. The same query produces consistent results, enabling reliable lead collection at scale.

### Agent Mindset

When building queries, agents should think in terms of:

- **What am I looking for?** (email, phone, profile, website)
- **Where would it live?** (contact page, PDF, LinkedIn, directory)
- **How would it be structured?** (info@, +44, site:linkedin.com/in)
- **What would make it unique?** (niche + city + contact method)

This four-question framework drives every query in this playbook and the 500+ companion document.

---

## Core Operators Reference

The following table provides a comprehensive reference for every Google search operator relevant to lead discovery. Each entry includes the operator syntax, its core purpose, a syntax example, and a concrete lead discovery use case.

| Operator | Purpose | Syntax Example | Practical Lead Discovery Use Case |
|---|---|---|---|
| `site:` | Restrict results to a specific domain or set of domains. Essential for targeting specific platforms (LinkedIn, Yelp, GMB) or filtering out noise. | `site:linkedin.com/in "dentist" "Accra"` | Find all publicly indexed LinkedIn profiles of dentists in Accra, Ghana. Restricts results exclusively to pages within the `linkedin.com/in` URL path. |
| `inurl:` | Require that a keyword or phrase appears in the URL of the page. Ideal for finding pages with predictable URL structures like contact pages. | `inurl:contact "plumber" "Austin"` | Discover plumber business pages where "contact" appears in the URL slug — catching contact, contact-us, contact-info pages that often contain email addresses and phone numbers. |
| `intitle:` | Require that a keyword or phrase appears in the HTML `<title>` tag of the page. Useful for finding pages that explicitly declare their purpose in the title. | `intitle:contact "roofing" "Texas"` | Find roofing company pages that have "contact" in their page title, which strongly correlates with pages containing actual contact information (email, phone, address). |
| `intext:` | Require that a keyword appears in the body text of the page. This is the body-level filter — it catches text anywhere in the visible content. | `intext:"@" "restaurant" "Lagos"` | Locate pages about restaurants in Lagos where an email address (@ symbol) actually appears in the page body, filtering out pages that merely mention "email" in navigation or metadata. |
| `filetype:` | Restrict results to specific file types. Extremely powerful for discovering contacts embedded in documents that are not accessible through normal page search. Supports: pdf, doc, docx, xls, xlsx, csv, txt, ppt, pptx, rtf. | `"law firm" "Houston" "@" filetype:pdf` | Uncover PDF documents (brochures, member directories, vendor lists, event programs) hosted by or about Houston law firms that contain email addresses. PDFs often contain rich, structured contact lists. |
| `related:` | Find websites that Google considers similar to a given domain. Useful for discovering competitor businesses or niche-specific directory sites. | `related:houzz.com "contractor" "Chicago"` | Discover websites similar to Houzz that list Chicago-area contractors. Useful for finding alternative directories and listing platforms that may contain leads not found on the primary site. |
| `cache:` | View Google's cached (stored) version of a page. Useful when a live page is temporarily down, geo-restricted, or when the cached version contains older contact information. | `cache:example.com/contact` | Access a cached version of a business's contact page when the live site is unreachable. The cached version may still contain the email address and phone number from the last crawl. |
| `info:` | Retrieve metadata about a specific URL — including Google's indexed information, similar pages, and pages that link to it. | `info:accradental.com` | Gather intelligence about a business website — discover related sites, see which pages Google has indexed, and find pages linking to the business, which may contain additional contact references. |
| `OR` (capitalized) | Match either keyword (or phrase). Must be capitalized. Essential for broadening queries without losing precision. | `"dentist" "Miami" @gmail.com OR @yahoo.com OR @outlook.com` | Find dentist contacts in Miami that use any of the three most common free email providers in a single query, rather than running three separate searches. |
| `AND` (capitalized) | Match both keywords. This is actually Google's default behavior for all terms, but explicitly using AND can improve clarity in complex queries and forces both terms to appear. | `"plumber" AND "email" AND "Denver"` | Ensure all three terms appear somewhere on the page. While implicit by default, explicit AND is useful in complex Boolean expressions where operator precedence matters. |
| `-` (minus) | Exclude results containing a specific term. One of the most powerful filtering operators — removes noise, irrelevant domains, and false positives. | `"marketing agency" "London" -site:linkedin.com -site:facebook.com` | Find marketing agencies in London while excluding LinkedIn and Facebook results, forcing Google to surface business websites, directories, and other sources that may contain direct contact information. |
| `""` (quotes) | Exact phrase match. Forces Google to match the enclosed words as a consecutive phrase rather than individual keywords appearing anywhere on the page. | `"book an appointment" "dentist" "Sydney"` | Find dentist pages that contain the exact phrase "book an appointment" — a strong signal that the page has actionable contact information, as opposed to pages that merely mention "book" and "appointment" separately. |
| `*` (asterisk) | Wildcard placeholder. Represents any word or phrase in the query position. Useful when the exact wording is uncertain but the structure is known. | `"how to contact *" "accountant" "Toronto"` | Find pages where an unknown word fills the wildcard position — could match "how to contact us," "how to contact our team," "how to contact me," etc., while still requiring "accountant" and "Toronto." |
| `..` (double dot) | Number range operator. Matches any number within the specified range. Useful for filtering by year, price, quantity, or other numeric data. | `"conference" "marketing" 2023..2025 "speaker"` | Find marketing conference speaker listings from 2023 to 2025, filtering out outdated conference pages while capturing recent and upcoming events with fresh contact information. |
| `before:` | Filter results to pages indexed before a specific date. Format: `before:YYYY-MM-DD`. Essential for finding recently published leads or filtering out stale data. | `"startup" "Nairobi" "email" before:2025-07-01` | Find pages about Nairobi startups containing email addresses that were indexed before July 2025, useful for discovering leads from a specific time window. |
| `after:` | Filter results to pages indexed after a specific date. Format: `after:YYYY-MM-DD`. Ideal for finding the freshest leads and newly published contact information. | `"real estate agent" "Dubai" "phone" after:2025-01-01` | Find real estate agent pages in Dubai with phone numbers that were indexed after January 2025, ensuring the contact data is recent and more likely to be current. |
| `allinurl:` | Require that ALL specified terms appear in the URL. More restrictive than individual `inurl:` operators — every single term must be present in the URL string. | `allinurl:contact email plumber "Austin"` | Find pages where ALL of "contact," "email," "plumber," and "Austin" appear somewhere in the URL. Extremely restrictive but highly precise when results exist. |
| `allintitle:` | Require that ALL specified terms appear in the page title. Similar to `allinurl:` but targets the `<title>` tag instead of the URL. | `allintitle:contact us plumber "Chicago"` | Find pages where "contact," "us," "plumber," and "Chicago" all appear in the page title. A highly specific filter that catches well-structured contact pages. |
| `allintext:` | Require that ALL specified terms appear in the page body text. This is the most restrictive text-level operator. | `allintext:"@gmail.com" "phone" "electrician" "Ohio"` | Find pages in the body text that contain a Gmail address, phone number, "electrician," and "Ohio." Extremely targeted but may return very few results. |
| `define:` | Look up word definitions. While not directly a lead discovery operator, it is useful for understanding niche terminology before building queries. | `define:chiropractor` | Understand what a chiropractor does and what alternative terms are used, enabling more comprehensive query building for the chiropractic niche. |
| `weather:` | Retrieve weather information for a location. Useful for agents to understand geographic context, climate-based business cycles, and seasonal search patterns. | `weather:Houston` | Check Houston's current weather — useful context for understanding why certain businesses (HVAC, landscaping) may be more active in search results at specific times. |
| `map:` | Trigger Google Maps results for a location-based query. Returns map listings directly in search results. | `map:dentists in "San Francisco"` | Get Google Maps-style results for dentists in San Francisco, which often include phone numbers, addresses, and website links directly in the search results. |
| `source:` | Restrict news results to a specific news source. Useful for finding business mentions and press releases that may contain contact information. | `"tech startup" "funding" source:techcrunch.com` | Find TechCrunch articles about startup funding rounds, which often include founder names, company websites, and sometimes email addresses in press releases. |
| `location:` | Apply a geographic filter to search results. Similar in effect to appending a city name but uses Google's internal geographic understanding. | `location:"London" "marketing agency" "email"` | Filter results to those Google considers geographically relevant to London, catching businesses that serve London even if "London" does not explicitly appear on the page. |

### Operator Precedence and Behavior Notes

- **`OR` must be capitalized.** Lowercase `or` is treated as a normal search term. This is the single most common operator mistake.
- **Quotes create atomic units.** `"marketing agency"` must appear as that exact phrase. Without quotes, Google may match pages containing "marketing" and "agency" separately, anywhere on the page.
- **Operators can be combined.** `site:linkedin.com/in "CEO" OR "Founder" "Lagos"` is valid and highly effective.
- **`-` applies to the immediately following term.** `-site:linkedin.com` excludes all LinkedIn results. `-linkedin.com` (without `site:`) excludes pages containing the text "linkedin.com" anywhere.
- **`filetype:` works with a single extension.** To search multiple file types, use OR: `filetype:pdf OR filetype:xlsx`.
- **Some operators cannot be combined.** `filetype:` cannot be used with `site:` in all contexts. Test combinations before deploying at scale.
- **Google ignores more than 32 words** in a single query. Keep queries under this limit.

---

## Operator Combination Principles

Knowing individual operators is necessary but not sufficient. The real power of search operator-based lead discovery comes from **combining operators strategically** to create queries that are both broad enough to find leads and narrow enough to be relevant.

### Principle 1: Stacking Operators for Precision

Operators should be stacked from broadest to narrowest:

```
[Domain/Source Filter] + [Location] + [Niche] + [Contact Method] + [Exclusions]
```

**Example:**
```
site:yelp.com "dentist" "Austin" "email" -site:facebook.com
```

This query follows the stacking pattern:
1. **Source**: `site:yelp.com` — only Yelp pages
2. **Location**: `"Austin"` — only Austin businesses
3. **Niche**: `"dentist"` — only dental businesses
4. **Contact Method**: `"email"` — pages mentioning email
5. **Exclusion**: `-site:facebook.com` — remove Facebook cross-posts

### Principle 2: Broad vs. Narrow Queries

Agents should maintain a **spectrum of queries** from broad to narrow:

| Query Width | Example | When to Use |
|---|---|---|
| **Very Broad** | `"dentist" "Accra"` | Initial survey of the market landscape. See how many dentists are discoverable. |
| **Broad + Contact** | `"dentist" "Accra" "@"` | Casting a wide net for any email-bearing page about Accra dentists. |
| **Moderate** | `"dentist" "Accra" "email" OR "phone"` | Targeted contact discovery with reasonable specificity. |
| **Narrow** | `site:yelp.com "dentist" "Accra" "phone"` | Platform-specific contact extraction. |
| **Very Narrow** | `site:linkedin.com/in "dentist" "Accra" "clinic" "@gmail.com"` | Highly specific — expect few results but high relevance. |

### Principle 3: The Funnel Approach

The Funnel Approach is the agent's primary query construction methodology. It mirrors how a professional search engineer would systematically narrow results:

**Step 1 — Market Survey (Broadest)**
```
"{niche}" "{city}"
```
Purpose: Understand how many businesses exist in this niche + location. Gauge market size. Note common URL structures and platforms that appear.

**Step 2 — Contact Signal Detection**
```
"{niche}" "{city}" "email" OR "phone" OR "contact"
```
Purpose: Identify which businesses have publicly exposed any contact method. This is the first filtering pass.

**Step 3 — Specific Contact Type**
```
"{niche}" "{city}" "@" filetype:html inurl:contact
```
Purpose: Focus specifically on email addresses found on contact pages. Much narrower than Step 2.

**Step 4 — Platform-Specific**
```
site:google.com/maps "{niche}" "{city}" "@"
```
Purpose: Target a specific platform (Google Maps) for the highest-value leads with structured data.

**Step 5 — Precision Extraction**
```
site:yelp.com "{niche}" "{city}" "phone" -site:facebook.com -site:linkedin.com
```
Purpose: Maximum precision — one platform, one location, one niche, one contact type, noise removed.

### Principle 4: Balancing Recall vs. Precision

| Priority | Strategy | Risk |
|---|---|---|
| **Maximum Recall** (find everything) | Use broad queries, fewer operators, wider OR clauses | More noise, more false positives, more manual review needed |
| **Maximum Precision** (find only good leads) | Use many operators, exact phrases, site restrictions | May miss leads that don't perfectly match the pattern |
| **Balanced** (recommended) | Use 3-4 operators per query, test and iterate | Good coverage with manageable noise |

**Agent Recommendation:** Start balanced. Run queries with 3-4 operator combinations. If results are too noisy, add more restrictions. If results are too sparse, remove restrictions. The 500+ query playbook is designed to provide balanced queries by default.

---

## Lead Discovery Query Patterns

This section documents the eight primary query patterns used in lead discovery. Each pattern includes strategic rationale and production-ready example queries. All examples use placeholder syntax consistent with `DISCOVERY_QUERIES_500_PLUS.md`: `{niche}`, `{city}`, `{state}`, `{country}`, `{domain}`, `{extension}`.

---

### Pattern 1: Email Extraction

**Strategy Overview:** Email extraction is the highest-value lead discovery pattern. Email addresses are the primary contact method for digital marketing outreach, and they appear across an enormous variety of web sources — from business contact pages and website footers to embedded documents and directory listings.

**Key Principles:**
- The `@` symbol is the universal email indicator. Always include it in email queries.
- Different email patterns indicate different types of businesses: `info@` suggests a corporate email, `@gmail.com` suggests a freelancer or small business.
- Contact pages (`inurl:contact`, `intitle:contact`) are the densest sources of email addresses.
- Combine with `filetype:` operators to find emails embedded in documents that are invisible to normal page search.

#### Direct Email + Location + Business Type

These queries combine a niche, location, and email signal to find businesses that have publicly exposed their email address:

```
"{niche}" "{city}" "email" "@gmail.com"
"{niche}" "{city}" "contact us" "@" "{state}"
"{niche}" "{city}" "get in touch" "@"
"{niche}" "{city}" "reach us" "email"
"{niche}" "{city}" "inquiries@" OR "info@" OR "contact@"
"{niche}" "{city}" "email:" -site:linkedin.com
"{niche}" "{city}" "mail:" OR "e-mail:" OR "email address"
"{niche}" "{city}" "@" filetype:html
"{niche}" "{city}" "send us an email" OR "drop us an email"
"{niche}" "{city}" "hello@" OR "team@" OR "support@"
"{niche}" "{city}" site:.com "@" "contact"
"{niche}" "{city}" "email me" OR "email us" "@"
"{niche}" "{city}" "book@" OR "booking@" OR "appointment@"
"{niche}" "{city}" "director@" OR "manager@" OR "owner@"
"{niche}" "{city}" "\"email\"" "\"phone\"" "{state}"
```

#### Filetype-Based Email Discovery

Email addresses embedded in publicly hosted documents are a goldmine that most conventional searches miss entirely:

```
"{niche}" "{city}" "@" filetype:pdf
"{niche}" "{city}" "@" filetype:xls OR filetype:xlsx
"{niche}" "{city}" "@" filetype:doc OR filetype:docx
"{niche}" "{city}" "contact" "@" filetype:txt
"{niche}" "{city}" "email list" filetype:csv
"{niche}" "{state}" "@" filetype:pdf "{country}"
"{niche}" "{city}" "directory" "@" filetype:pdf
"{niche}" "{city}" "member list" "@" filetype:xlsx
"{niche}" "{city}" "contact details" "@" filetype:pdf
"{niche}" "{city}" "email directory" filetype:pdf OR filetype:xlsx
```

#### Contact Page Email Mining

Targeting pages specifically designed for contact information yields the highest density of email addresses per result:

```
"{niche}" inurl:contact "{city}"
"{niche}" "{city}" intext:"@" intitle:"contact"
"{niche}" "{city}" site:.com "info@" OR "contact@"
"{niche}" "{city}" inurl:contact intext:"@" site:.com
"{niche}" "{city}" intitle:"contact" "email" site:.com
"{niche}" "{city}" inurl:contact-us "@" OR inurl:contact-us "email"
"{niche}" "{city}" inurl:get-in-touch "@" OR "email"
```

---

### Pattern 2: Phone Number Discovery

**Strategy Overview:** Phone numbers are critical for WhatsApp outreach, SMS marketing, and voice contact. Phone numbers appear prominently on directory listings, contact pages, Google Maps listings, social media profiles, and classified ad platforms. Different countries use different phone number formats, so queries should account for local conventions.

**Key Principles:**
- Phone numbers often appear alongside keywords like "call," "tel," "phone," "mobile," "cell," "telephone."
- Include country codes in queries when targeting specific nations: `+1` (US/Canada), `+44` (UK), `+234` (Nigeria), `+233` (Ghana), `+61` (Australia), `+27` (South Africa), `+1` (Jamaica), `+254` (Kenya), `+971` (UAE), `+91` (India).
- WhatsApp numbers are often shared explicitly with "WhatsApp" or "wa.me" keywords.

#### Direct Phone + Location

```
"{niche}" "{city}" "phone" OR "tel" OR "call" "{state}"
"{niche}" "{city}" intext:"phone:" OR intext:"tel:" OR intext:"call us"
"{niche}" "{city}" inurl:contact "phone" site:.com
"{niche}" "{city}" "\"phone\"" "\"email\"" "{state}"
"{niche}" "{city}" "mobile" OR "cell" OR "telephone" "contact"
"{niche}" "{city}" site:yelp.com "{niche}" "phone"
"{niche}" "{city}" site:yellowpages.com OR site:yellowpages.ca
"{niche}" "{city}" "+1" OR "+44" OR "+234" "{niche}" "contact"
"{niche}" "{city}" "call now" OR "dial" "phone"
"{niche}" "{city}" "contact number" OR "phone number" "{niche}"
```

#### WhatsApp Number Patterns

```
"{niche}" "{city}" "whatsapp" "{niche}" "contact"
"{niche}" "{city}" "whatsapp" "number" OR "phone"
"{niche}" "{city}" "chat on whatsapp" OR "whatsapp us"
"{niche}" "{city}" "wa.me" OR "api.whatsapp.com"
"{niche}" "{city}" "whatsapp" "+1" OR "+44" OR "+234" OR "+91"
"{niche}" "{city}" "message us on whatsapp" OR "reach us on whatsapp"
"{niche}" "{city}" "whatsapp" site:facebook.com OR site:instagram.com
"{niche}" "{city}" "whatsapp business" "contact"
"{niche}" "{city}" "order via whatsapp" OR "book via whatsapp"
"{niche}" "{city}" "whatsapp" "link" "{niche}"
```

#### Business Phone Directories

```
"{niche}" "{city}" site:yp.com OR site:yellowbook.com
"{niche}" "{city}" site:whitepages.com
"{niche}" "{city}" site:craigslist.org "phone"
"{niche}" "{city}" site:classifiedads.com "{niche}" "phone"
"{niche}" "{city}" site:locanto.com "{niche}" "phone"
"{niche}" "{city}" site:gumtree.com OR site:gumtree.co.za
"{niche}" "{city}" site:angieslist.com OR site:homeadvisor.com
"{niche}" "{city}" site:foursquare.com
"{niche}" "{city}" "phone" site:bbb.org
"{niche}" "{city}" site:thumbr.com OR site:citysearch.com
```

---

### Pattern 3: LinkedIn Profile Mining

**Strategy Overview:** LinkedIn is the premier platform for professional lead discovery. While LinkedIn's internal search requires authentication, Google indexes millions of public LinkedIn profiles that are accessible through search operators. These profiles expose names, job titles, companies, locations, and sometimes email addresses.

**Key Principles:**
- `site:linkedin.com/in` targets individual profiles (as opposed to company pages at `site:linkedin.com/company`).
- Public profiles may have limited information — capture whatever is visible.
- Combine profession keywords with location keywords for the best results.
- Job title-based searches (`CEO`, `Founder`, `Director`) yield decision-maker leads ideal for B2B outreach.

#### Public Profile Discovery by Profession + Location

```
site:linkedin.com/in "{niche}" "{city}"
site:linkedin.com/in "{niche}" "{state}"
site:linkedin.com/in "{niche}" "{country}"
site:linkedin.com/in "{niche}" "{city}" "{state}"
site:linkedin.com/in "professional" "{niche}" "{city}"
site:linkedin.com/in "specialist" "{niche}" "{city}"
site:linkedin.com/in "manager" "{niche}" "{city}"
site:linkedin.com/in "director" "{niche}" "{city}"
site:linkedin.com/in "expert" "{niche}" "{city}"
site:linkedin.com/in "consultant" "{niche}" "{city}"
site:linkedin.com/in "founder" OR "ceo" "{niche}" "{city}"
site:linkedin.com/in "freelance" "{niche}" "{city}"
site:linkedin.com/in "{niche}" "open to work" "{city}"
site:linkedin.com/in "{niche}" "{city}" "experience"
```

#### Title-Based Searches

```
site:linkedin.com/in "{niche}" "{city}" "CEO" OR "Founder" OR "Owner"
site:linkedin.com/in "{niche}" "{city}" "Marketing Manager" OR "Marketing Director"
site:linkedin.com/in "{niche}" "{city}" "Sales Manager" OR "Business Development"
site:linkedin.com/in "{niche}" "{city}" "Operations Manager" OR "General Manager"
site:linkedin.com/in "{niche}" "{city}" "HR Manager" OR "Human Resources"
site:linkedin.com/in "{niche}" "{city}" "IT Director" OR "CTO" OR "CIO"
site:linkedin.com/in "{niche}" "{city}" "VP" OR "Vice President"
site:linkedin.com/in "{niche}" "{city}" "Senior" OR "Lead" OR "Head"
site:linkedin.com/in "{niche}" "{city}" "Supervisor" OR "Team Lead"
site:linkedin.com/in "{niche}" "{city}" "Associate" OR "Analyst"
site:linkedin.com/in "{niche}" "{city}" "President" OR "Chairman"
site:linkedin.com/in "{niche}" "{city}" "Engineer" OR "Developer" OR "Architect"
site:linkedin.com/in "{niche}" "{city}" "Professor" OR "Doctor" OR "Attorney"
site:linkedin.com/in "{niche}" "{city}" "Partner" OR "Principal"
site:linkedin.com/in "{niche}" "{city}" "Coordinator" OR "Specialist"
```

#### Company-Linked Profiles

```
site:linkedin.com/company "{niche}" "{city}"
site:linkedin.com/company "{niche}" "{state}"
site:linkedin.com/company "{niche}" "{country}" "employees"
site:linkedin.com/company "{niche}" "{city}" "website"
site:linkedin.com/company "{niche}" "{city}" "industry"
site:linkedin.com/company "{niche}" "{city}" "size" OR "employees"
site:linkedin.com/company "{niche}" "{city}" "about" OR "overview"
site:linkedin.com/company "{niche}" "{city}" "services" OR "products"
site:linkedin.com/company "{niche}" "{state}" "followers" OR "connections"
site:linkedin.com/company "{niche}" "{city}" "careers" OR "jobs"
```

---

### Pattern 4: Business Website Discovery

**Strategy Overview:** A business's own website is the single most authoritative source of contact information. While finding individual business websites requires broad queries, the reward is substantial — website contact pages typically contain the most complete and accurate contact details available anywhere online.

**Key Principles:**
- Target contact pages directly with `inurl:contact` and `intitle:contact`.
- "About" pages often contain team member names, roles, and sometimes personal email addresses.
- Website footers frequently contain email addresses and phone numbers embedded in the HTML.
- Use `site:.com` or `site:.{extension}` to restrict to business domains.

#### Finding Business Websites by Niche + Location

```
"{niche}" "{city}" site:.com "contact"
"{niche}" "{city}" site:.com "about"
"{niche}" "{city}" site:.co.uk "email" OR "phone"
"{niche}" "{city}" site:.com.ng "@" OR "contact"
"{niche}" "{city}" site:.com.au "business"
"{niche}" "{city}" "services" site:.com
"{niche}" "{city}" "website" OR "www" "{niche}"
"{niche}" "{city}" "official website" OR "official site"
"{niche}" "{city}" site:.com -site:linkedin.com -site:facebook.com
"{niche}" "{state}" site:.com "{niche}" "contact us"
```

#### Contact Page Discovery

```
"{niche}" "{city}" inurl:contact
"{niche}" "{city}" inurl:contact-us
"{niche}" "{city}" inurl:get-in-touch
"{niche}" "{city}" intitle:"Contact Us" OR intitle:"Contact Me"
"{niche}" "{city}" "reach out" OR "get in touch" site:.com
"{niche}" "{city}" inurl:contact "@" OR inurl:contact "email"
"{niche}" "{city}" inurl:contact "phone" OR "tel"
"{niche}" "{city}" "send us a message" OR "drop us a line"
"{niche}" "{city}" inurl:contact "whatsapp" OR "wa.me"
"{niche}" "{city}" "appointment" OR "booking" inurl:contact
```

#### About Page Intelligence

```
"{niche}" "{city}" inurl:about "team"
"{niche}" "{city}" inurl:about-us "founder" OR "owner"
"{niche}" "{city}" inurl:about "director" OR "manager" "@"
"{niche}" "{city}" "meet our team" OR "our team" site:.com
"{niche}" "{city}" "about us" "email" OR "phone" site:.com
```

---

### Pattern 5: Document-Based Discovery

**Strategy Overview:** Emails, phone numbers, and contact lists are frequently embedded in publicly hosted documents — PDFs, spreadsheets, presentations, and text files. These documents are often invisible to standard web searches but can be uncovered using the `filetype:` operator. Document-based discovery is one of the highest-yield patterns because documents typically contain **structured, dense contact data** (lists, tables, directories) rather than scattered individual contacts.

**Key Principles:**
- PDFs are the most common document type on the web. They often contain brochures, directories, membership lists, and vendor catalogs with embedded contacts.
- Excel files (`.xls`, `.xlsx`) frequently contain structured contact lists — member rosters, client databases, email lists.
- CSV files are often generated by export tools and may contain massive, structured contact databases left publicly accessible.
- PowerPoint files (`.ppt`, `.pptx`) from conferences and company presentations sometimes contain speaker and company contact details.

#### PDF Email Harvesting

```
"{niche}" "{city}" "email" filetype:pdf
"{niche}" "{city}" "directory" filetype:pdf
"{niche}" "{city}" "member" OR "members" filetype:pdf
"{niche}" "{city}" "contact list" filetype:pdf
"{niche}" "{city}" "vendor" OR "supplier" filetype:pdf
"{niche}" "{state}" "@" filetype:pdf
"{niche}" "{city}" "brochure" "email" filetype:pdf
"{niche}" "{city}" "catalog" "@" filetype:pdf
"{niche}" "{city}" "newsletter" "email" filetype:pdf
"{niche}" "{country}" "{niche}" "email directory" filetype:pdf
```

#### Spreadsheet Data Extraction

```
"{niche}" "{city}" "email" filetype:xls OR filetype:xlsx
"{niche}" "{city}" "database" filetype:xlsx
"{niche}" "{city}" "list" filetype:xls OR filetype:xlsx
"{niche}" "{city}" "member list" filetype:xlsx
"{niche}" "{state}" "@" filetype:xls
"{niche}" "{city}" "directory" filetype:xlsx
"{niche}" "{city}" "contacts" filetype:xlsx OR filetype:csv
"{niche}" "{city}" "vendor list" filetype:xlsx
"{niche}" "{city}" "client list" filetype:xlsx
"{niche}" "{city}" "leads" filetype:xlsx OR filetype:csv
```

#### Presentation File Intelligence

```
"{niche}" "{city}" "email" filetype:ppt OR filetype:pptx
"{niche}" "{city}" "contact" filetype:pptx
"{niche}" "{city}" "speaker" filetype:ppt OR filetype:pptx
"{niche}" "{city}" "presentation" "@" filetype:pptx
"{niche}" "{state}" "@" filetype:ppt OR filetype:pptx
"{niche}" "{city}" "company profile" filetype:pptx
"{niche}" "{city}" "proposal" "@" filetype:pdf OR filetype:pptx
"{niche}" "{city}" "deck" "contact" filetype:pptx
"{niche}" "{city}" "introduction" "@" filetype:pptx
"{niche}" "{country}" "{niche}" filetype:pptx "@"
```

---

### Pattern 6: Social Media Contact Mining

**Strategy Overview:** Social media platforms host millions of business profiles and professional accounts that contain contact information. Instagram business bios, Facebook page "About" sections, Twitter/X bios, TikTok profiles, and YouTube channel descriptions frequently expose email addresses, phone numbers, WhatsApp numbers, and website links.

**Key Principles:**
- Instagram business profiles almost always have an email in the bio or behind the "Email" button.
- Facebook business pages expose phone numbers, emails, and WhatsApp links in their About section.
- Twitter/X bios are frequently used by freelancers and solopreneurs to share contact email.
- YouTube channel "About" pages often contain "Business Inquiries" email addresses.
- Link-in-bio tools (Linktree, Beacons, Carrd) aggregate multiple contact methods.

#### Instagram Business Accounts

```
site:instagram.com "{niche}" "{city}" "email" OR "contact"
site:instagram.com "{niche}" "{city}" "@" "bio"
"{niche}" "{city}" site:instagram.com "book now" OR "DM" OR "message"
site:instagram.com "{niche}" "{city}" "link in bio" "@"
"{niche}" "{city}" "instagram" "@" "contact" OR "email"
site:instagram.com "{niche}" "{city}" "business" OR "official"
"{niche}" "{city}" "instagram.com" "@" "{niche}"
"{niche}" "{city}" site:instagram.com "call" OR "whatsapp" OR "phone"
site:instagram.com "{niche}" "{state}" "email" OR "contact"
"{niche}" "{city}" "instagram" "gmail.com" OR "yahoo.com"
```

#### Facebook Page Contacts

```
site:facebook.com "{niche}" "{city}" "contact" OR "email" OR "phone"
site:facebook.com "{niche}" "{city}" "about" "@"
site:facebook.com "{niche}" "{city}" "whatsapp" OR "message"
site:facebook.com "{niche}" "{city}" "services" "contact"
"{niche}" "{city}" site:facebook.com "page" "phone" OR "call"
site:facebook.com "{niche}" "{city}" "reviews" OR "recommendations"
site:facebook.com "{niche}" "{city}" "book now" OR "send message"
"{niche}" "{city}" site:facebook.com "community" OR "group" "contact"
site:facebook.com "{niche}" "{state}" "@" "business"
"{niche}" "{city}" "facebook page" "@" "{niche}"
```

#### Twitter/X Professional Profiles

```
site:twitter.com "{niche}" "{city}" "@" OR "email"
site:x.com "{niche}" "{city}" "email" OR "contact"
"{niche}" "{city}" site:twitter.com "DM" OR "message" "business"
site:twitter.com "{niche}" "{city}" "bio" "@"
"{niche}" "{city}" site:twitter.com "founder" OR "ceo" OR "owner"
site:twitter.com "{niche}" "{city}" "hire me" OR "freelance" "@"
"{niche}" "{city}" "twitter.com" "email" OR "contact me"
site:twitter.com "{niche}" "{state}" "contact" "@"
"{niche}" "{city}" "tweet" "email" "gmail.com"
"{niche}" "{city}" site:twitter.com "website" OR "link" "bio"
```

---

### Pattern 7: Directory & Listing Mining

**Strategy Overview:** Business directories (Yelp, Yellow Pages, TripAdvisor, Houzz, BBB, Foursquare, and hundreds of niche-specific directories) are structured databases of business information. They provide verified business names, phone numbers, addresses, website URLs, and sometimes email addresses. Directory mining is one of the most reliable and scalable lead discovery patterns because directories are designed to expose business data.

**Key Principles:**
- Each directory platform has a different data model — Yelp exposes phone and website, TripAdvisor exposes phone and email for hospitality, Houzz exposes email for home services.
- Government business registries and chamber of commerce listings provide high-authority data.
- Industry-specific directories (e.g., Avvo for lawyers, Zillow for real estate) provide niche-targeted leads.
- Always cross-reference directory leads with other sources (business website, GMB listing) for enrichment.

#### Yelp, Yellow Pages, TripAdvisor

```
site:yelp.com "{niche}" "{city}" "phone"
site:yelp.com "{niche}" "{city}" "email" OR "contact"
site:yelp.com "{niche}" "{city}" "website" OR "biz"
site:yellowpages.com "{niche}" "{city}" "phone" OR "email"
site:yellowpages.com "{niche}" "{city}" "website"
site:yell.com "{niche}" "{city}" "phone" OR "email"
site:tripadvisor.com "{niche}" "{city}" "phone" OR "email"
site:tripadvisor.com "{niche}" "{city}" "website" OR "contact"
site:tripadvisor.com "hotel" "{city}" "email" OR "phone"
```

#### Industry-Specific Directories

```
site:houzz.com "{niche}" "{city}" "email" OR "phone"
site:houzz.com "{niche}" "{city}" "professional" OR "pro"
site:bbb.org "{niche}" "{city}" "phone" OR "website"
site:chamberofcommerce.com "{niche}" "{city}" "contact"
site:hotfrog.com "{niche}" "{city}" "email" OR "phone"
site:manta.com "{niche}" "{city}" "contact"
site:clutch.co "{niche}" "{city}" "email" OR "phone"
site:goodfirms.co "{niche}" "{city}" "contact"
site:avvo.com "lawyer" "{city}" "phone" OR "email"
site:zillow.com "{niche}" "{city}" "contact"
```

#### Government Business Registries

```
site:gov.uk "{niche}" "{city}" "register"
site:sec.gov "{niche}" OR "business" "{state}"
site:gov.au "business register" "{city}"
site:companieshouse.gov.uk "{niche}" "{city}"
site:cac.gov.ng "business registration" "{city}"
site:irs.gov "{niche}" "{state}"
"{niche}" "{city}" "business license" site:.gov
"{niche}" "{state}" "registered business" site:.gov
```

---

### Pattern 8: Freelancer & Remote Worker Discovery

**Strategy Overview:** Freelancers, remote workers, and independent professionals represent a high-value lead segment for B2B services. They actively seek clients, maintain public portfolios, and often list direct contact methods. Discovery targets include freelancer platforms (Upwork, Fiverr, Toptal), portfolio sites (Behance, Dribbble, GitHub), and personal websites.

**Key Principles:**
- Freelancers on platforms like Upwork and Fiverr often have personal websites listed in their profiles — follow those links for direct contact info.
- Portfolio platforms (Behance, Dribbble) have a high density of "hire me" pages with email addresses.
- GitHub profiles may contain email in README files and profile settings.
- Remote workers frequently list their location as "Remote" or their home city — account for both patterns.

#### Platform-Specific Queries

```
site:upwork.com "{niche}" "{city}"
site:upwork.com "{niche}" "{country}" "freelancer"
site:upwork.com "{niche}" "profile" "{city}"
site:upwork.com "{niche}" "{city}" "@" OR "email"
site:fiverr.com "{niche}" "{city}"
site:fiverr.com "{niche}" "seller" OR "freelancer" "{country}"
site:fiverr.com "{niche}" "gig" "@" OR "contact"
site:toptal.com "{niche}" "{city}"
site:peopleperhour.com "{niche}" "{city}" "contact"
site:guru.com "{niche}" "{city}" "freelancer"
site:freelancer.com "{niche}" "{city}" "hire"
```

#### Portfolio-Based Queries

```
site:behance.net "{niche}" "{city}" "email"
site:behance.net "{niche}" "{city}" "@" OR "hire me"
site:dribbble.com "{niche}" "{city}" "@" OR "email"
site:dribbble.com "{niche}" "{city}" "hire" OR "available"
site:github.com "{niche}" "{city}" "email" OR "@"
site:github.com "{niche}" "{city}" "hire me" OR "available"
site:github.com "{niche}" "{city}" "README" "@"
"{niche}" "{city}" site:wordpress.com "contact" "@"
"{niche}" "{city}" site:wix.com "email" OR "contact"
"{niche}" "{city}" site:squarespace.com "contact" "@"
"{niche}" "{city}" site:carrd.co "email" OR "hire"
```

#### Remote Job Listing Queries

```
site:remote.co "{niche}" "{city}"
site:weworkremotely.com "{niche}" "{city}"
site:remoteok.com "{niche}" "{country}"
site:indeed.com "{niche}" "{city}" "resume" "@"
site:ziprecruiter.com "{niche}" "{city}" "email"
site:monster.com "{niche}" "{city}" "contact"
site:glassdoor.com "{niche}" "{city}" "website" OR "email"
site:flexjobs.com "{niche}" "{state}" "contact"
site:linkedin.com/jobs "{niche}" "{city}" "remote"
```

---

## Advanced Query Techniques

### The Boolean Funnel

The Boolean Funnel is a systematic method for building queries that progress from maximum breadth to maximum precision. Agents should use this approach when entering a new niche or geographic area to calibrate their queries before running large-scale collection.

**Level 1 — Market Survey:**
```
"{niche}" "{city}"
```
*Goal: Count total results. Understand market size. Note top platforms.*

**Level 2 — Contact Signal:**
```
"{niche}" "{city}" "email" OR "@" OR "phone" OR "contact"
```
*Goal: What percentage of results have any contact information?*

**Level 3 — Platform Identification:**
```
"{niche}" "{city}" site:yelp.com
"{niche}" "{city}" site:linkedin.com/in
"{niche}" "{city}" site:google.com/maps
```
*Goal: Which platforms have the most results? Prioritize those platforms.*

**Level 4 — Email-Specific:**
```
"{niche}" "{city}" "@" site:yelp.com
"{niche}" "{city}" "@" filetype:pdf
"{niche}" "{city}" "@" inurl:contact
```
*Goal: How many results have actual email addresses?*

**Level 5 — Maximum Precision:**
```
"{niche}" "{city}" "info@" OR "contact@" site:.com -site:linkedin.com
```
*Goal: High-confidence, email-bearing, domain-verified leads.*

### Cross-Reference Queries

Cross-referencing is the practice of finding the same business across multiple sources. This serves two purposes: **verification** (confirming the lead is real and current) and **enrichment** (discovering additional contact fields from a different source).

**Strategy 1 — From Directory to Website:**
```
Step 1: site:yelp.com "{niche}" "{city}"
→ Find business name: "Sunrise Dental Clinic"
Step 2: "Sunrise Dental Clinic" "{city}" "email" OR "@" site:.com
→ Find the actual website and extract email
```

**Strategy 2 — From LinkedIn to Website:**
```
Step 1: site:linkedin.com/in "{niche}" "{city}"
→ Find name: "Dr. Jane Smith", company: "Smith Dental"
Step 2: "Smith Dental" "{city}" "contact" "@"
→ Find the clinic website and contact details
```

**Strategy 3 — Verification Query:**
```
"business name" "{city}" "phone" OR "email"
```
*Run this after discovering a lead from any source to verify the contact information against other web references.*

### Competitive Intelligence Queries

Beyond individual lead discovery, search operators can be used for competitive intelligence — understanding the market landscape, identifying competitor businesses, and estimating market size.

**Finding Competitors in the Same Niche:**
```
"{niche}" "{city}" -site:linkedin.com -site:facebook.com -site:instagram.com
```
*Returns business websites for the niche, excluding social platforms to surface actual competitors.*

**Discovering Competitor Client Lists:**
```
"client" OR "customer" OR "project" "for" "{competitor name}" filetype:pdf
```
*Some businesses publish case studies, portfolios, or client lists as PDFs.*

**Market Size Estimation:**
```
"{niche}" "{city}" site:google.com/maps
"{niche}" "{city}" site:yelp.com
"{niche}" "{city}" site:linkedin.com/in
```
*Count results from each source to estimate total market size and coverage gaps.*

**Industry Event Discovery:**
```
"{niche}" "conference" OR "summit" OR "expo" "{country}" 2024..2025
```
*Find industry events where potential leads may be speakers, attendees, or sponsors.*

---

## Query Testing Protocol

Agents should **never deploy queries at scale without testing**. The testing protocol ensures queries produce useful results before committing processing resources.

### Step 1: Single Query Test

Execute the query manually (or through a single API call) and evaluate the first 10 results:

- **Relevance check:** Are the results actually about `{niche}` businesses in `{city}`?
- **Contact density:** What percentage of results on the first page contain an email, phone, or other contact method?
- **Source diversity:** Are results coming from multiple domains, or is one domain dominating?
- **Freshness check:** Are the results recent? Are there dead links or outdated information?

### Step 2: Results Count Assessment

- **0 results:** Query is too restrictive. Remove one operator and retry.
- **1-10 results:** Very narrow. Useful for precision targeting but will not yield many leads.
- **10-100 results:** Ideal range. Good balance of precision and recall.
- **100-1,000 results:** Broad. May contain noise. Consider adding a restriction.
- **1,000+ results:** Very broad. High recall but likely low precision. Add location, niche, or platform restrictions.

### Step 3: Contact Extraction Test

From the first page of results, attempt to extract actual contact information:

- How many results have a visible email address?
- How many have a phone number?
- How many have a website URL that can be visited for further extraction?
- What is the **contact yield rate** (percentage of results with at least one contact field)?

### Step 4: Iteration

Based on test results, iterate on the query:

| Problem | Solution |
|---|---|
| Too few results | Remove a restriction, broaden location (city → state), add OR alternatives |
| Too many irrelevant results | Add an exclusion (-site:), require intitle:, add a specific contact method |
| No contact information found | Target contact pages (inurl:contact), try filetype: operators, switch platforms |
| All results from one source | Add -site: exclusions to force diversity |
| Results are outdated | Add after: date filter |

### Step 5: Abandonment Criteria

Abandon a query pattern if:
- After 3 iterations, it still produces zero results.
- The contact yield rate is below 5% (fewer than 1 in 20 results has any contact info).
- All results are from a single, already-exhausted source.
- The results are consistently irrelevant to the target niche and location.

When abandoning a pattern, log the attempted queries and the reason for abandonment. This prevents future agents from repeating unsuccessful attempts.

---

## Rate Limiting & Best Practices

### Google Rate Limits

Google imposes rate limits on automated search queries to prevent abuse. Agents must operate within these limits to avoid temporary or permanent blocks.

| Behavior | Recommended Limit | Risk of Exceeding |
|---|---|---|
| Queries per minute | 5-10 | Temporary IP block (429 errors) |
| Queries per hour | 100-200 | Extended block (hours) |
| Queries per day | 500-1,000 | Possible permanent IP restriction |
| Consecutive identical queries | Avoid | Results may be throttled or blocked |
| Queries from same session without delay | 3-second minimum delay | Risk of CAPTCHA or block |

### Mitigation Strategies

1. **Rotate queries.** Never execute the exact same query repeatedly. Even minor variations (adding a space, changing word order) help.
2. **Add random delays.** Wait 3-10 seconds between queries. Vary the delay duration.
3. **Rotate IP addresses** when possible. Different geographic IPs have separate rate limit quotas.
4. **Use session management.** Clear cookies and start fresh sessions periodically.
5. **Batch and schedule.** Run queries in batches of 50-100, then pause for 30-60 minutes before the next batch.
6. **Prioritize high-value queries.** Run the most promising queries first in case rate limits are hit.
7. **Use Google Custom Search API** when available — it has a formal quota system (100 queries/day free, 10,000/day paid) and is designed for programmatic use.

### Respecting robots.txt

Agents should respect `robots.txt` directives:

- **Allow:** Indexing of public business listings, contact pages, directory entries, social media profiles.
- **Avoid:** Crawling behind login walls, scraping private profile data, accessing pages explicitly blocked by robots.txt.
- **Principle:** Only access data that is publicly indexable and intended to be visible. The English Nations Hub operates on publicly available information only.

### Ethical Boundaries

- Only collect contact information that is **publicly posted** by the business or individual.
- Do not circumvent paywalls, login requirements, or access restrictions.
- Do not use deceptive techniques to obtain private contact information.
- Respect GDPR, CAN-SPAM, and other applicable data protection regulations.
- All data collected should be treated as public business intelligence for outreach purposes.

---

## Query Logging

Every query executed by an agent should be logged for reproducibility, optimization, and quality assurance. Query logs enable future agents to learn from past successes and failures, avoid repeating ineffective queries, and continuously improve discovery performance.

### Required Log Fields

| Field | Description | Example |
|---|---|---|
| **Query Text** | The exact search query string executed | `"dentist" "Accra" "@" filetype:pdf` |
| **Date Used** | The date the query was executed | `2025-06-15` |
| **Time Used** | The time the query was executed (for rate limit tracking) | `14:32:00 UTC` |
| **Location Targeted** | The geographic location the query targeted | `Accra, Ghana` |
| **Niche Targeted** | The business niche or profession targeted | `Dentists` |
| **Source Platform** | The primary platform targeted (if any) | `Google Web Search` |
| **Total Results Count** | Number of results returned by Google | `47` |
| **Leads Extracted Count** | Number of actual leads extracted from results | `12` |
| **Contact Yield Rate** | Percentage of results yielding at least one contact field | `25.5%` |
| **Query Pattern** | Which query pattern this belongs to (1-8 from this playbook) | `Pattern 5: Document-Based Discovery` |
| **Agent ID** | Identifier of the agent that executed the query | `Agent-ENH-001` |
| **Notes** | Any observations, issues, or follow-up actions | `High yield rate. Several outdated PDFs noted.` |

### Storage Location

Query logs should be stored in the relevant city area folder alongside the collected leads:

```
{City-Area}/
├── GMB_Leads/
│   ├── Raw_Leads/
│   ├── Enriched_Leads/
│   ├── Niches/
│   └── Query_Log/
│       └── query_log.csv
├── LinkedIn_Public_Leads/
│   ├── Niches/
│   ├── Search_Operators_Used/
│   └── Query_Log/
│       └── query_log.csv
└── Other_Public_Web_Leads/
    ├── Business_Niches/
    ├── Skilled_Professionals/
    └── Query_Log/
        └── query_log.csv
```

### Query Log CSV Format

```csv
Query Text,Date Used,Time Used,Location Targeted,Niche Targeted,Source Platform,Total Results Count,Leads Extracted Count,Contact Yield Rate,Query Pattern,Agent ID,Notes
"\"dentist\" \"Accra\" \"@\" filetype:pdf","2025-06-15","14:32:00","Accra, Ghana","Dentists","Google Web Search","47","12","25.5%","Pattern 5: Document-Based Discovery","Agent-ENH-001","High yield rate. Several outdated PDFs noted."
```

### Log Analysis

Agents should periodically analyze query logs to:

1. **Identify top-performing queries** — queries with the highest contact yield rate should be prioritized and expanded.
2. **Identify underperforming queries** — queries with low yield rates should be modified or abandoned.
3. **Track coverage progress** — monitor how many unique leads have been collected per niche per location.
4. **Detect source depletion** — if a source that previously yielded many leads now yields few, it may be exhausted for that niche/location.
5. **Calculate overall efficiency** — leads extracted per query executed, to optimize resource allocation.

---

## Appendix: Quick Reference Card

### Most-Used Operators (Top 10 for Lead Discovery)

| Rank | Operator | Primary Use |
|---|---|---|
| 1 | `site:` | Platform-specific targeting (LinkedIn, Yelp, GMB) |
| 2 | `filetype:` | Document-embedded contact discovery |
| 3 | `""` (quotes) | Exact phrase matching for precision |
| 4 | `OR` | Broadening queries across synonyms |
| 5 | `-` (minus) | Noise reduction and source exclusion |
| 6 | `inurl:` | Contact page and URL structure targeting |
| 7 | `intitle:` | Page title-based filtering |
| 8 | `intext:` | Body text content filtering |
| 9 | `@` (symbol) | Email address detection |
| 10 | `before:` / `after:` | Temporal filtering for freshness |

### Common Country Codes for Phone Queries

| Country | Code | Query Example |
|---|---|---|
| USA / Canada | `+1` | `"+1" "dentist" "Houston" "phone"` |
| UK | `+44` | `"+44" "dentist" "London" "phone"` |
| Nigeria | `+234` | `"+234" "dentist" "Lagos" "phone"` |
| Ghana | `+233` | `"+233" "dentist" "Accra" "phone"` |
| Australia | `+61` | `"+61" "dentist" "Sydney" "phone"` |
| South Africa | `+27` | `"+27" "dentist" "Johannesburg" "phone"` |
| Kenya | `+254` | `"+254" "dentist" "Nairobi" "phone"` |
| India | `+91` | `"+91" "dentist" "Mumbai" "phone"` |
| Jamaica | `+1` (876) | `"876" "dentist" "Kingston" "phone"` |
| Ireland | `+353` | `"+353" "dentist" "Dublin" "phone"` |
| New Zealand | `+64` | `"+64" "dentist" "Auckland" "phone"` |
| UAE | `+971` | `"+971" "dentist" "Dubai" "phone"` |

---

*This playbook is a living document. Agents are encouraged to suggest additions, report ineffective queries, and contribute new query patterns as they are discovered during operation.*
