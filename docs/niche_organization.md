# Business Niche Organization — Comprehensive Guide

> **Document Purpose:** This guide defines the complete business niche taxonomy used across all English Nations Hub city-area repositories. Every agent, researcher, and contributor must follow these conventions to ensure consistency, scalability, and maximum commercial value of the lead data we collect.

---

## Overview

The English Nations Hub is a structured repository of local business leads organised by **geographic area** and **business niche**. The goal is to build the most comprehensive, verified local business database available for English-speaking markets worldwide.

### Core Principles

- **Each city area** should ideally include leads across **50+ business niches**
- Niches are **organised by industry category** for intuitive navigation
- Agents should **prioritise high-value niches first** but expand coverage over time
- Every niche folder must contain **verified, structured lead data** — not raw dumps
- The repository is designed to serve **multiple buyer personas**: marketing agencies, SaaS companies, sales teams, and market researchers

### Folder Structure Convention

```
data/
├── {country}/
│   ├── {region_or_state}/
│   │   ├── {city_area}/
│   │   │   ├── healthcare_medical/
│   │   │   │   ├── dentists_dental_clinics.csv
│   │   │   │   ├── general_physicians.csv
│   │   │   │   └── ...
│   │   │   ├── legal_services/
│   │   │   ├── financial_services/
│   │   │   └── ...
```

All folder and file names use **snake_case**. Category-level folders group related niches. Individual niche folders contain CSV or JSON files with standardised lead records.

---

## Why Niche Organisation Matters

### 1. Enables Targeted Marketing Campaigns

Buyers rarely want "all businesses in a city." They want **dentists in Manchester**, **plumbers in Austin**, or **marketing agencies in Toronto**. Niche organisation lets them purchase precisely the segment they need, increasing perceived value and sale price.

### 2. Allows Niche-Specific Outreach Strategies

Different niches respond to different messaging. A cold email to a dentist should reference patient acquisition and chair-time utilisation. An email to a roofing contractor should mention lead generation for storm damage repair. Niche organisation lets agents and end-users craft **category-aware outreach templates**.

### 3. Supports Market Analysis by Industry

Researchers, investors, and competitors use niche-segmented data to analyse market density, competitive saturation, pricing trends, and geographic gaps. A city with 200 restaurants but only 3 marketing agencies presents a different opportunity profile than the reverse.

### 4. Makes the Repository Useful for Different Types of Buyers

| Buyer Type | Primary Niches of Interest |
|---|---|
| Marketing Agencies | Marketing Agencies, Web Developers, IT Services |
| SaaS Companies (Vertical) | Dentists, Accountants, Lawyers, Real Estate |
| Sales Teams / Lead Gen | All niches — bulk purchasing |
| Market Researchers | Dense coverage across all categories |
| Private Equity | Professional Services, Healthcare, Technology |

---

## The 60 Business Niches

Each niche below includes its **folder name convention**, **typical services offered**, **key contact data to collect**, **priority level** for outreach (H = High, M = Medium, L = Low), and **typical email patterns** observed in the wild.

---

### Healthcare & Medical (8 niches)

#### 1. Dentists & Dental Clinics
- **Folder:** `dentists_dental_clinics`
- **Services:** General dentistry, cosmetic dentistry, orthodontics, teeth whitening, dental implants, emergency dental care
- **Key Data:** Business name, dentist name(s), phone, email, website, address, specialisation (cosmetic, paediatric, orthodontic), NHS/private status (UK), number of chairs/locations
- **Priority:** **H** — Extremely high demand from dental SaaS (Dentrix, Curve Dental), marketing agencies, and equipment suppliers
- **Typical Emails:** `info@{practice}.com`, `contact@{practice}.com`, `hello@{practice}.co.uk`, `{name}@{practice}.com`

#### 2. General Physicians & Family Doctors
- **Folder:** `general_physicians_family_doctors`
- **Services:** Primary care, health screenings, vaccinations, chronic disease management, referrals
- **Key Data:** Practice name, GP name(s), phone, email, website, address, NHS registration (UK), insurance networks accepted (US/CA/AU), patient capacity
- **Priority:** **H** — High demand from healthcare SaaS, telemedicine platforms, medical billing companies
- **Typical Emails:** `admin@{practice}.com`, `reception@{practice}.co.uk`, `info@{clinic}.com`

#### 3. Pharmacies
- **Folder:** `pharmacies`
- **Services:** Prescription dispensing, OTC medications, flu vaccinations, health consultations, compounding
- **Key Data:** Pharmacy name, pharmacist name, phone, email, website, address, chain vs. independent, services offered (compounding, vaccinations, delivery)
- **Priority:** **M** — Moderate demand; pharmacy chains have centralised marketing, but independent pharmacies are valuable leads
- **Typical Emails:** `info@{pharmacy}.com`, `{store}@{chain}.com`, `pharmacy.{location}@{chain}.co.uk`

#### 4. Optometrists & Eye Care
- **Folder:** `optometrists_eye_care`
- **Services:** Eye exams, contact lens fitting, glasses dispensing, LASIK referrals, paediatric eye care
- **Key Data:** Practice name, optometrist name(s), phone, email, website, address, brands carried (designer frames), services (LASIK co-management, paediatric)
- **Priority:** **H** — High demand from optical SaaS, frame suppliers, and marketing agencies specialising in healthcare
- **Typical Emails:** `info@{practice}.com`, `hello@{optical}.com`, `contact@{eyecare}.co.uk`

#### 5. Physiotherapists & Chiropractors
- **Folder:** `physiotherapists_chiropractors`
- **Services:** Injury rehabilitation, sports therapy, spinal adjustment, massage therapy, post-surgical recovery
- **Key Data:** Clinic name, practitioner name(s), phone, email, website, address, specialisations (sports, neurological, paediatric), insurance affiliations
- **Priority:** **H** — Strong demand from practice management SaaS and marketing agencies
- **Typical Emails:** `info@{clinic}.com`, `admin@{practice}.com`, `{name}@{physio}.co.uk`

#### 6. Mental Health & Counseling
- **Folder:** `mental_health_counseling`
- **Services:** Individual therapy, couples counselling, CBT, psychiatric services, group therapy, online counselling
- **Key Data:** Practice name, therapist name(s), credentials (LCSW, PhD, PsyD, MFT), phone, email, website, address, specialisations (anxiety, trauma, addiction), telehealth capability
- **Priority:** **H** — Rapidly growing demand; mental health SaaS (SimplePractice, TheraNest) and directory platforms are aggressive buyers
- **Typical Emails:** `info@{practice}.com`, `contact@{counseling}.com`, `{name}@{therapy}.com`

#### 7. Veterinary Clinics
- **Folder:** `veterinary_clinics`
- **Services:** Wellness exams, vaccinations, surgery, dental care, emergency services, boarding
- **Key Data:** Clinic name, vet name(s), phone, email, website, address, services (24/7 emergency, exotics, equine), number of locations
- **Priority:** **M** — Niche but loyal buyer base; vet SaaS (Cornerstone, AVImark) and pet product companies
- **Typical Emails:** `info@{vetclinic}.com`, `reception@{vets}.co.uk`, `contact@{animalclinic}.com`

#### 8. Dermatologists & Skin Care
- **Folder:** `dermatologists_skin_care`
- **Services:** Medical dermatology, cosmetic procedures (Botox, fillers), skin cancer screening, acne treatment, laser therapy
- **Key Data:** Practice name, dermatologist name(s), board certification, phone, email, website, address, services (cosmetic vs. medical), number of providers
- **Priority:** **H** — High average transaction value; cosmetic dermatology is a premium market with strong digital marketing spend
- **Typical Emails:** `info@{dermatology}.com`, `contact@{skinclinic}.com`, `hello@{practice}.co.uk`

---

### Legal Services (5 niches)

#### 9. Lawyers & Law Firms
- **Folder:** `lawyers_law_firms`
- **Services:** General legal counsel, litigation, contract drafting, wills & estates, personal injury
- **Key Data:** Firm name, attorney name(s), practice areas, phone, email, website, address, firm size (solo, small, mid, large), bar admissions
- **Priority:** **H** — Legal is one of the highest-CPA verticals for marketing and SaaS; extremely competitive buyer market
- **Typical Emails:** `info@{firm}.com`, `{name}@{firm}.com`, `contact@{law}.co.uk`

#### 10. Real Estate Attorneys
- **Folder:** `real_estate_attorneys`
- **Services:** Property transactions, title searches, closings, landlord-tenant disputes, zoning
- **Key Data:** Attorney/firm name, phone, email, website, address, transaction volume indicators, jurisdictions served
- **Priority:** **H** — High-value niche; real estate attorneys work on high-ticket transactions and invest in marketing
- **Typical Emails:** `info@{firm}.com`, `{name}@{realestatelaw}.com`, `contact@{conveyancing}.co.uk`

#### 11. Immigration Lawyers
- **Folder:** `immigration_lawyers`
- **Services:** Visa applications, green cards, citizenship, deportation defence, work permits, asylum
- **Key Data:** Attorney/firm name, phone, email, website, address, languages spoken, visa types handled, success rate indicators
- **Priority:** **H** — Immigration is a high-stress, high-urgency service; clients search aggressively online; strong digital marketing opportunity
- **Typical Emails:** `info@{firm}.com`, `contact@{immigration}.com`, `{name}@{visalaw}.com`

#### 12. Corporate / Business Lawyers
- **Folder:** `corporate_business_lawyers`
- **Services:** Business formation, M&A, IP protection, contract negotiation, compliance, employment law
- **Key Data:** Firm name, attorney name(s), phone, email, website, address, industry focus (tech, healthcare, finance), client size focus
- **Priority:** **H** — Corporate law firms have large marketing budgets and buy high-value SaaS solutions
- **Typical Emails:** `info@{firm}.com`, `{name}@{lawfirm}.com`, `contact@{corporate}.co.uk`

#### 13. Family Law Practitioners
- **Folder:** `family_law_practitioners`
- **Services:** Divorce, child custody, adoption, prenuptial agreements, domestic violence, mediation
- **Key Data:** Practice name, attorney name(s), phone, email, website, address, specialisations, collaborative law certification
- **Priority:** **H** — Family law has high search volume and emotional urgency; strong performance marketing vertical
- **Typical Emails:** `info@{practice}.com`, `{name}@{familylaw}.com`, `contact@{solicitors}.co.uk`

---

### Financial Services (6 niches)

#### 14. Accountants & CPAs
- **Folder:** `accountants_cpas`
- **Services:** Tax preparation, auditing, financial consulting, bookkeeping advisory, business advisory
- **Key Data:** Firm name, accountant name(s), credentials (CPA, CA, ACCA), phone, email, website, address, firm size, specialisations (tax, audit, advisory)
- **Priority:** **H** — Accountants are prolific SaaS buyers (QuickBooks, Xero ecosystem) and respond well to B2B outreach
- **Typical Emails:** `info@{firm}.com`, `{name}@{accounting}.com`, `contact@{firm}.co.uk`

#### 15. Financial Advisors
- **Folder:** `financial_advisors`
- **Services:** Investment planning, retirement planning, wealth management, estate planning, insurance advisory
- **Key Data:** Firm/advisor name, phone, email, website, address, regulatory registrations (SEC, FCA, ASIC), AUM indicators, specialisations
- **Priority:** **H** — High-net-worth client base; financial advisors invest heavily in lead generation and digital presence
- **Typical Emails:** `info@{firm}.com`, `{name}@{wealth}.com`, `contact@{advisors}.co.uk`

#### 16. Tax Preparation Services
- **Folder:** `tax_preparation_services`
- **Services:** Personal tax returns, business tax returns, tax planning, IRS/AU-ATO/UK-HMRC correspondence, tax resolution
- **Key Data:** Business name, phone, email, website, address, seasonal vs. year-round operation, software used, number of preparers
- **Priority:** **M** — Highly seasonal demand; strong Q1 outreach window; valuable for tax SaaS and marketing agencies
- **Typical Emails:** `info@{tax}.com`, `contact@{taxservice}.com`, `office@{accounting}.co.uk`

#### 17. Insurance Agencies
- **Folder:** `insurance_agencies`
- **Services:** Life insurance, health insurance, auto insurance, home insurance, commercial insurance, business liability
- **Key Data:** Agency name, agent name(s), phone, email, website, address, carriers represented, lines of business, independent vs. captive
- **Priority:** **H** — Insurance agents are aggressive lead buyers and invest significantly in marketing
- **Typical Emails:** `info@{agency}.com`, `{name}@{insurance}.com`, `contact@{agency}.co.uk`

#### 18. Bookkeeping Services
- **Folder:** `bookkeeping_services`
- **Services:** Accounts payable/receivable, bank reconciliation, payroll processing, financial reporting, BAS/VAT/GST filing
- **Key Data:** Business name, phone, email, website, address, software proficiency (QuickBooks, Xero, Sage), certifications, client industries
- **Priority:** **M** — Growing market; bookkeepers increasingly adopt SaaS tools and are responsive to efficiency pitches
- **Typical Emails:** `info@{bookkeeping}.com`, `hello@{books}.com`, `contact@{firm}.co.uk`

#### 19. Payroll Services
- **Folder:** `payroll_services`
- **Services:** Payroll processing, tax withholding, direct deposit, compliance reporting, benefits administration, time tracking
- **Key Data:** Company name, phone, email, website, address, client count range, integration capabilities, industries served
- **Priority:** **M** — Consolidating market dominated by ADP, Paychex, Gusto; niche players are acquisition targets
- **Typical Emails:** `info@{payroll}.com`, `sales@{payroll}.com`, `contact@{company}.co.uk`

---

### Food & Hospitality (7 niches)

#### 20. Restaurants & Cafes
- **Folder:** `restaurants_cafes`
- **Services:** Dine-in, takeaway, delivery, catering, private dining, event hosting
- **Key Data:** Business name, owner/manager name, phone, email, website, address, cuisine type, price range, seating capacity, delivery platforms used, review ratings
- **Priority:** **H** — Massive market; high demand from POS systems, reservation platforms, food delivery aggregators, and review management tools
- **Typical Emails:** `info@{restaurant}.com`, `hello@{cafe}.com`, `manager@{restaurant}.co.uk`

#### 21. Catering Services
- **Folder:** `catering_services`
- **Services:** Corporate catering, wedding catering, event catering, drop-off catering, full-service catering
- **Key Data:** Company name, phone, email, website, address, cuisine types, event types, capacity, price range, delivery radius
- **Priority:** **M** — Event-driven demand cycles; valuable for event management platforms and venue directories
- **Typical Emails:** `info@{catering}.com`, `events@{catering}.com`, `hello@{catering}.co.uk`

#### 22. Bakeries
- **Folder:** `bakeries`
- **Services:** Custom cakes, pastries, bread, wedding cakes, gluten-free options, wholesale
- **Key Data:** Bakery name, phone, email, website, address, specialities, custom order capability, wholesale availability, dietary accommodations
- **Priority:** **M** — Seasonal peaks (weddings, holidays); responsive to local marketing and online ordering tools
- **Typical Emails:** `info@{bakery}.com`, `orders@{bakery}.com`, `hello@{bakery}.co.uk`

#### 23. Hotels & Lodging
- **Folder:** `hotels_lodging`
- **Services:** Accommodation, conference facilities, event hosting, restaurant/bar, spa services, airport transfers
- **Key Data:** Property name, phone, email, website, address, star rating, room count, amenities, corporate rate availability, review scores
- **Priority:** **H** — High-value B2B buyers: PMS vendors, OTAs, revenue management SaaS, and corporate travel platforms
- **Typical Emails:** `info@{hotel}.com`, `reservations@{hotel}.com`, `gm@{hotel}.com`

#### 24. Bars & Lounges
- **Folder:** `bars_lounges`
- **Services:** Craft cocktails, live entertainment, happy hours, private events, food service, karaoke/trivia
- **Key Data:** Bar name, phone, email, website, address, capacity, entertainment schedule, private event availability, liquor licence type
- **Priority:** **L** — Lower B2B SaaS demand but useful for event promotion platforms, beverage distributors, and local marketing
- **Typical Emails:** `info@{bar}.com`, `events@{bar}.com`, `hello@{lounge}.co.uk`

#### 25. Food Delivery Services
- **Folder:** `food_delivery_services`
- **Services:** Meal delivery, ghost kitchen operations, corporate catering delivery, subscription meal plans
- **Key Data:** Company name, phone, email, website, delivery radius, platform used, cuisine types, pricing model
- **Priority:** **M** — Growing market; valuable for logistics SaaS, packaging suppliers, and kitchen equipment vendors
- **Typical Emails:** `info@{delivery}.com`, `support@{delivery}.com`, `hello@{meals}.co.uk`

#### 26. Event Venues
- **Folder:** `event_venues`
- **Services:** Wedding receptions, corporate events, conferences, concerts, exhibitions, private parties
- **Key Data:** Venue name, phone, email, website, address, capacity, event types, catering in-house vs. external, AV equipment, pricing tier
- **Priority:** **M** — Event management platforms, wedding directories, and AV companies are key buyers
- **Typical Emails:** `info@{venue}.com`, `events@{venue}.com`, `bookings@{venue}.co.uk`

---

### Home Services (8 niches)

#### 27. Plumbers
- **Folder:** `plumbers`
- **Services:** Emergency repairs, installations, drain cleaning, water heater services, gas fitting, bathroom remodelling
- **Key Data:** Business name, phone, email, website, address, emergency availability, licencing, service radius, specialisations
- **Priority:** **H** — Home services is one of the most competitive local SEO verticals; extremely high marketing demand
- **Typical Emails:** `info@{plumbing}.com`, `contact@{plumbing}.com`, `office@{plumbers}.co.uk`

#### 28. Electricians
- **Folder:** `electricians`
- **Services:** Wiring, panel upgrades, lighting installation, EV charger installation, generator installation, safety inspections
- **Key Data:** Business name, phone, email, website, address, licencing/certification, emergency availability, commercial vs. residential focus
- **Priority:** **H** — Same dynamic as plumbing; electricians invest heavily in local marketing and lead generation
- **Typical Emails:** `info@{electrical}.com`, `contact@{electrical}.com`, `office@{electricians}.co.uk`

#### 29. HVAC Services
- **Folder:** `hvac_services`
- **Services:** Installation, repair, maintenance plans, duct cleaning, indoor air quality, commercial HVAC
- **Key Data:** Company name, phone, email, website, address, brands serviced, maintenance plan offerings, emergency availability, commercial capability
- **Priority:** **H** — HVAC has the highest average ticket price in home services; very strong marketing investment
- **Typical Emails:** `info@{hvac}.com`, `service@{hvac}.com`, `contact@{heating}.co.uk`

#### 30. Cleaning Services (Residential & Commercial)
- **Folder:** `cleaning_services`
- **Services:** Residential cleaning, commercial cleaning, deep cleaning, move-in/out cleaning, carpet cleaning, post-construction cleaning
- **Key Data:** Company name, phone, email, website, address, residential vs. commercial split, team size, bonded/insured status, scheduling software used
- **Priority:** **H** — High search volume, low barriers to entry = massive market with many small operators needing marketing help
- **Typical Emails:** `info@{cleaning}.com`, `hello@{clean}.com`, `contact@{cleaners}.co.uk`

#### 31. Landscaping & Gardening
- **Folder:** `landscaping_gardening`
- **Services:** Lawn care, garden design, tree surgery, irrigation, hardscaping, seasonal maintenance
- **Key Data:** Company name, phone, email, website, address, services offered, commercial vs. residential, fleet size, seasonal capacity
- **Priority:** **M** — Seasonal demand; strong in spring/summer; valuable for equipment suppliers and SaaS
- **Typical Emails:** `info@{landscaping}.com`, `contact@{garden}.com`, `hello@{lawncare}.co.uk`

#### 32. Painters
- **Folder:** `painters`
- **Services:** Interior painting, exterior painting, commercial painting, decorative finishes, cabinet refinishing, wallpaper
- **Key Data:** Company name, phone, email, website, address, specialisations, crew size, commercial capability, licensing
- **Priority:** **M** — Moderate market; responsive to review management and lead generation services
- **Typical Emails:** `info@{painting}.com`, `contact@{painters}.com`, `office@{decorators}.co.uk`

#### 33. Roofing Contractors
- **Folder:** `roofing_contractors`
- **Services:** Roof repair, roof replacement, gutter installation, skylight installation, flat roofing, emergency storm damage
- **Key Data:** Company name, phone, email, website, address, materials speciality, insurance claim assistance, commercial capability, warranty offered
- **Priority:** **H** — Very high ticket prices; storm damage creates spikes in demand; strong marketing vertical
- **Typical Emails:** `info@{roofing}.com`, `estimates@{roofing}.com`, `contact@{roofers}.co.uk`

#### 34. Pest Control
- **Folder:** `pest_control`
- **Services:** General pest control, termite treatment, rodent control, bed bug treatment, wildlife removal, preventive plans
- **Key Data:** Company name, phone, email, website, address, treatment types, subscription plans, certifications, service radius
- **Priority:** **M** — Recurring revenue model makes these businesses valuable; SaaS and marketing demand is steady
- **Typical Emails:** `info@{pestcontrol}.com`, `contact@{pest}.com`, `hello@{exterminators}.co.uk`

---

### Professional Services (7 niches)

#### 35. Marketing Agencies
- **Folder:** `marketing_agencies`
- **Services:** SEO, PPC, social media management, content marketing, email marketing, branding, web design
- **Key Data:** Agency name, phone, email, website, address, team size, specialisations, client industries, minimum retainer, certifications (Google Partner, Meta Partner)
- **Priority:** **H** — Marketing agencies are both buyers AND sellers in the lead data ecosystem; critical niche
- **Typical Emails:** `info@{agency}.com`, `hello@{agency}.com`, `{name}@{agency}.com`

#### 36. IT Services & Computer Repair
- **Folder:** `it_services_computer_repair`
- **Services:** Managed IT, computer repair, network setup, cloud services, cybersecurity, data recovery, VoIP
- **Key Data:** Company name, phone, email, website, address, services offered, commercial vs. residential, SLA offerings, certifications (MSP, CompTIA)
- **Priority:** **M** — MSP market is consolidating; valuable for IT vendor sales and channel partner recruitment
- **Typical Emails:** `info@{itservices}.com`, `support@{computers}.com`, `contact@{tech}.co.uk`

#### 37. Consulting Firms
- **Folder:** `consulting_firms`
- **Services:** Management consulting, strategy, operations, HR consulting, digital transformation, fractional executive services
- **Key Data:** Firm name, phone, email, website, address, consulting speciality, firm size, client industries, engagement model
- **Priority:** **M** — Lower volume but high-value contacts; useful for enterprise sales and partnership development
- **Typical Emails:** `info@{consulting}.com`, `{name}@{firm}.com`, `contact@{advisory}.co.uk`

#### 38. Recruitment Agencies
- **Folder:** `recruitment_agencies`
- **Services:** Permanent placement, temp staffing, executive search, niche/specialist recruitment, RPO
- **Key Data:** Agency name, phone, email, website, address, industry focus, placement level, candidate database size, fee structure
- **Priority:** **M** — Recruitment tech (ATS, sourcing tools) is a major buyer category; strong B2B SaaS demand
- **Typical Emails:** `info@{recruitment}.com`, `jobs@{recruitment}.com`, `contact@{recruiters}.co.uk`

#### 39. Translation Services
- **Folder:** `translation_services`
- **Services:** Document translation, interpreting, localisation, certified translation, subtitling, transcreation
- **Key Data:** Company name, phone, email, website, address, languages offered, certifications, specialisations (legal, medical, technical), turnaround times
- **Priority:** **L** — Niche market; valuable for globalisation platforms and language tech companies
- **Typical Emails:** `info@{translation}.com`, `contact@{languages}.com`, `hello@{translators}.co.uk`

#### 40. Printing & Copy Services
- **Folder:** `printing_copy_services`
- **Services:** Business cards, brochures, banners, large format printing, binding, promotional products, mailing services
- **Key Data:** Company name, phone, email, website, address, equipment types, digital vs. offset, turnaround times, design services offered
- **Priority:** **L** — Declining market due to digital shift; still useful for print management SaaS and franchise directories
- **Typical Emails:** `info@{printing}.com`, `orders@{print}.com`, `contact@{copyshop}.co.uk`

#### 41. Security Services
- **Folder:** `security_services`
- **Services:** Manned guarding, CCTV installation, alarm systems, access control, mobile patrols, event security
- **Key Data:** Company name, phone, email, website, address, services offered, licencing (SIA in UK), client industries, monitoring capability
- **Priority:** **M** — Growing demand driven by commercial security needs; security tech vendors are active buyers
- **Typical Emails:** `info@{security}.com`, `contact@{security}.com`, `office@{guarding}.co.uk`

---

### Creative Services (6 niches)

#### 42. Photographers
- **Folder:** `photographers`
- **Services:** Wedding photography, portrait photography, commercial photography, event photography, product photography, real estate photography
- **Key Data:** Photographer name, phone, email, website, address, specialisations, pricing tier, second shooter availability, studio vs. on-location
- **Priority:** **M** — Large fragmented market; valuable for editing SaaS (Lightroom alternatives), gallery platforms, and booking tools
- **Typical Emails:** `info@{photography}.com`, `hello@{photos}.com`, `{name}@{studio}.com`

#### 43. Videographers
- **Folder:** `videographers`
- **Services:** Wedding videography, corporate video, event coverage, real estate video, social media content, aerial/drone footage
- **Key Data:** Company/videographer name, phone, email, website, address, specialisations, equipment used, pricing, drone certification
- **Priority:** **M** — Growing demand for short-form video; valuable for editing software and stock footage platforms
- **Typical Emails:** `info@{video}.com`, `contact@{videography}.com`, `hello@{media}.co.uk`

#### 44. Graphic Designers
- **Folder:** `graphic_designers`
- **Services:** Logo design, brand identity, print design, packaging design, digital design, UI/UX design
- **Key Data:** Designer/agency name, phone, email, website, address, specialisations, tools used (Adobe, Figma, Canva), portfolio link
- **Priority:** **M** — Useful for design tool vendors, freelance platforms, and creative staffing agencies
- **Typical Emails:** `info@{design}.com`, `hello@{studio}.com`, `{name}@{design}.co.uk`

#### 45. Interior Designers
- **Folder:** `interior_designers`
- **Services:** Residential interior design, commercial interior design, space planning, furniture sourcing, renovation project management
- **Key Data:** Designer/firm name, phone, email, website, address, style specialisations, project types, fee structure, trade accounts
- **Priority:** **M** — High-value professional referrals; valuable for furniture vendors, material suppliers, and design tech
- **Typical Emails:** `info@{design}.com`, `studio@{interiors}.com`, `contact@{designer}.co.uk`

#### 46. Event Planners
- **Folder:** `event_planners`
- **Services:** Wedding planning, corporate events, social events, conference planning, destination events, partial planning
- **Key Data:** Planner name, phone, email, website, address, event types, client price range, vendor network size, certifications
- **Priority:** **M** — Seasonal demand; valuable for venue directories, catering platforms, and event management SaaS
- **Typical Emails:** `info@{events}.com`, `hello@{planning}.com`, `contact@{planner}.co.uk`

#### 47. Hair Salons & Barbers
- **Folder:** `hair_salons_barbers`
- **Services:** Haircuts, colouring, styling, extensions, beard grooming, spa treatments, bridal hair
- **Key Data:** Salon/barber name, phone, email, website, address, services offered, pricing tier, number of chairs, booking system used
- **Priority:** **M** — High volume, low individual value; useful for booking SaaS (Fresha, Vagaro) and product distributors
- **Typical Emails:** `info@{salon}.com`, `hello@{hair}.com`, `contact@{barbers}.co.uk`

---

### Education & Training (5 niches)

#### 48. Tutors & Tutoring Centers
- **Folder:** `tutors_tutoring_centers`
- **Services:** Subject tutoring, test prep (SAT, GCSE, A-Level), homework help, online tutoring, group classes
- **Key Data:** Center/tutor name, phone, email, website, address, subjects, levels, online capability, group size, pricing
- **Priority:** **M** — Growing market; valuable for EdTech platforms and tutoring marketplaces
- **Typical Emails:** `info@{tutoring}.com`, `hello@{learning}.com`, `contact@{tuition}.co.uk`

#### 49. Driving Schools
- **Folder:** `driving_schools`
- **Services:** Learner lessons, intensive courses, refresher lessons, motorcycle training, fleet driver training, theory test prep
- **Key Data:** School name, phone, email, website, address, vehicle types, instructor count, pass rate, lesson areas
- **Priority:** **L** — Niche but consistent demand; useful for driving school management SaaS
- **Typical Emails:** `info@{drivingschool}.com`, `lessons@{driving}.com`, `contact@{school}.co.uk`

#### 50. Language Schools
- **Folder:** `language_schools`
- **Services:** General language courses, business language training, exam preparation (IELTS, TOEFL), immersion programs, online classes
- **Key Data:** School name, phone, email, website, address, languages taught, course types, accreditation, student nationalities
- **Priority:** **L** — Valuable for EdTech and international student recruitment platforms
- **Typical Emails:** `info@{languages}.com`, `hello@{school}.com`, `contact@{courses}.co.uk`

#### 51. Vocational Training Centers
- **Folder:** `vocational_training_centers`
- **Services:** Trade certifications, professional development, safety training, compliance training, apprenticeships
- **Key Data:** Center name, phone, email, website, address, training areas, certification bodies, delivery modes (in-person, online, blended)
- **Priority:** **L** — Important for workforce development; buyers include LMS vendors and certification platforms
- **Typical Emails:** `info@{training}.com`, `enrol@{center}.com`, `contact@{courses}.co.uk`

#### 52. Daycare & Preschools
- **Folder:** `daycare_preschools`
- **Services:** Childcare, early education, after-school programs, infant care, preschool curriculum, part-time and full-time care
- **Key Data:** Center name, phone, email, website, address, capacity, age ranges, curriculum type, licensing, hours of operation
- **Priority:** **M** — Parents search aggressively; valuable for childcare management SaaS and family-focused marketing
- **Typical Emails:** `info@{daycare}.com`, `hello@{preschool}.com`, `contact@{childcare}.co.uk`

---

### Fitness & Wellness (4 niches)

#### 53. Gyms & Fitness Centers
- **Folder:** `gyms_fitness_centers`
- **Services:** Gym memberships, group classes, personal training, swimming, squash, childcare, corporate wellness
- **Key Data:** Gym name, phone, email, website, address, membership tiers, facilities, group class schedule, chain vs. independent
- **Priority:** **H** — High demand from gym management SaaS (Mindbody, Zen Planner), equipment vendors, and marketing agencies
- **Typical Emails:** `info@{gym}.com`, `membership@{gym}.com`, `contact@{fitness}.co.uk`

#### 54. Yoga Studios
- **Folder:** `yoga_studios`
- **Services:** Yoga classes (vinyasa, hot, restorative, prenatal), meditation, teacher training, workshops, retreats
- **Key Data:** Studio name, phone, email, website, address, class types, teacher training program, pricing, online class capability
- **Priority:** **M** — Strong community orientation; valuable for wellness platforms and booking SaaS
- **Typical Emails:** `info@{yoga}.com`, `hello@{studio}.com`, `contact@{yoga}.co.uk`

#### 55. Personal Trainers
- **Folder:** `personal_trainers`
- **Services:** One-on-one training, online coaching, group training, nutrition planning, body transformation programs
- **Key Data:** Trainer name, phone, email, website, social media profiles, certifications, specialisations, rates, training locations
- **Priority:** **L** — Individual operators with low technology adoption; useful for fitness SaaS and supplement companies
- **Typical Emails:** `{name}@{training}.com`, `info@{fitness}.com`, `hello@{coach}.co.uk`

#### 56. Spas & Wellness Centers
- **Folder:** `spas_wellness_centers`
- **Services:** Massages, facials, body treatments, hydrotherapy, wellness retreats, membership packages
- **Key Data:** Spa name, phone, email, website, address, services offered, pricing tier, product lines, booking system
- **Priority:** **M** — High disposable income clientele; valuable for spa management SaaS and luxury product vendors
- **Typical Emails:** `info@{spa}.com`, `hello@{wellness}.com`, `contact@{spa}.co.uk`

---

### Technology (4 niches)

#### 57. Web Developers
- **Folder:** `web_developers`
- **Services:** Website design and development, e-commerce, CMS development, web application development, website maintenance
- **Key Data:** Company/freelancer name, phone, email, website, address, technology stack, specialisations, team size, project range
- **Priority:** **H** — Web developers are key partners for SaaS companies and marketing agencies; strong referral value
- **Typical Emails:** `info@{agency}.com`, `hello@{webdev}.com`, `{name}@{studio}.com`

#### 58. App Developers
- **Folder:** `app_developers`
- **Services:** iOS development, Android development, cross-platform development, UI/UX design, app maintenance, app strategy
- **Key Data:** Company name, phone, email, website, address, platforms, technology stack, portfolio, industries served, team size
- **Priority:** **M** — Valuable for enterprise app vendors seeking development partners and freelance platforms
- **Typical Emails:** `info@{appdev}.com`, `hello@{mobile}.com`, `contact@{apps}.co.uk`

#### 59. Software Companies
- **Folder:** `software_companies`
- **Services:** SaaS products, custom software development, ERP/CRM solutions, data analytics, AI/ML solutions
- **Key Data:** Company name, phone, email, website, address, product type, target market, funding stage, team size, tech stack
- **Priority:** **H** — Software companies are both data consumers and partnership targets; extremely valuable niche
- **Typical Emails:** `info@{software}.com`, `hello@{company}.com`, `{name}@{software}.co.uk`

#### 60. Cybersecurity Firms
- **Folder:** `cybersecurity_firms`
- **Services:** Security audits, penetration testing, compliance (SOC2, ISO 27001), managed security, incident response, security awareness training
- **Key Data:** Company name, phone, email, website, address, services offered, certifications, client industries, MSSP capability
- **Priority:** **M** — High-growth niche; valuable for security tool vendors, MSSP partners, and enterprise sales teams
- **Typical Emails:** `info@{cybersecurity}.com`, `contact@{security}.com`, `hello@{cyber}.co.uk`

---

## Additional High-Value Niches (Bonus)

These niches are not part of the core 60 but should be captured when discovered. They represent **high-demand verticals** with strong buyer markets.

| # | Niche | Folder Name | Priority | Key Buyer Segments |
|---|---|---|---|---|
| B1 | Real Estate Agents & Agencies | `real_estate_agents` | H | CRM vendors, marketing agencies, mortgage lenders, title companies |
| B2 | Auto Repair & Mechanics | `auto_repair_mechanics` | H | Parts distributors, shop management SaaS, fleet management |
| B3 | Car Dealerships | `car_dealerships` | H | DMS vendors, marketing agencies, auto finance, warranty providers |
| B4 | Moving Companies | `moving_companies` | M | Booking platforms, packing supply vendors, storage facilities |
| B5 | Architects | `architects` | M | BIM software vendors, construction material suppliers, rendering tools |
| B6 | Construction Companies | `construction_companies` | H | Construction management SaaS, equipment vendors, safety compliance platforms |

---

## Niche Priority Matrix

The following matrix evaluates each niche across three dimensions to determine overall priority for data collection and outreach:

| Niche | Lead Volume Potential | Contact Data Availability | Outreach Conversion Rate | Overall Priority |
|---|:---:|:---:|:---:|:---:|
| Dentists & Dental Clinics | High | High | Medium | **H** |
| General Physicians & Family Doctors | High | Medium | Low | **H** |
| Pharmacies | Medium | Medium | Low | **M** |
| Optometrists & Eye Care | Medium | High | Medium | **H** |
| Physiotherapists & Chiropractors | Medium | High | Medium | **H** |
| Mental Health & Counseling | High | Medium | Medium | **H** |
| Veterinary Clinics | Medium | High | Medium | **M** |
| Dermatologists & Skin Care | Medium | High | Medium | **H** |
| Lawyers & Law Firms | High | High | High | **H** |
| Real Estate Attorneys | Medium | High | High | **H** |
| Immigration Lawyers | Medium | Medium | High | **H** |
| Corporate / Business Lawyers | Medium | High | High | **H** |
| Family Law Practitioners | Medium | High | High | **H** |
| Accountants & CPAs | High | High | Medium | **H** |
| Financial Advisors | Medium | High | Medium | **H** |
| Tax Preparation Services | Medium | Medium | Medium | **M** |
| Insurance Agencies | High | High | High | **H** |
| Bookkeeping Services | Medium | Medium | Medium | **M** |
| Payroll Services | Medium | Medium | Medium | **M** |
| Restaurants & Cafes | Very High | Medium | Low | **H** |
| Catering Services | Medium | Medium | Medium | **M** |
| Bakeries | Medium | Medium | Low | **M** |
| Hotels & Lodging | Medium | High | Medium | **H** |
| Bars & Lounges | Medium | Low | Low | **L** |
| Food Delivery Services | Medium | Medium | Medium | **M** |
| Event Venues | Medium | High | Medium | **M** |
| Plumbers | High | High | High | **H** |
| Electricians | High | High | High | **H** |
| HVAC Services | Medium | High | High | **H** |
| Cleaning Services | Very High | Medium | Medium | **H** |
| Landscaping & Gardening | Medium | Medium | Medium | **M** |
| Painters | Medium | Medium | Medium | **M** |
| Roofing Contractors | Medium | High | High | **H** |
| Pest Control | Medium | Medium | Medium | **M** |
| Marketing Agencies | High | High | High | **H** |
| IT Services & Computer Repair | Medium | Medium | Medium | **M** |
| Consulting Firms | Low | High | Low | **M** |
| Recruitment Agencies | Medium | High | Medium | **M** |
| Translation Services | Low | Medium | Low | **L** |
| Printing & Copy Services | Medium | Medium | Low | **L** |
| Security Services | Medium | Medium | Medium | **M** |
| Photographers | High | Medium | Medium | **M** |
| Videographers | Medium | Medium | Medium | **M** |
| Graphic Designers | Medium | Medium | Medium | **M** |
| Interior Designers | Low | High | Medium | **M** |
| Event Planners | Medium | Medium | Medium | **M** |
| Hair Salons & Barbers | Very High | Medium | Low | **M** |
| Tutors & Tutoring Centers | Medium | Medium | Medium | **M** |
| Driving Schools | Low | Medium | Low | **L** |
| Language Schools | Low | Medium | Low | **L** |
| Vocational Training Centers | Low | Medium | Low | **L** |
| Daycare & Preschools | Medium | Medium | Medium | **M** |
| Gyms & Fitness Centers | High | High | Medium | **H** |
| Yoga Studios | Medium | Medium | Medium | **M** |
| Personal Trainers | Medium | Low | Low | **L** |
| Spas & Wellness Centers | Medium | High | Medium | **M** |
| Web Developers | Medium | High | High | **H** |
| App Developers | Low | High | Medium | **M** |
| Software Companies | Low | High | Medium | **H** |
| Cybersecurity Firms | Low | High | Medium | **M** |

---

## Niche Expansion Protocol

### How Agents Should Add New Niches

When an agent discovers a business niche that is **not covered in the 60+ list above**, they should:

1. **Evaluate market viability:** Does this niche have at least 20 businesses in the target city area? Is there a clear buyer market for the data?
2. **Check for duplicates:** Review the existing niche list to see if the discovered niche fits under an existing category. For example, "Orthodontists" should be grouped under "Dentists & Dental Clinics" unless the volume justifies a separate folder.
3. **Propose the new niche:** Open an issue or discussion in the repository with the proposed niche name, justification, and expected volume.
4. **Receive approval:** A new niche should not be added to the main dataset until approved by a repository maintainer to prevent category sprawl.

### Documentation Requirements for New Niches

Every new niche must include:

- **Niche name** (title case for display, snake_case for folder)
- **Parent category** (must fit under an existing category or propose a new one)
- **Brief description** (1-2 sentences)
- **Key data fields** (minimum 5, maximum 15)
- **Priority assessment** (H/M/L with justification)
- **Typical email patterns** (based on research of at least 10 businesses in the niche)
- **Known buyer segments** (who would purchase this lead data)

### Naming Conventions for New Niche Folders

- All folder names use **snake_case**
- Pluralise the primary noun: `restaurants_cafes`, not `restaurant_cafe`
- Use **underscores** between words: `mental_health_counseling`
- Keep folder names **under 40 characters** when possible
- Avoid abbreviations unless universally understood (e.g., `cpas` is acceptable, `hvacs` is not — use `hvac_services`)
- For compound niches, use the most descriptive term first: `it_services_computer_repair`, not `computer_repair_it_services`

---

## Per-Area Target Coverage

### Coverage Tiers

| Tier | Niches Covered | Status Label |
|---|---|---|
| **Minimum Viable** | 30+ niches | `coverage-minimum` |
| **Standard Target** | 50+ niches | `coverage-standard` |
| **Stretch Goal** | 60+ niches | `coverage-complete` |
| **Expanded** | 60+ core + bonus niches | `coverage-expanded` |

### How to Prioritise Niches by City Characteristics

Not every city has equal demand across all niches. Agents should adjust priorities based on:

**City Size / Population:**
- **Large metro areas (1M+):** Prioritise professional services, technology, creative services — higher density of B2B businesses
- **Mid-size cities (250K–1M):** Balanced approach; home services and healthcare are strong across all sizes
- **Small cities (under 250K):** Prioritise home services, healthcare, food & hospitality — these have the highest per-capita business density

**Economic Profile:**
- **Finance / business hubs (e.g., London, New York, Toronto):** Prioritise legal, financial, consulting, technology niches
- **Tourist destinations (e.g., Orlando, Gold Coast, Edinburgh):** Prioritise hospitality, event venues, tour operators
- **Industrial / manufacturing cities:** Prioritise construction, security, industrial services
- **University towns:** Prioritise education, food & hospitality, student-facing services

**Regional Variations:**
- **UK-specific:** Conveyancing solicitors, NHS-aligned medical practices, pubs (can be captured under Bars & Lounges or as a separate bonus niche)
- **US-specific:** Urgent care centers, med spas, marijuana dispensaries (where legal — high-value bonus niche)
- **Australia-specific:** Trades-focused niches (plumbers, electricians, builders) have very high per-capita density
- **Canada-specific:** Bilingual service niches in Quebec (French-language providers), winter-specific services (snow removal, heating specialists)

### Coverage Tracking

Each city area should include a `COVERAGE.md` file summarising:

```markdown
# Coverage Report — {City Name}

Last Updated: YYYY-MM-DD
Agent: {agent_name}

## Summary
- Total Niches Covered: 47 / 60
- Coverage Tier: Standard Target
- Total Leads: 3,241

## Category Breakdown
| Category | Niches Covered | Target | Status |
|---|---|---|---|
| Healthcare & Medical | 7 / 8 | 8 | ⚠️ Missing: Dermatologists |
| Legal Services | 5 / 5 | 5 | ✅ Complete |
| Financial Services | 4 / 6 | 6 | ⚠️ Missing: Payroll, Tax Prep |
| ... | ... | ... | ... |

## Next Actions
- [ ] Collect dermatologist leads from Google Maps
- [ ] Verify and expand financial services coverage
- [ ] Add bonus niche: Real Estate Agents
```

---

## Niche-Specific Search Strategies

For the **top 10 high-priority niches**, agents should use these refined search queries to maximise lead discovery:

### 1. Dentists & Dental Clinics
```
dentist in {city} {country}
dental clinic {city} {region}
cosmetic dentist {city}
emergency dentist {city} open now
"{city}" dentist near me
```

### 2. Lawyers & Law Firms
```
law firm {city} {country}
solicitor {city} {region}  (UK)
attorney {city} {state}     (US)
corporate lawyer {city}
"{city}" legal services
```

### 3. Accountants & CPAs
```
accountant {city} {country}
CPA {city} {state}          (US)
chartered accountant {city} (UK/AU/CA)
tax accountant {city}
bookkeeping services {city}
```

### 4. Restaurants & Cafes
```
restaurant {city} {country}
cafe {city} {region}
best restaurants in {city}
"{city}" dining
"{city}" new restaurant 2024
```

### 5. Plumbers
```
plumber {city} {country}
emergency plumber {city}
licensed plumber {city} {region}
"{city}" plumbing services
gas fitter {city}           (UK/AU)
```

### 6. Electricians
```
electrician {city} {country}
emergency electrician {city}
licensed electrician {city} {region}
"{city}" electrical services
electrical contractor {city}
```

### 7. HVAC Services
```
HVAC {city} {country}
heating and cooling {city}
air conditioning {city} {region}
furnace repair {city}       (US/CA)
boiler repair {city}        (UK)
```

### 8. Cleaning Services
```
cleaning service {city} {country}
commercial cleaning {city}
house cleaning {city}
"{city}" maid service
end of tenancy cleaning {city}  (UK)
```

### 9. Marketing Agencies
```
marketing agency {city} {country}
digital marketing {city}
SEO agency {city}
"{city}" marketing company
social media agency {city}
```

### 10. Roofing Contractors
```
roofing contractor {city} {country}
roof repair {city}
roof replacement {city}
"{city}" roofer
emergency roof repair {city}
```

### General Search Tips for All Niches

- **Combine niche + location:** `{niche} {city} {country}` is the most reliable base query
- **Use "near me" variants:** Google Maps results for "{niche} near {city}" often surface businesses not found in standard search
- **Check industry directories:** Many niches have dedicated directories (e.g., Avvo for lawyers, Zocdoc for doctors, Houzz for interior designers)
- **Cross-reference review platforms:** Yelp, Google Reviews, Trustpilot, and industry-specific review sites surface additional businesses
- **Use category browsing on Google Maps:** Search the broad category (e.g., "Health" in a city) and then filter subcategories
- **Verify each lead:** Always confirm the business is still operational, the phone number connects, and the email address accepts mail before adding to the dataset

---

## Appendix: Quick-Reference Cheat Sheet

### Priority Legend
| Code | Meaning | Action |
|---|---|---|
| **H** | High Priority | Collect first; highest buyer demand; allocate most agent time |
| **M** | Medium Priority | Collect after H-niches; good buyer demand; fill gaps |
| **L** | Low Priority | Collect if discovered opportunistically; lowest buyer demand |

### Category Quick Map
| # | Category | Niches | H-Priority Count |
|---|---|---|---|
| 1 | Healthcare & Medical | 8 | 6 |
| 2 | Legal Services | 5 | 5 |
| 3 | Financial Services | 6 | 4 |
| 4 | Food & Hospitality | 7 | 2 |
| 5 | Home Services | 8 | 5 |
| 6 | Professional Services | 7 | 1 |
| 7 | Creative Services | 6 | 0 |
| 8 | Education & Training | 5 | 0 |
| 9 | Fitness & Wellness | 4 | 1 |
| 10 | Technology | 4 | 2 |
| **Total** | **10 categories** | **60 niches** | **26 H-priority** |

---

> **Document Maintained By:** English Nations Hub — Lead Data Operations Team
> **Last Updated:** 2025-01-01
> **Version:** 1.0.0
