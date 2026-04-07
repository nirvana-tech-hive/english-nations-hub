# Geographic Handling — Intelligent Lead Placement

> **Document Version:** 1.0
> **Classification:** Operational Reference — Geographic Intelligence
> **Audience:** Autonomous Lead Collection Agents, Repository Maintainers
> **Repository:** English Nations Hub
> **Last Updated:** June 2025

---

## Table of Contents

1. [Overview](#overview)
2. [The Hierarchy](#the-hierarchy)
3. [The Golden Rule](#the-golden-rule)
4. [Incomplete Data Scenarios & Solutions](#incomplete-data-scenarios--solutions)
5. [Fallback Folder Creation Rules](#fallback-folder-creation-rules)
6. [Geographic Data Fields](#geographic-data-fields)
7. [Country-Specific Notes](#country-specific-notes)
8. [Decision Flowchart](#decision-flowchart)

---

## Overview

The English Nations Hub repository organizes all lead intelligence geographically, using a **four-level geographic hierarchy** as its structural backbone. This hierarchy spans 15 English-speaking nations across 2,700+ directories and is designed to make every lead discoverable, browsable, and actionable at a local level.

The four levels are:

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| **1** | Country | The sovereign nation | `Nigeria` |
| **2** | State / Region / Province | The primary administrative division within the country | `Lagos` |
| **3** | City | The primary urban center or municipality | `Lagos` (city) |
| **4** | City Area | The neighborhood, suburb, district, or borough within a city | `Victoria-Island` |

Real-world lead data is rarely perfectly precise. Online business profiles, social media listings, directory entries, and website contact pages frequently provide incomplete, ambiguous, or partially specified geographic information. A business might list "Greater London" without specifying a borough; a professional on LinkedIn might list only "Ghana" as their location; a freelancer might describe themselves as "remote" without a fixed office. This document defines **exactly how agents should handle every geographic scenario** — ensuring no lead is ever discarded due to incomplete location data, and that every record is placed at the most specific level of the hierarchy that can be confidently determined.

---

## The Hierarchy

### Level 1 — Country

The country is the top-level geographic container within the `countries/` directory. Each country folder represents a sovereign English-speaking nation included in the repository. Currently 15 countries are covered: United States, Canada, United Kingdom, Ireland, Nigeria, Ghana, South Africa, Australia, New Zealand, Jamaica, Trinidad and Tobago, Barbados, Bahamas, Belize, and Guyana.

**Folder path example:**
```
countries/Nigeria/
```

**Naming convention:** Full country name in Title-Case, spaces replaced with hyphens. Examples: `United-States-of-America/`, `United-Kingdom/`, `South-Africa/`.

### Level 2 — State / Region / Province

The second level represents the primary administrative division within each country. The terminology varies by country — "States" in the USA and Nigeria, "Provinces" in Canada and South Africa, "Regions" in Ghana, "Counties" in Ireland, "Nations" in the UK (England, Scotland, Wales, Northern Ireland), and "Parishes" in Jamaica.

**Folder path example:**
```
countries/Nigeria/Lagos/
countries/United-States-of-America/California/
countries/Ghana/Greater-Accra/
countries/United-Kingdom/England/
```

**Naming convention:** Title-Case with hyphens for multi-word names. Examples: `New-York/`, `Greater-London/`, `FCT-Abuja/`.

### Level 3 — City

The third level represents a specific city, town, or major urban center within a state or region. Not every city in a country is included — only those that are economically significant or that have sufficient lead density to warrant their own folder.

**Folder path example:**
```
countries/Nigeria/Lagos/Lagos/
countries/United-States-of-America/California/Los-Angeles/
countries/Ghana/Greater-Accra/Accra/
countries/United-Kingdom/England/London/
```

### Level 4 — City Area

The fourth and deepest level represents neighborhoods, suburbs, boroughs, districts, or zones within a city. This is where leads are ideally placed — at the most granular geographic level possible.

**Folder path example:**
```
countries/Nigeria/Lagos/Lagos/Victoria-Island/
countries/United-States-of-America/California/Los-Angeles/Hollywood/
countries/Ghana/Greater-Accra/Accra/East-Legon/
```

**Naming convention:** Title-Case with hyphens. Examples: `Beverly-Hills/`, `Ikoyi/`, `Sandton/`.

### How the Folder Structure Maps to Real Geography

The repository's physical folder structure (`countries/{Country}/{State}/{City}/{City-Area}/`) directly mirrors real-world administrative geography. When an agent reads a lead's address — for example, "45 Ozumba Mbadiwe Ave, Victoria Island, Lagos, Nigeria" — the agent should decompose it into:

- **Country:** Nigeria
- **State:** Lagos
- **City:** Lagos
- **City Area:** Victoria Island

And place the lead at:
```
countries/Nigeria/Lagos/Lagos/Victoria-Island/
```

When any level is missing from the source data, the agent follows the fallback strategy described below.

---

## The Golden Rule

> **Leads must NEVER be discarded due to incomplete geographic precision. Instead, intelligently categorize them for later refinement.**

This is the single most important principle governing geographic handling. A lead that specifies only a country is still a valuable lead. A lead whose location is ambiguous or uncertain still has potential value. The repository's fallback folder system exists specifically to capture these leads at the highest level of geographic certainty available, so they can be refined and relocated as more information becomes available.

The cost of storing an imprecisely placed lead is negligible. The cost of permanently losing a potentially valuable contact is incalculable. **When in doubt, always store.**

---

## Incomplete Data Scenarios & Solutions

Below are ten distinct geographic scenarios that agents will encounter, along with the precise handling strategy for each.

### Scenario 1: Full Precision — City Area Known

**Description:** The lead's source data includes a specific city area, neighborhood, suburb, or district that maps cleanly to an existing City Area folder in the repository.

**Action:** Place the lead directly into the matching City Area folder under the appropriate lead category (`GMB_Leads/`, `LinkedIn_Public_Leads/`, or `Other_Public_Web_Leads/`).

**Example:**
- Source data: `"123 Main St, East Legon, Accra, Ghana"`
- Placement: `countries/Ghana/Greater-Accra/Accra/East-Legon/`

**Geographic Precision Level:** Exact

---

### Scenario 2: City Known, Area Unknown

**Description:** The lead specifies a city but no specific neighborhood, suburb, or district within that city. This is extremely common on LinkedIn profiles and many business directories where only the city-level location is listed.

**Action:** Place the lead in the `City_General/` fallback folder at the city level. If this folder does not yet exist, the agent is authorized to create it following the standard fallback folder structure (see [Fallback Folder Creation Rules](#fallback-folder-creation-rules)).

**Example:**
- Source data: `"Accra, Ghana"` (no area specified)
- Placement: `countries/Ghana/Greater-Accra/Accra/Accra_General/`

**Example:**
- Source data: `"London, United Kingdom"`
- Placement: `countries/United-Kingdom/England/London/London_General/`

**Geographic Precision Level:** Partial

---

### Scenario 3: State/Region Known, City Unknown

**Description:** The lead specifies a state, province, or region but no city. This commonly occurs for professionals who list their state on LinkedIn, service-area businesses that cover an entire state, or directory listings that only include state-level information.

**Action:** Place the lead in the `State_General_Leads/` fallback folder at the state level.

**Example:**
- Source data: `"Lagos State"` or `"Lagos, Nigeria"` where it is unclear whether Lagos refers to the city or the state
- Placement: `countries/Nigeria/Lagos/State_General_Leads/`

**Example:**
- Source data: `"Texas, USA"` (no city)
- Placement: `countries/United-States-of-America/Texas/State_General_Leads/`

**Geographic Precision Level:** General

---

### Scenario 4: Country Only

**Description:** The lead specifies only a country with no sub-national geographic detail whatsoever. This is common for remote workers, newly registered businesses, social media profiles with minimal detail, or businesses whose website lacks an address.

**Action:** Place the lead in the `Country_General_Leads/` fallback folder at the country level.

**Example:**
- Source data: `"Ghana"` (no city, region, or area)
- Placement: `countries/Ghana/Country_General_Leads/`

**Example:**
- Source data: `"Australia"` (no state or city)
- Placement: `countries/Australia/Country_General_Leads/`

**Geographic Precision Level:** General

---

### Scenario 5: Metropolitan Area Reference

**Description:** The lead references a metropolitan area, greater urban zone, or regional designation that encompasses multiple cities or boroughs without specifying one. Examples include "Greater London," "Greater Accra," "Metro Manila" (outside scope), "Dallas–Fort Worth," or "Research Triangle."

**Action:** Place the lead in the `City_General/` folder of the **primary or largest city** within that metropolitan area. Add a metadata note indicating the metropolitan area reference so the lead can be reviewed and potentially re-routed later.

**Example:**
- Source data: `"Greater Accra"` or `"Accra Metropolitan Area"`
- Placement: `countries/Ghana/Greater-Accra/Accra/Accra_General/`
- Note: `"Lead references Greater Accra metro area; placed in Accra General for review."`

**Example:**
- Source data: `"Greater London"`
- Placement: `countries/United-Kingdom/England/London/London_General/`
- Note: `"Lead references Greater London; borough unknown."`

**Geographic Precision Level:** Partial

---

### Scenario 6: Remote Worker / No Fixed Location

**Description:** The lead is a freelancer, remote worker, digital nomad, or service provider with no fixed physical office location. They may list "Remote," "Work from anywhere," or provide no address at all. In some cases, they may mention a timezone, home country, or general region as context.

**Action:** Apply the following priority logic:

1. **If a specific country is mentioned** (even as "based in [country]") → place in `Country_General_Leads/`.
2. **If a timezone or general region is mentioned** (e.g., "GMT+1," "West Africa") → use best judgment to infer the most likely country and place in `Country_General_Leads/`.
3. **If no geographic clue exists at all** → place in a `Location_Uncertain/` subfolder within the most relevant country, or in a general uncategorized folder at the repository root.

**Always tag the record with `"Remote"`** in the geographic precision field.

**Example:**
- Source data: `"Remote — based in Jamaica"` with timezone `"EST (UTC-5)"`
- Placement: `countries/Jamaica/Country_General_Leads/`
- Tag: `"Remote"`

**Example:**
- Source data: `"Digital nomad, currently in West Africa"`
- Placement: `countries/Nigeria/Country_General_Leads/` (or the most relevant West African country in the repo)
- Tag: `"Remote"`, `"Location_Uncertain"`

**Geographic Precision Level:** Uncertain

---

### Scenario 7: Multi-Location Business

**Description:** The lead is a business that operates from multiple physical locations across different cities, states, or even countries. Examples include chain restaurants, franchise operations, logistics companies with multiple depots, law firms with branch offices, or consulting firms serving multiple regions.

**Action:**

1. **Create a primary record** in the City Area folder corresponding to the business's **headquarters or primary registered address**.
2. **Add a `"Multi-Location"` flag** to the lead's metadata, along with a comma-separated list of all known locations.
3. **Optionally create copies** of the lead record in each additional relevant City Area folder where the business has a verifiable physical presence. Each copy should include a note: `"This business also operates in: [list of other locations]. Primary record located at: [path]."`
4. **Do NOT create copies at State_General_Leads/ or Country_General_Leads/ level** — the headquarters record is sufficient for general-level access.

**Example:**
- Source data: `"Zenith Bank — branches in Victoria Island, Ikeja, Marina, and 300+ locations nationwide"`
- Primary placement: `countries/Nigeria/Lagos/Lagos/Victoria-Island/` (headquarters)
- Flag: `"Multi-Location"`
- Note: `"Also operates in: Ikeja, Marina, and nationwide. 300+ branches."`

**Geographic Precision Level:** Exact (for primary), Partial (for copies)

---

### Scenario 8: Neighboring City Area

**Description:** The lead references a city area or neighborhood that does not have its own folder in the repository but is geographically proximate to an existing City Area. This often occurs with informal neighborhood names, newly developed areas, spelling variations, or suburbs that fall within the catchment area of a listed district.

**Action:**

1. **Place the lead in the closest geographically matching City Area folder.**
2. **Add a `"Nearby"` note** in the lead's metadata indicating the original location text and the folder it was placed in. Example: `"Listed as 'Ajah'; placed in Lekki (nearest matching area)."`
3. **If multiple neighboring areas could be valid**, place in the City Area that shares the same postal code, local government area, or administrative boundary.
4. **Do not create a new City Area folder** without explicit justification — instead, log the unrecognized area name in the City_General/ folder's README for future folder creation consideration.

**Example:**
- Source data: `"Ajah, Lagos"` (no Ajah folder exists, but Lekki is nearby and in the same Eti-Osa LGA)
- Placement: `countries/Nigeria/Lagos/Lagos/Lekki/`
- Note: `"Nearby — listed as Ajah; placed in Lekki (same Eti-Osa LGA). Review for folder creation."`

**Geographic Precision Level:** Partial

---

### Scenario 9: Ambiguous Location

**Description:** The lead provides location information that is genuinely ambiguous and cannot be resolved to any single geographic level with confidence. Examples include conflicting address fields, a city name that exists in multiple states, a region name that spans multiple countries, or a location written in a non-standard format that defies parsing.

**Action:**

1. **Preserve ALL available location clues** in the lead record's metadata — do not discard any location text.
2. **Place the lead in a `Location_Uncertain/` subfolder** within the most plausible geographic container (country, state, or city level).
3. **Include a detailed note** explaining why the location is ambiguous and what the possible resolutions are.
4. **Flag the record** for periodic review as the repository's geographic coverage expands.

**Example:**
- Source data: `"Springfield, USA"` (there are over 40 cities named Springfield in the US)
- Placement: `countries/United-States-of-America/Country_General_Leads/Location_Uncertain/`
- Note: `"Ambiguous — 'Springfield' exists in 40+ US states. Additional context needed: state, zip code, or area code."`

**Example:**
- Source data: `"Greater Manchester"` (could be the metropolitan county or the city of Manchester itself)
- Placement: `countries/United-Kingdom/England/Greater-Manchester/Manchester/Manchester_General/`
- Note: `"Ambiguous — 'Greater Manchester' could refer to the metro county or the city. Placed in Manchester General for review."`

**Geographic Precision Level:** Uncertain

---

### Scenario 10: Country Not in Repository

**Description:** The lead is associated with a country that does not yet have a folder in the repository. This may occur for leads discovered in English-speaking professionals or businesses located in countries not currently covered (e.g., Singapore, Kenya, India, Philippines).

**Action:**

1. **Create a new country folder** at the `countries/` level following the existing naming convention: full country name, Title-Case, hyphens for spaces. Example: `countries/Kenya/`.
2. **Create the standard fallback folder** `Country_General_Leads/` within the new country folder, including all three lead category sub-folders (`GMB_Leads/`, `LinkedIn_Public_Leads/`, `Other_Public_Web_Leads/`).
3. **Document the addition** in the repository's progress tracker with the country name, date added, and a brief justification.
4. **Place the lead** in the newly created `Country_General_Leads/` folder.

**Example:**
- Source data: `"Nairobi, Kenya"`
- New folder created: `countries/Kenya/`
- Placement: `countries/Kenya/Country_General_Leads/`
- Tracker entry: `"2025-06-15: Added Kenya — lead discovered with no existing country folder."`

**Geographic Precision Level:** General

---

## Fallback Folder Creation Rules

Agents are **explicitly authorized** to create fallback folders at any level of the hierarchy when leads cannot be placed into existing City Area folders. The following rules govern fallback folder creation:

### Naming Conventions

| Fallback Level | Folder Name | Created At |
|----------------|-------------|------------|
| City level | `City_General/` | Inside the specific city folder |
| State/Region level | `State_General_Leads/` | Inside the specific state folder |
| Country level | `Country_General_Leads/` | Inside the specific country folder |
| Uncertain location | `Location_Uncertain/` | Inside any relevant geographic container |

### Required Structure

Every fallback folder must contain the **three standard lead category sub-folders**, even if they are initially empty:

```
City_General/              (or State_General_Leads/, etc.)
├── GMB_Leads/
├── LinkedIn_Public_Leads/
└── Other_Public_Web_Leads/
```

### README Requirement

Every fallback folder **must include a README.md** explaining its purpose:

```markdown
# [City/State/Country]_General — Fallback Folder

## Purpose
This folder contains leads whose geographic placement could not be
resolved to a specific [city area / city / state] within [location].

Leads placed here have a Geographic Precision Level of "Partial,"
"General," or "Uncertain" and should be reviewed for refinement as
more information becomes available.

## Review Priority
- **High:** Leads with partial addresses that could be geocoded
- **Medium:** Leads with only city-level precision
- **Low:** Leads with country-level precision only
```

### Do NOT Create Fallback Folders Unnecessarily

Fallback folders should only be created when there is an actual lead to place inside them. Do not pre-create empty fallback folders across the entire repository — this would add thousands of empty directories with no data value. Instead, create them **on demand** as leads are discovered that require them.

---

## Geographic Data Fields

Every lead record in the repository — regardless of its source category — must include the following geographic metadata fields:

| Field | Required | Description | Example Values |
|-------|----------|-------------|----------------|
| **Country** | Yes (mandatory) | The country where the lead is located or based | `"Nigeria"`, `"United States"`, `"Ghana"` |
| **State/Region** | If known | The state, province, region, or equivalent | `"Lagos"`, `"California"`, `"Greater Accra"` |
| **City** | If known | The city, town, or municipality | `"Lagos"`, `"Los Angeles"`, `"Accra"` |
| **City Area** | If known | The neighborhood, suburb, district, or borough | `"Victoria Island"`, `"Hollywood"`, `"East Legon"` |
| **Geographic Precision Level** | Yes (mandatory) | How precise the geographic placement is | `Exact`, `Partial`, `General`, `Uncertain` |
| **Location Notes** | If applicable | Free-text notes about location ambiguity or multi-location status | `"Multi-Location"`, `"Remote"`, `"Nearby — listed as Ajah"` |

### Precision Level Definitions

| Level | Definition | Example |
|-------|-----------|---------|
| **Exact** | Lead is placed in a specific City Area folder with a verified address | `"123 Main St, East Legon, Accra"` |
| **Partial** | Lead is placed at city level or references a metropolitan area | `"Accra, Ghana"`, `"Greater London"` |
| **General** | Lead is placed at state or country level only | `"Texas, USA"`, `"Ghana"` |
| **Uncertain** | Lead's location is ambiguous, conflicting, or unresolved | `"Springfield, USA"`, `"Remote"` |

---

## Country-Specific Notes

Different countries use different administrative divisions, naming conventions, and address formats. Below are geographic handling notes for the key countries in the repository:

### United States of America

| Level | US Terminology | Examples |
|-------|---------------|---------|
| 2 | State | `California`, `Texas`, `New-York` |
| 3 | City | `Los-Angeles`, `Houston`, `Chicago` |
| 4 | Neighborhood / Borough / District | `Hollywood`, `Manhattan`, `Brooklyn` |

**Notes:**
- The US has 50 states plus Washington D.C. (treated as a state-level entry).
- US addresses often include zip codes — use zip codes to disambiguate when a city name exists in multiple states.
- Boroughs of New York City (Manhattan, Brooklyn, Queens, Bronx, Staten Island) are treated as City Areas within the `New-York` city folder.
- Counties are NOT used as a hierarchy level in this repository — they are skipped in favor of State → City → Area.

### United Kingdom

| Level | UK Terminology | Examples |
|-------|---------------|---------|
| 2 | Nation (Country) | `England`, `Scotland`, `Wales`, `Northern-Ireland` |
| 3 | City / County | `London`, `Manchester`, `Birmingham` |
| 4 | Borough / District / Area | `Westminster`, `Camden`, `City-Centre` |

**Notes:**
- The UK's Level 2 uses the four constituent nations rather than traditional counties.
- London boroughs (Westminster, Camden, Kensington, etc.) are treated as City Areas.
- Postal code areas (e.g., "SW1A") can help disambiguate borough placement but are not used as folder names.

### Nigeria

| Level | Nigerian Terminology | Examples |
|-------|---------------------|---------|
| 2 | State (including FCT) | `Lagos`, `FCT-Abuja`, `Rivers` |
| 3 | City | `Lagos`, `Abuja`, `Port-Harcourt` |
| 4 | Area / Neighborhood | `Victoria-Island`, `Ikoyi`, `Maitama` |

**Notes:**
- Nigeria has 36 states plus the Federal Capital Territory (Abuja), treated as a state-level entry.
- LGAs (Local Government Areas) are NOT used as a hierarchy level — they are useful for disambiguation notes but not for folder creation.
- Lagos State and Lagos City share the same name — the city folder is nested inside the state folder.

### Ghana

| Level | Ghanaian Terminology | Examples |
|-------|---------------------|---------|
| 2 | Region | `Greater-Accra`, `Ashanti`, `Western` |
| 3 | City | `Accra`, `Kumasi`, `Takoradi` |
| 4 | Area / Suburb | `East-Legon`, `Osu`, `Cantonments` |

**Notes:**
- Ghana reorganized its administrative regions from 10 to 16 in 2019. The repository uses the current 16-region structure.
- Districts and municipalities are NOT used as a hierarchy level.

### Canada

| Level | Canadian Terminology | Examples |
|-------|---------------------|---------|
| 2 | Province / Territory | `Ontario`, `British-Columbia`, `Alberta` |
| 3 | City | `Toronto`, `Vancouver`, `Calgary` |
| 4 | Neighborhood / Borough | `Downtown`, `North-York`, `Kitsilano` |

**Notes:**
- Canada has 10 provinces and 3 territories. All are treated equally at Level 2.
- Quebec is included despite being predominantly French-speaking, as it contains significant English-speaking populations and bilingual businesses.

### Australia

| Level | Australian Terminology | Examples |
|-------|----------------------|---------|
| 2 | State / Territory | `New-South-Wales`, `Victoria`, `Queensland` |
| 3 | City | `Sydney`, `Melbourne`, `Brisbane` |
| 4 | Suburb | `Bondi`, `Parramatta`, `St-Kilda` |

**Notes:**
- Australia has 6 states and 2 territories (ACT and Northern Territory).
- Australian "suburbs" function as the equivalent of City Areas — they are the primary sub-city geographic unit.

### South Africa

| Level | South African Terminology | Examples |
|-------|--------------------------|---------|
| 2 | Province | `Gauteng`, `Western-Cape`, `KwaZulu-Natal` |
| 3 | City | `Johannesburg`, `Cape-Town`, `Durban` |
| 4 | Suburb / Area | `Sandton`, `Rosebank`, `City-Bowl` |

**Notes:**
- South Africa has 9 provinces.
- Metropolitan municipalities (e.g., City of Johannesburg Metro) are not used as separate hierarchy levels.

### New Zealand

| Level | NZ Terminology | Examples |
|-------|---------------|---------|
| 2 | Region | `Auckland`, `Wellington`, `Canterbury` |
| 3 | City | `Auckland-City`, `Wellington-City`, `Christchurch` |
| 4 | Suburb | `CBD`, `Ponsonby`, `Newtown` |

**Notes:**
- New Zealand has 16 regions.
- Special characters in Maori place names should be converted to ASCII (e.g., `Whangarei` instead of `Whangarei` with macron).

### Ireland

| Level | Irish Terminology | Examples |
|-------|------------------|---------|
| 2 | County | `Dublin`, `Cork`, `Galway` |
| 3 | City | `Dublin-City`, `Cork-City` |
| 4 | Area | `City-Centre`, `Temple-Bar`, `Ballsbridge` |

**Notes:**
- Ireland has 26 counties (Republic of Ireland only; Northern Ireland is part of the UK).
- Dublin postal districts (Dublin 1, Dublin 2, etc.) can inform area-level placement but are not used as folder names.

### Jamaica

| Level | Jamaican Terminology | Examples |
|-------|-------------------|---------|
| 2 | Parish | `Kingston`, `St-Andrew`, `St-James` |
| 3 | City | `Kingston`, `Montego-Bay` |
| 4 | Area / Neighborhood | `New-Kingston`, `Half-Way-Tree` |

**Notes:**
- Jamaica has 14 parishes, which function as the equivalent of states/provinces.
- The Kingston Metropolitan Area spans Kingston and St. Andrew parishes — use best judgment for placement.

---

## Decision Flowchart

The following text-based decision tree should be followed by agents when determining where to place a lead. Start at the top and follow the appropriate path based on the information available in the lead's source data.

```
START: Analyze the lead's available location information
│
├── Q1: Is the COUNTRY known or inferable?
│   ├── NO → Place in a general uncategorized/miscellaneous folder
│   │         at the repository root. Tag as "Location_Uncertain."
│   │         Flag for human review.
│   │
│   └── YES → Navigate to the country folder.
│            │
│            ├── Q2: Is the STATE/REGION/PROVINCE known?
│            │   ├── NO → Place in Country_General_Leads/
│            │   │         Tag precision as "General."
│            │   │
│            │   └── YES → Navigate to the state folder.
│            │            │
│            │            ├── Q3: Is the CITY known?
│            │            │   ├── NO → Place in State_General_Leads/
│            │            │   │         Tag precision as "General."
│            │            │   │
│            │            │   └── YES → Navigate to the city folder.
│            │            │            │
│            │            │            ├── Q4: Is the CITY AREA (neighborhood,
│            │            │            │         suburb, district) known?
│            │            │            │   ├── YES and folder EXISTS
│            │            │            │   │   → Place in the City Area folder.
│            │            │            │   │     Tag precision as "Exact."
│            │            │            │   │     DONE.
│            │            │            │   │
│            │            │            │   ├── YES but folder DOES NOT exist
│            │            │            │   │   → Place in nearest neighboring
│            │            │            │   │     City Area folder with "Nearby" note.
│            │            │            │   │   Tag precision as "Partial."
│            │            │            │   │     Log unrecognized area in City_General/ README.
│            │            │            │   │     DONE.
│            │            │            │   │
│            │            │            │   └── NO → Is this a METROPOLITAN AREA
│            │            │            │           reference (e.g., "Greater London")?
│            │            │            │       ├── YES → Place in City_General/ of the
│            │            │            │       │         primary city. Tag as "Partial."
│            │            │            │       │         DONE.
│            │            │            │       │
│            │            │            │       └── NO → Is this a REMOTE worker or
│            │            │            │                 no-fixed-location lead?
│            │            │            │           ├── YES → Place in Country_General_Leads/
│            │            │            │           │         with "Remote" tag.
│            │            │            │           │         Tag precision as "Uncertain."
│            │            │            │           │         DONE.
│            │            │            │           │
│            │            │            │           └── NO → Place in City_General/.
│            │            │            │                   Tag precision as "Partial."
│            │            │            │                   DONE.
│            │            │
│            │            └── (end of city-level path)
│            │
│            └── (end of state-level path)
│
└── (end of country-level path)
```

### Quick Reference Summary Table

| What You Know | Where It Goes | Precision Tag |
|---------------|--------------|---------------|
| Country + State + City + Area (folder exists) | `countries/{C}/{S}/{City}/{Area}/` | Exact |
| Country + State + City + Area (no folder) | `countries/{C}/{S}/{City}/{Nearest-Area}/` + Nearby note | Partial |
| Country + State + City | `countries/{C}/{S}/{City}/City_General/` | Partial |
| Country + State + Metro reference | `countries/{C}/{S}/{Primary-City}/City_General/` | Partial |
| Country + State | `countries/{C}/{S}/State_General_Leads/` | General |
| Country only (or Remote) | `countries/{C}/Country_General_Leads/` | General / Uncertain |
| Nothing useful | Uncategorized/miscellaneous folder | Uncertain |
| Country not in repo | Create `countries/{C}/Country_General_Leads/` + log it | General |

---

*This document is a living reference and should be updated as the repository's geographic coverage expands, new edge cases are encountered, and the agent framework evolves. For questions not covered by this document, agents should apply the Golden Rule: preserve the lead, place it at the highest level of certainty available, and flag it for review.*
