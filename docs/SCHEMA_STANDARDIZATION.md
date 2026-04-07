# CSV Schema Standardization Report

> **Date:** 2025  
> **Scope:** All CSV lead data files across 7 areas in Ghana and Nigeria  
> **Status:** Documentation only — no CSV files were modified.

---

## 1. Summary of Inconsistencies

There are **4 file types** with CSV data across the project. Every file type has **multiple competing schemas** due to different naming conventions (Title Case vs snake_case) and different column sets being collected over time.

| File Type | Files Found | Distinct Schemas |
|---|---|---|
| GMB Raw Leads (`raw_leads.csv`) | 7 | 2 |
| GMB Enriched Leads (`enriched_leads.csv`) | 5 | 5 |
| LinkedIn Raw Leads | 7 | 3 |
| Other Public Web Raw Leads | 4 | 2 |

**Total distinct schemas: 12 across 23 CSV files.**

---

## 2. Current Schemas by File Type

### 2A. GMB Raw Leads (`raw_leads.csv`)

#### Schema GMB-Raw-A — "Title Case" (4 files)

Used by: Ghana/Cantonments, Nigeria/Ikeja, Nigeria/Lekki, Nigeria/Victoria-Island

```
Business Name, Business Niche, Address, City Area, Phone Number,
WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL,
Date Collected
```
**Columns (10):** Business Name, Business Niche, Address, City Area, Phone Number, WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL, Date Collected

#### Schema GMB-Raw-B — "snake_case" (3 files)

Used by: Ghana/Airport-Residential, Ghana/East-Legon, Ghana/Osu

```
business_name, niche, address, phone, whatsapp, website,
email, source_url, date_collected
```
**Columns (9):** business_name, niche, address, phone, whatsapp, website, email, source_url, date_collected

#### Differences

| Aspect | GMB-Raw-A | GMB-Raw-B |
|---|---|---|
| Naming convention | Title Case | snake_case |
| Column count | 10 | 9 |
| Has `email` | No | Yes |
| Has `source_url` | No (has `Google Maps Listing URL`) | Yes |
| Has `Social Media Links` | Yes | No |
| Has `City Area` | Yes | No |
| Has `Phone Number` | Yes (`Phone Number`) | Yes (`phone`) |

---

### 2B. GMB Enriched Leads (`enriched_leads.csv`)

#### Schema GMB-Enriched-A — Cantonments GH (16 cols)

```
Business Name, Business Niche, Address, City Area, Phone Number,
WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL,
Email Address, Additional Phone Numbers, Website Verified, Social Profiles,
Email Validation Status, Date Enriched, Source URLs, Date Collected
```

#### Schema GMB-Enriched-B — East-Legon GH (11 cols)

```
business_name, niche, address, phone, whatsapp, website, email,
social_profiles, email_validation_status, date_enriched, source_urls
```

#### Schema GMB-Enriched-C — Ikeja NG (18 cols)

```
Business Name, Business Niche, Address, City Area, Phone Number,
WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL,
Email Address, WhatsApp, Additional Phone Numbers, Website (Verified),
Social Profiles, Email Validation Status, Date Enriched, Source URLs
```
**Note:** Duplicate `WhatsApp` column (also has `WhatsApp Contact`). Missing `Date Collected`.

#### Schema GMB-Enriched-D — Lekki NG (18 cols)

```
Business Name, Business Niche, Address, City Area, Phone Number,
WhatsApp Contact, Website, Social Media Links, Google Maps Listing URL,
Date Collected, Email Address, WhatsApp, Additional Phone Numbers,
Website (Verified), Social Profiles, Email Validation Status, Date Enriched,
Source URLs
```
**Note:** Same duplicate `WhatsApp` column as Ikeja. `Date Collected` appears mid-schema.

#### Schema GMB-Enriched-E — Victoria-Island NG (18 cols)

Identical to Schema GMB-Enriched-D (Lekki).

#### Key Differences

| Aspect | Cantonments | East-Legon | Ikeja | Lekki / VI |
|---|---|---|---|---|
| Naming convention | Title Case | snake_case | Title Case | Title Case |
| Column count | 16 | 11 | 18 | 18 |
| Has `Date Collected` | Yes (end) | No | No | Yes (mid-schema) |
| Has `Google Maps URL` | Yes | No | Yes | Yes |
| Has `City Area` | Yes | No | Yes | Yes |
| Duplicate `WhatsApp` | No | No | Yes | Yes |
| Has `Website Verified` | Yes | No | Yes (parentheses) | Yes (parentheses) |

---

### 2C. LinkedIn Raw Leads

#### Schema LinkedIn-A — "Full Profile" (4 files)

Used by: Ghana/Cantonments, Nigeria/Ikeja, Nigeria/Lekki, Nigeria/Victoria-Island

```
Full Name, Skill/Profession, LinkedIn Profile URL, Email Address,
Phone/WhatsApp, Company/Business, Location Listed, Email Validation Status,
Date Collected
```
**Columns (9)**

#### Schema LinkedIn-B — "Detailed" (1 file)

Used by: Ghana/Airport-Residential

```
lead_type, name, job_title, company_name, industry, linkedin_url,
website, address, phone, email, employee_range, location, description,
date_collected, source
```
**Columns (15)**

#### Schema LinkedIn-C — "Minimal" (1 file)

Used by: Ghana/Osu

```
type, name, industry, linkedin_url, description, date_collected, source
```
**Columns (7)**

#### Key Differences

| Aspect | LinkedIn-A | LinkedIn-B | LinkedIn-C |
|---|---|---|---|
| Naming convention | Title Case + slashes | snake_case | snake_case |
| Column count | 9 | 15 | 7 |
| Has `email` | Yes | Yes | No |
| Has `linkedin_url` | Yes (`LinkedIn Profile URL`) | Yes | Yes |
| Has `phone` | Yes (`Phone/WhatsApp`) | Yes | No |
| Has `job_title` | No (has `Skill/Profession`) | Yes | No |
| Has `employee_range` | No | Yes | No |
| Has `website` | No | Yes | No |
| Has `Email Validation Status` | Yes | No | No |

---

### 2D. Other Public Web Raw Leads

#### Schema Web-A — "Profile Style" (2 files)

Used by: Ghana/Cantonments, Nigeria/Ikeja

```
Name/Business Name, Skill/Industry, Email, Phone/WhatsApp,
Website/Portfolio, Location, Source URL, Source Type,
Email Validation Status, Date Collected
```
**Columns (10)**

#### Schema Web-B — "Business Directory Style" (2 files)

Used by: Ghana/Osu, Ghana/Airport-Residential

```
business_name, category, niche, address, city, phone, phone_2,
website, email, whatsapp, social_media, contact_person,
date_collected, source, source_url
```
**Columns (15)**

#### Key Differences

| Aspect | Web-A | Web-B |
|---|---|---|
| Naming convention | Title Case + slashes | snake_case |
| Column count | 10 | 15 |
| Has `category` | No | Yes |
| Has `niche` | No (has `Skill/Industry`) | Yes |
| Has `phone_2` | No | Yes |
| Has `social_media` | No | Yes |
| Has `contact_person` | No | Yes |
| Has `Email Validation Status` | Yes | No |
| Has `Source Type` | Yes | No (has `source`) |

---

## 3. Recommended Standard Schemas

### 3A. Standard GMB Raw Leads Schema (11 columns)

```csv
business_name,business_niche,address,city_area,phone_number,whatsapp,website,social_media_links,google_maps_url,email,date_collected
```

**Rationale:**
- All-lowercase snake_case for programmatic consistency
- Combines the best of both existing schemas
- Adds `email` (present in Schema B, missing from A)
- Retains `city_area`, `social_media_links`, `google_maps_url` (present in A, missing from B)
- Replaces `source_url` with `google_maps_url` since GMB leads primarily come from Google Maps

### 3B. Standard GMB Enriched Leads Schema (18 columns)

```csv
business_name,business_niche,address,city_area,phone_number,whatsapp,website,social_media_links,google_maps_url,email,additional_phones,website_verified,social_profiles,email_validation_status,date_enriched,source_urls,date_collected
```

**Rationale:**
- Extends the raw schema with enrichment-specific columns
- Removes the duplicate `WhatsApp` column (bug in Ikeja/Lekki/VI)
- Consistent column ordering: core fields → enrichment fields → dates
- `Date Collected` at end (not mid-schema as in Lekki/VI)
- Uses `website_verified` without parentheses (not `Website (Verified)`)

### 3C. Standard LinkedIn Raw Leads Schema (12 columns)

```csv
full_name,skill_profession,job_title,company_name,industry,linkedin_url,email,phone_whatsapp,location,employee_range,description,date_collected
```

**Rationale:**
- Merges the most useful fields from all three existing schemas
- Includes `employee_range` and `job_title` from Schema B (valuable enrichment data)
- Includes `email` and `phone` from Schema A
- Includes `description` from Schemas B and C
- Uses underscored names without slashes (not `Skill/Profession`)
- Does NOT include `Email Validation Status` at raw stage (move to enrichment)
- Does NOT include `source` (implicit from file location)

### 3D. Standard Other Web Raw Leads Schema (14 columns)

```csv
business_name,category,niche,address,city,phone,phone_2,website,email,whatsapp,social_media,contact_person,source_url,date_collected
```

**Rationale:**
- Based on Web-B schema which is more comprehensive
- Uses consistent naming with GMB schemas where columns overlap
- Includes `contact_person` (unique to Web-B, valuable data)
- Includes `category` and `niche` separately (different granularity)
- `source_url` is sufficient (no need for separate `source` and `Source Type` at raw stage)

---

## 4. Changes Required by Area

### Ghana — Cantonments

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-A | Std GMB Raw | Rename 10 cols to snake_case; add `email` col (empty) |
| GMB Enriched | GMB-Enriched-A | Std GMB Enriched | Rename cols to snake_case; remove `Website Verified` → `website_verified`; reorder dates |
| LinkedIn Raw | LinkedIn-A | Std LinkedIn | Rename cols; add `job_title`, `company_name`, `industry`, `employee_range`, `description` cols (empty) |
| Web Raw | Web-A | Std Web | Rename cols; add `category`, `niche`, `address`, `city`, `phone_2`, `social_media`, `contact_person` cols (empty); remove `Source Type` |

### Ghana — Airport-Residential

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-B | Std GMB Raw | Rename cols; add `city_area`, `social_media_links`, `google_maps_url` cols (empty); rename `source_url` → `google_maps_url` |
| GMB Enriched | _(none)_ | Std GMB Enriched | Create file when enrichment is done |
| LinkedIn Raw | LinkedIn-B | Std LinkedIn | Reorder cols; rename `company_name`→keep, add `full_name`; remove `website`, `address` (non-LinkedIn); remove `source` |
| Web Raw | Web-B | Std Web | Minimal changes — already close to standard |

### Ghana — East-Legon

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-B | Std GMB Raw | Rename cols; add `city_area`, `social_media_links`, `google_maps_url` cols (empty) |
| GMB Enriched | GMB-Enriched-B | Std GMB Enriched | Major expansion: rename cols + add 7 missing cols (`city_area`, `phone_number`→`phone`, `whatsapp`, `social_media_links`, `google_maps_url`, `additional_phones`, `website_verified`, `date_collected`) |
| LinkedIn Raw | _(none)_ | Std LinkedIn | Create file when collection is done |
| Web Raw | _(none)_ | Std Web | Create file when collection is done |

### Ghana — Osu

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-B | Std GMB Raw | Rename cols; add `city_area`, `social_media_links`, `google_maps_url` cols (empty) |
| GMB Enriched | _(none)_ | Std GMB Enriched | Create file when enrichment is done |
| LinkedIn Raw | LinkedIn-C | Std LinkedIn | Major expansion: add 5 missing cols (`full_name`, `skill_profession`, `job_title`, `company_name`, `email`, `phone_whatsapp`, `location`, `employee_range`) |
| Web Raw | Web-B | Std Web | Minimal changes — already close to standard |

### Nigeria — Ikeja

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-A | Std GMB Raw | Rename 10 cols to snake_case; add `email` col (empty) |
| GMB Enriched | GMB-Enriched-C | Std GMB Enriched | Rename cols; remove duplicate `WhatsApp`; add `date_collected` |
| LinkedIn Raw | LinkedIn-A | Std LinkedIn | Rename cols; add `job_title`, `company_name`, `industry`, `employee_range`, `description` cols (empty) |
| Web Raw | Web-A | Std Web | Rename cols; add 7 missing cols; remove `Source Type` |

### Nigeria — Lekki

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-A | Std GMB Raw | Rename 10 cols to snake_case; add `email` col (empty) |
| GMB Enriched | GMB-Enriched-D | Std GMB Enriched | Rename cols; remove duplicate `WhatsApp`; move `Date Collected` to end |
| LinkedIn Raw | LinkedIn-A | Std LinkedIn | Rename cols; add `job_title`, `company_name`, `industry`, `employee_range`, `description` cols (empty) |
| Web Raw | _(none)_ | Std Web | Create file when collection is done |

### Nigeria — Victoria-Island

| File | Current Schema | Target Schema | Changes Needed |
|---|---|---|---|
| GMB Raw | GMB-Raw-A | Std GMB Raw | Rename 10 cols to snake_case; add `email` col (empty) |
| GMB Enriched | GMB-Enriched-E | Std GMB Enriched | Same as Lekki — rename, remove dup `WhatsApp`, move `Date Collected` |
| LinkedIn Raw | LinkedIn-A | Std LinkedIn | Rename cols; add 5 missing cols (empty) |
| Web Raw | _(none)_ | Std Web | Create file when collection is done |

---

## 5. Data Integrity Risks

Before performing any standardization, the following risks must be mitigated:

1. **AREA_SUMMARY.md reports** — These reference specific column names. Any column rename will break the report generation logic. Reports must be regenerated after schema changes.

2. **Niche categorizations** — Existing niche values are tied to `Business Niche` / `niche` column. Renaming must preserve exact values.

3. **Data loss from column removal** — The duplicate `WhatsApp` column in Ikeja/Lekki/VI enriched files may contain different values than `WhatsApp Contact`. Must audit before merging.

4. **Empty new columns** — Adding columns like `email` to GMB-Raw-A files will create empty values. This is acceptable but must be documented.

5. **Downstream scripts** — Any Python/Node scripts that parse these CSVs will need updates.

---

## 6. Implementation Recommendations

### Phase 1: Validation (Recommended First Step)
1. Write a validation script that reads every CSV and checks:
   - All rows have the expected column count
   - No extra commas in values (common CSV quoting issue)
   - Date columns parse correctly
   - URL columns contain valid-looking URLs
2. Document any data quality issues found

### Phase 2: Standardize Column Names Only
1. Create a migration script that renames columns in-place (header-only change)
2. This is the lowest-risk change — no data moves
3. Update all AREA_SUMMARY.md templates to use new column names

### Phase 3: Add Missing Columns
1. Add new empty columns where the standard requires them
2. Fill in values where possible (e.g., `city_area` from directory path, `date_collected` from file metadata)

### Phase 4: Reorder Columns
1. Reorder columns to match the standard ordering
2. This is purely cosmetic but improves readability

### Phase 5: Fix Data Issues
1. Resolve the duplicate `WhatsApp` column in enriched files
2. Normalize `website_verified` values (True/False/empty)
3. Normalize `email_validation_status` values

### Ongoing
- All future lead collection should use the standard schemas defined in Section 3
- Create CSV templates in each `Raw_Leads/` directory with just the header row
- Add a schema validation step to any automated collection pipeline
