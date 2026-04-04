# Email Validation Methods — Complete Guide

## Overview

Email validation is a critical component of the English Nations Hub repository. Every email address collected through discovery, scraping, or manual entry must pass through a structured validation pipeline before being used in outreach campaigns, CRM imports, or data exports. The quality of our email data directly impacts bounce rates, sender reputation, and overall campaign effectiveness.

This document defines the validation framework, the three canonical validation statuses, five validation methods, the recommended pipeline workflow, batch processing strategy, metadata requirements, and regional email patterns relevant to the ten English-speaking nations covered by this repository.

Every email in the repository **must** have a validation status. There are no exceptions. Even emails sourced from trusted directories or official websites must still pass at minimum the syntax and disposable-email checks before being marked as anything other than *Pending Validation*.

Multiple validation methods should be used in combination for maximum accuracy. No single method is sufficient on its own — each catches a different class of problems, and together they form a robust defense against bad data entering the system.

---

## Why Email Validation Matters

### Reduces Bounce Rates in Outreach Campaigns
Every bounced email signals to email service providers (ESPs) that the sender may be sending unsolicited or low-quality mail. High bounce rates trigger spam filters, throttle delivery speeds, and can result in outright blacklisting of the sending domain. By validating emails before they enter any campaign list, we keep bounce rates well below the industry-accepted threshold of 2%.

### Protects Sender Reputation
Sender reputation is an aggregate score maintained by mailbox providers (Gmail, Microsoft, Yahoo, etc.) based on complaint rates, bounce rates, and engagement metrics. A single batch of unverified emails can cause lasting damage that takes weeks or months to repair. Validation acts as a pre-flight check that prevents reputation-harming sends.

### Increases Campaign Effectiveness
Clean data means higher deliverability, which means more emails actually reach the inbox. More inbox placements translate directly into higher open rates, click-through rates, and ultimately more leads converted to clients. The return on investment from validation far exceeds its cost in time and tooling.

### Saves Money on Email Service Costs
Most ESPs charge per contact or per email sent. Storing and sending to invalid addresses is literally paying for nothing. For repositories containing tens of thousands of leads, removing invalid emails before import can save significant monthly costs.

### Ensures Data Quality Across the Repository
The English Nations Hub is a shared resource used by multiple agents and campaigns. If one agent allows bad data to accumulate, it pollutes the entire dataset. Consistent validation standards ensure every user can trust the data they pull from the repository.

---

## Validation Status Definitions

Every email in the repository must carry exactly one of the following three statuses. The status is stored in the `validation_status` field of each lead record.

### Validated

An email earns the **Validated** status when it has passed **at least two** of the five validation methods, **one of which must be SMTP verification**. Specifically:

- SMTP verification returned a positive response (250 OK or equivalent) from the destination mail server.
- MX records are active and properly configured for the domain.
- The email address passes RFC 5322 syntax validation.
- The email is not from a known disposable email provider.
- The email is not a role-based address (e.g., `info@`, `admin@`) unless it was intentionally collected as a known business contact point and flagged accordingly.

Validated emails are safe to use in outreach campaigns, CRM imports, and automated sequences.

### Pending Validation

An email carries the **Pending Validation** status when:

- The email has been collected (from a website, directory, social profile, or manual entry) but has not yet been processed through the full verification pipeline.
- A preliminary syntax check indicates the format appears correct (contains `@`, has a recognizable domain structure), but no deeper verification has been performed.
- The email is queued in a batch awaiting its turn in the validation pipeline.

**Pending emails must never be used in outreach campaigns.** They should be validated before any send activity. The goal is to minimize the time any email spends in this status — ideally completing validation within 24 hours of collection.

### Invalid

An email is marked **Invalid** when it fails one or more validation checks. Specific failure reasons include:

- SMTP verification returned a negative response (550, 551, 553, or 554 rejection codes).
- The domain has no MX records, or MX records point to non-functional servers.
- Syntax errors are detected (missing `@`, invalid characters, malformed domain, spaces in address).
- The email uses a known disposable or temporary email domain.
- A hard bounce was received during a prior send attempt.
- The domain does not exist (NXDOMAIN in DNS resolution).

Invalid emails should be retained in the repository for record-keeping (to prevent re-collection) but must be filtered out of all campaign exports and outreach lists.

---

## Validation Method 1: Syntax Validation

### How It Works
Syntax validation checks whether an email address conforms to the format defined in **RFC 5322** (the Internet Message Format standard). This is the fastest and most basic form of validation — it operates entirely on the string itself without any network calls.

### What It Catches
- Missing `@` symbol or multiple `@` symbols
- Missing local part (nothing before `@`) or missing domain part (nothing after `@`)
- Invalid characters in the local part (spaces, unescaped quotes, control characters)
- Invalid domain format (no TLD, spaces, missing dots where expected)
- Unquoted special characters that violate the specification

### Tools
- **Regex patterns**: Custom or library-provided regular expressions matching RFC 5322
- **Python `email.utils`**: The `parseaddr()` function for basic parsing
- **Python `email-validator` library**: A third-party package that performs comprehensive syntax checks including internationalized domain names (IDN)

### Limitations
Syntax validation **only checks format**, not deliverability. An email like `nobody.exists@gmail.com` passes every syntax check but is undeliverable. Syntax validation is necessary but never sufficient on its own.

### Python Code Example

```python
import re

# RFC 5322 compliant regex pattern (simplified practical version)
RFC_5322_PATTERN = re.compile(
    r"(^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$)"
)

def validate_syntax(email: str) -> dict:
    """Validate email syntax against RFC 5322 standard.

    Args:
        email: The email address to validate.

    Returns:
        Dictionary with 'is_valid' (bool) and 'error' (str or None).
    """
    email = email.strip()

    if not email:
        return {"is_valid": False, "error": "Empty email address"}

    if len(email) > 254:
        return {"is_valid": False, "error": "Email exceeds 254 character limit"}

    if RFC_5322_PATTERN.match(email):
        return {"is_valid": True, "error": None}
    else:
        return {"is_valid": False, "error": "Email does not match RFC 5322 format"}

# --- Usage ---
results = validate_syntax("john.doe@example.com")
print(results)
# {'is_valid': True, 'error': None}

results = validate_syntax("invalid-email@")
print(results)
# {'is_valid': False, 'error': 'Email does not match RFC 5322 format'}
```

---

## Validation Method 2: MX Record Lookup

### How It Works
MX (Mail Exchange) record lookup queries the Domain Name System (DNS) to determine whether the domain associated with an email address has active mail servers configured. Every domain that receives email must have at least one MX record pointing to a mail server that accepts incoming messages.

### What It Checks
- Does the domain exist? (NXDOMAIN check)
- Does the domain have one or more MX records?
- Are the MX record targets reachable (do they have A or AAAA records)?
- What are the priority values of the MX records (lower = higher priority)?

### Tools
- **Command line**: `dig MX example.com`, `nslookup -type=MX example.com`
- **Python `dns.resolver`**: Part of the `dnspython` library, provides programmatic DNS queries

### Python Code Example

```python
import dns.resolver
import dns.name

def check_mx_records(domain: str, timeout: float = 5.0) -> dict:
    """Check whether a domain has active MX records.

    Args:
        domain: The domain portion of the email address.
        timeout: DNS query timeout in seconds.

    Returns:
        Dictionary with 'mx_found' (bool), 'records' (list), and 'error' (str or None).
    """
    try:
        # Strip trailing dot if present
        domain = domain.rstrip(".")
        answers = dns.resolver.resolve(domain, "MX", lifetime=timeout)
        records = [
            {
                "preference": r.preference,
                "exchange": str(r.exchange).rstrip("."),
            }
            for r in answers
        ]
        # Sort by preference (lower = higher priority)
        records.sort(key=lambda x: x["preference"])
        return {
            "mx_found": True,
            "records": records,
            "error": None,
        }
    except dns.resolver.NXDOMAIN:
        return {"mx_found": False, "records": [], "error": "Domain does not exist (NXDOMAIN)"}
    except dns.resolver.NoAnswer:
        return {"mx_found": False, "records": [], "error": "No MX records found for domain"}
    except dns.resolver.NoNameservers:
        return {"mx_found": False, "records": [], "error": "No nameservers available for domain"}
    except dns.exception.Timeout:
        return {"mx_found": False, "records": [], "error": "DNS query timed out"}
    except Exception as e:
        return {"mx_found": False, "records": [], "error": f"Unexpected error: {str(e)}"}

# --- Usage ---
result = check_mx_records("gmail.com")
print(result)
# {'mx_found': True, 'records': [{'preference': 5, 'exchange': 'gmail-smtp-in.l.google.com'}, ...], 'error': None}

result = check_mx_records("thisdomaindoesnotexist12345.com")
print(result)
# {'mx_found': False, 'records': [], 'error': 'Domain does not exist (NXDOMAIN)'}
```

### Limitations
MX record lookup confirms that a **domain** accepts mail, but it does **not** verify whether a specific mailbox (e.g., `john.doe@`) exists on that server. A domain like `gmail.com` has active MX records, but `randomgarbage123456@gmail.com` is still an invalid address. MX checks should always be paired with SMTP verification.

---

## Validation Method 3: SMTP Verification

### How It Works
SMTP verification is the most accurate single validation method. It connects directly to the destination mail server (identified via MX records) and uses the SMTP protocol to ask whether a specific mailbox exists. The process involves:

1. Resolving the MX records for the domain to find the mail server hostname.
2. Opening a TCP connection to the mail server on port 25.
3. Initiating an SMTP session with `EHLO`.
4. Setting the sender with `MAIL FROM`.
5. Issuing `RCPT TO` with the target email address.
6. Reading the server's response code.
7. A **250** response means the mailbox exists; **550** or similar means it does not.

### What It Checks
- Does this **specific email address** exist on the destination mail server?
- Is the mailbox currently accepting mail?

### Tools
- **Python `smtplib`**: Built-in library for SMTP operations
- **Command line**: `telnet mail.example.com 25`, `swaks --to user@example.com`

### Python Code Example

```python
import smtplib
import socket
import dns.resolver
from email.utils import parseaddr, formataddr

def smtp_verify(email: str, timeout: float = 10.0, from_addr: str = "verify@example.com") -> dict:
    """Verify an email address via SMTP RCPT TO command.

    Args:
        email: The email address to verify.
        timeout: Connection and read timeout in seconds.
        from_addr: The sender address used in MAIL FROM.

    Returns:
        Dictionary with 'is_valid' (bool), 'response_code' (int or None),
        'response_msg' (str or None), and 'error' (str or None).
    """
    _, email = parseaddr(email)
    if "@" not in email:
        return {"is_valid": False, "response_code": None, "response_msg": None, "error": "Invalid email format"}

    domain = email.split("@")[1]

    # Step 1: Resolve MX records
    try:
        mx_answers = dns.resolver.resolve(domain, "MX", lifetime=timeout)
        mx_host = str(mx_answers[0].exchange).rstrip(".")
    except Exception as e:
        return {"is_valid": False, "response_code": None, "response_msg": None, "error": f"MX resolution failed: {str(e)}"}

    # Step 2: Connect and verify
    try:
        server = smtplib.SMTP(timeout=timeout)
        server.connect(mx_host, 25)
        server.ehlo_or_helo_if_needed()

        # Set sender
        code, msg = server.mail(from_addr)
        if code >= 300:
            server.quit()
            return {"is_valid": False, "response_code": code, "response_msg": str(msg), "error": "MAIL FROM rejected"}

        # Check recipient
        code, msg = server.rcpt(email)
        server.quit()

        if code == 250:
            return {
                "is_valid": True,
                "response_code": code,
                "response_msg": str(msg),
                "error": None,
            }
        elif code in (550, 551, 553, 554):
            return {
                "is_valid": False,
                "response_code": code,
                "response_msg": str(msg),
                "error": "Mailbox does not exist",
            }
        else:
            # 252 or other codes mean the server could not confirm
            return {
                "is_valid": None,  # inconclusive
                "response_code": code,
                "response_msg": str(msg),
                "error": f"Inconclusive response (code {code})",
            }

    except socket.timeout:
        return {"is_valid": None, "response_code": None, "response_msg": None, "error": "Connection timed out"}
    except smtplib.SMTPServerDisconnected:
        return {"is_valid": None, "response_code": None, "response_msg": None, "error": "Server disconnected unexpectedly"}
    except ConnectionRefusedError:
        return {"is_valid": None, "response_code": None, "response_msg": None, "error": "Connection refused (port 25 blocked)"}
    except socket.gaierror:
        return {"is_valid": None, "response_code": None, "response_msg": None, "error": "DNS resolution failed for mail server"}
    except Exception as e:
        return {"is_valid": None, "response_code": None, "response_msg": None, "error": f"Unexpected error: {str(e)}"}

# --- Usage ---
result = smtp_verify("existing.user@gmail.com")
print(result)
# {'is_valid': True, 'response_code': 250, 'response_msg': '2.1.5 OK', 'error': None}

result = smtp_verify("nonexistent.random.abc@gmail.com")
print(result)
# {'is_valid': False, 'response_code': 550, 'response_msg': '5.1.1 No such user', 'error': 'Mailbox does not exist'}
```

### Limitations
- **Greylisting**: Many mail servers temporarily reject first-time RCPT TO attempts to deter spammers. The email may actually exist, but the server returns a 450 or 451 code instead of confirming. A retry after a delay (typically 5–15 minutes) often succeeds.
- **Catch-all domains**: Some servers accept mail for any address at the domain (e.g., many corporate servers). These always return 250 regardless of whether the mailbox exists, making SMTP verification unreliable for those domains.
- **Rate limiting**: Servers may block or throttle verification attempts if too many come from the same IP in a short period.
- **Port 25 blocking**: Some networks (especially cloud providers and residential ISPs) block outbound connections on port 25, preventing SMTP verification entirely.

### Best Practices
- Always use appropriate timeouts (10 seconds is a good default).
- Handle greylisting by retrying failed checks after a delay.
- Space out verification requests to avoid rate limiting (recommend 1–2 seconds between checks for the same domain).
- Log all SMTP responses for debugging and audit purposes.
- Fall back to MX + syntax validation when SMTP verification is inconclusive.

---

## Validation Method 4: Disposable Email Detection

### How It Works
Disposable email detection checks whether an email address uses a domain from a known temporary or throwaway email service. These services generate email addresses on demand that auto-expire after a set period. They are commonly used to bypass sign-up forms, avoid spam, or hide identity — none of which are desirable for legitimate lead data.

### What It Catches
- Services like TempMail, Guerrilla Mail, 10 Minute Mail, and hundreds of similar providers.
- Emails registered through browser extensions or in-browser email generators.
- Domains that explicitly advertise themselves as temporary, disposable, or fake email providers.

### Common Disposable Email Domains (50+)

```
0-mail.com           10minutemail.com     20minutemail.com
33mail.com           60mail.to            aaathats3as.com
anonbox.net          antispam.de          beethoven10.com
binkmail.com         bobmail.info         brefmail.com
bsnow.net            bugmenot.com         cazmir.com
chammy.info          clipmail.eu          consumerriot.com
cosmorph.com         curryworld.de        cust.in
dacoolest.com        damnthespam.com      dayrep.com
dfgh.net             digitalsanctuary.com  disposableemailaddresses.email
disposableemailaddresses.emailmiser.com    disposableemailaddresses.fyi
dispostable.com      dodgit.com           donebyrate.com
e4ward.com           emailigo.de          emailsensei.com
emailtemporario.com.br  emailwarden.com   fammix.com
fakeinbox.com        faker.email          fastacura.com
filzmail.com         fizmail.com          fr33mail.info
get2mail.fr          gishpuppy.com        gorillawithagoldenheart.com
guerrillamail.com    guerrillamailblock.com  guerrillamail.de
guerrillamail.info   guerrillamail.net    guerrillamail.org
h.mintemail.com      haltospam.com        harakirimail.com
hat-geld.de          hotpop.com           igor.ch
ihateyoual.com       immediate-mail.com   inmynetwork.info
inboxes.com          incognitomail.org    instant-mail.de
ipoo.org             isafreak.com         junkmail.com
kasmail.com          killmail.com         klassmaster.com
klzlk.com            kmend.nz             landmail.co
lastmail.co          lavabit.com          letthemeatspam.com
lhsdv.com            lifebyfood.com       lilspam.com
loprk.com            lovebitco.in         lr78.com
m4ilweb.info         ma1l.bid            mailcatch.com
mailexpire.com       mailfreeonline.com   mailimate.com
mailinater.com       mailme.lv            mailmoat.com
mailnull.com         mailsac.com          mailsiphon.com
mailzilla.org        mbx.cc               mettl.com
mifarrell.com        mintemail.com        moakt.co
mobi.web.id          mobileninja.co.uk    montheye.com
mouchette.com        muchomail.com        mycleaninbox.net
mymail-in.net       mytempemail.com      nada.email
nbox.notif.me        neomailbox.com       nethack.pl
netmails.com         neverbox.com         nomail.xl.cx
nospamfor.us         nospamthanks.info    throwawayemailaddress.com
objectmail.com       obobbo.com           onewaymail.com
ordinaryamerican.net outln.com            ovtnbb.com
pancakemail.com      pookmail.com         privacy.net
proxymail.eu         rcpt.at              reallymymail.com
realtyalerts.ca      receivemail.info     regbypass.com
remail.cf            replacesmail.com     rtrtr.com
s0ny.net             safersignup.de       sbcglobal.net
schafmail.de         schrott-email.de     selfdestructingmail.com
sharklasers.com      shitmail.me          shortsushi.com
sinnlos-mail.de      smtp.li              smwg.co
sofimail.com         sooos.com            spamavert.com
spambog.com          spambox.us           spamcannon.com
spamcannon.net       spamcorptastic.com   spamday.com
spamex.com           spamfree24.org       spamfree24.com
spamgourmet.com      spamherelots.com     spamify.com
spammotel.com        spamobox.com         spamthis.co.uk
spamthisplease.com   suremail.info        tempail.com
tempinbox.com        tempmailaddress.com  tempmaildemo.com
tempmailer.com       tempmailo.com        tempmails.com
tempomail.fr         temporaryemail.net   temporaryforwarding.com
temporaryinbox.com   tempsnah.com         thecloudindex.com
thrma.com            tmail.ws             totemail.com
trash-mail.com       trashymail.com       trashymail.net
trbvn.com            trialmail.de         tryalert.com
twinmail.de          tyldd.com            uggsrock.com
veryrealemail.com    vtmp.org             vxnotes.com
wasteland.rfc822.org  webcontact.co.uk   wegwerfmail.de
wegwerfmail.net     wg0.com              wh4f.org
willselfdestruct.com  wuzup.net           wwjp.net
xagloo.com           xemaps.com           yopmail.com
yopmail.fr           yopmail.net          yourenotmyboss.com
yourtube.ml          yyt.is               za.com
zetmail.com          zippymail.info       zoemail.org
```

### Why This Matters for Lead Quality
Disposable emails are useless for outreach. They expire, the owners are not real business contacts, and sending to them provides zero return. More importantly, a high proportion of disposable emails in a campaign list is a signal of poor data quality that can affect campaign segmentation and reporting accuracy.

---

## Validation Method 5: Role-Based Email Detection

### How It Works
Role-based email detection identifies addresses that are not tied to a specific person but rather to a function, department, or position within an organization. These addresses typically start with generic prefixes that indicate a role rather than a name.

### Why Role Emails Matter
- **Lower engagement rates**: Role-based inboxes are often monitored by teams or auto-responders rather than decision-makers, resulting in lower open and reply rates.
- **Higher unsubscribe/complaint rates**: Role addresses on marketing lists generate more complaints because multiple people may access the inbox and not all consented.
- **Deliverability risk**: Some ESPs flag campaigns with high percentages of role-based addresses as potential spam.
- **Relationship building**: Personal emails (first.last@company.com) enable relationship-based selling, while role emails do not.

### Common Role-Based Prefixes

```
abuse@          admin@          admissions@    all@
archive@        billing@        careers@       complaints@
contact@        customerservice@  daemon@       data@
debug@          distribution@    dns@           domain@
enquiries@      enquiry@         finance@       ftp@
guest@          help@            helpdesk@      hostmaster@
info@           inquiries@       it@            jobs@
list@           log@             mail@          maintenance@
marketing@      no-reply@        noreply@       null@
office@         operations@      orders@        owner@
partner@        postmaster@      press@         privacy@
registrar@      requests@        returns@       root@
sales@          security@        service@       spam@
stats@          subscribe@       support@        sys@
system@         tech@            test@          unsubscribe@
user@           users@           uucp@          violence@
webmaster@      welcome@         www@
```

### When to Keep vs. Flag Role-Based Emails
- **Keep** if the role email is the only known contact for a business and the business is a high-value target.
- **Keep** if the email was explicitly listed as the contact point for inquiries on the business's own website.
- **Flag** for manual review if a role email could be supplemented with a personal email (e.g., finding the owner's name via LinkedIn or the company's team page).
- **Flag** in CRM systems with a `is_role_based` boolean so campaign managers can segment appropriately.

---

## Validation Pipeline Workflow

Every email collected by the English Nations Hub should pass through the following sequential pipeline. The pipeline is designed to be fast for obvious rejects and thorough for borderline cases.

```
COLLECT EMAIL
     |
     v
[Step 1] Syntax Validation (instant — <1ms)
     |
     +-- FAIL --> Mark INVALID (syntax error) --> Record metadata --> STOP
     |
     v
[Step 2] Disposable Email Check (instant — <1ms lookup)
     |
     +-- MATCH --> Mark INVALID (disposable domain) --> Record metadata --> STOP
     |
     v
[Step 3] Role-Based Email Detection (instant — <1ms lookup)
     |
     +-- MATCH --> Flag is_role_based = True --> Continue pipeline
     |
     v
[Step 4] MX Record Lookup (fast — ~100ms–1s per domain)
     |
     +-- FAIL --> Mark INVALID (no MX records) --> Record metadata --> STOP
     |
     v
[Step 5] SMTP Verification (slower — ~1s–5s per email)
     |
     +-- PASS (250) --> Mark VALIDATED --> Record metadata --> STOP
     |
     +-- FAIL (550) --> Mark INVALID --> Record metadata --> STOP
     |
     +-- INCONCLUSIVE (timeout/greylisting/452)
     |         |
     |         v
     |   Retry once after 60 seconds
     |         |
     |         +-- PASS --> Mark VALIDATED
     |         +-- FAIL --> Mark INVALID
     |         +-- STILL INCONCLUSIVE --> Mark PENDING VALIDATION --> Queue for retry
     |
     v
[Step 6] Assign Final Status & Record Metadata
```

### Step-by-Step Detail

1. **Collect email**: Email is gathered from a discovery source (website, directory, social profile, manual entry).
2. **Syntax validation** (instant): Regex and RFC 5322 check. Reject immediately on failure.
3. **Disposable check** (instant): Look up the domain against the disposable email list. Reject immediately on match.
4. **MX record lookup** (fast): DNS query for MX records. Reject if domain has no mail servers.
5. **SMTP verification** (slower): Connect to the mail server and verify the mailbox exists. Retry once on inconclusive results. Fall back to PENDING VALIDATION if still inconclusive after retry.
6. **Assign final status**: Based on the combined results of all steps, assign Validated, Pending Validation, or Invalid.
7. **Record validation metadata**: Store the results, methods used, timestamps, and response data for audit and debugging.

---

## Batch Validation Strategy

When validating large volumes of emails (hundreds or thousands), the pipeline must be optimized for throughput and respect for external systems.

### How to Validate Large Volumes Efficiently
- **Pre-filter with fast checks first**: Syntax and disposable checks are instant and CPU-only. Run them on the entire batch before making any network calls. This typically eliminates 10–20% of entries before any slow operations begin.
- **Cache MX results**: Multiple emails may share the same domain. Cache MX record lookups by domain to avoid redundant DNS queries.
- **Deduplicate before validating**: Remove exact duplicate emails from the batch. Deduplicate by domain for MX lookups.

### Rate Limiting Considerations
- **SMTP rate limits**: Most mail servers accept 10–30 RCPT TO verification attempts per minute from a single IP before throttling or blocking. Stay conservative: 1 request per 2 seconds to the same domain, 10 requests per second across different domains.
- **DNS rate limits**: Public DNS resolvers (Google 8.8.8.8, Cloudflare 1.1.1.1) handle thousands of queries per second, but DNS providers for specific domains may rate-limit. Use caching to minimize repeated lookups.
- **Exponential backoff**: If a server returns 421 or 452 (temporarily unavailable), back off exponentially (2s, 4s, 8s, 16s) rather than hammering the server.

### Priority-Based Validation
Validate high-value niches first:
1. **Tier 1** (immediate): Emails from priority niches, recently collected leads, emails needed for active campaigns.
2. **Tier 2** (within 24 hours): Standard leads from discovery operations.
3. **Tier 3** (within 72 hours): Bulk imports, older pending entries, lower-priority niches.

### Parallel Processing Recommendations
- Use asynchronous I/O (`asyncio` in Python) to run multiple DNS queries concurrently while respecting per-domain rate limits.
- Use thread pools for SMTP verification (each connection blocks on I/O), with a maximum of 10–20 concurrent connections.
- Process emails in batches of 100–500 for manageable memory usage and progress tracking.
- Persist intermediate results so a batch can resume from where it left off if interrupted.

---

## Validation Metadata

Every validated email in the repository must record the following metadata fields alongside the lead record. This metadata supports auditing, debugging, and quality analysis.

| Field                  | Type   | Description                                              |
|------------------------|--------|----------------------------------------------------------|
| `email_address`        | string | The email address that was validated                     |
| `validation_status`    | enum   | One of: `Validated`, `Pending Validation`, `Invalid`     |
| `validation_date`      | string | ISO 8601 timestamp of when validation was performed      |
| `methods_used`         | string | Comma-separated list of methods applied                  |
| `smtp_response`        | string | Full SMTP response string (if SMTP method was used)      |
| `smtp_response_code`   | int    | Numeric SMTP response code (e.g., 250, 550)              |
| `mx_records_found`     | bool   | Whether MX records were found for the domain             |
| `mx_records`           | string | JSON array of MX record details (preference, exchange)   |
| `is_disposable`        | bool   | Whether the domain is a known disposable email provider   |
| `is_role_based`        | bool   | Whether the email uses a known role-based prefix         |
| `syntax_valid`         | bool   | Whether the email passed syntax validation                |
| `validated_by`         | string | Agent ID or process name that performed the validation   |
| `validation_duration`  | float  | Total time taken to validate in seconds                  |
| `retry_count`          | int    | Number of retries performed (for SMTP greylisting)       |

---

## Common Email Patterns by Region

Understanding regional email domain patterns helps anticipate the types of addresses encountered during discovery and informs expectations for deliverability and response rates.

### United States
- **Personal**: gmail.com, yahoo.com, outlook.com, hotmail.com, aol.com, icloud.com, protonmail.com
- **Business**: company.com (custom domains), outlook.com (Microsoft 365)

### United Kingdom
- **Personal**: gmail.com, outlook.com, yahoo.co.uk, hotmail.co.uk, btinternet.com, sky.com, virginmedia.com
- **Business**: co.uk domains are dominant; many businesses use Google Workspace or Microsoft 365

### Nigeria
- **Personal**: gmail.com, yahoo.com, outlook.com, hotmail.com
- **Business**: Custom .ng, .com.ng, and .com domains; increasing use of Google Workspace

### Ghana
- **Personal**: gmail.com, yahoo.com, hotmail.com, outlook.com
- **Business**: Custom .gh, .com.gh, and .com domains

### South Africa
- **Personal**: gmail.com, webmail.co.za, mweb.co.za, telkomsa.net, iafrica.com
- **Business**: Custom .co.za, .co.za with Google Workspace

### Canada
- **Personal**: gmail.com, outlook.com, yahoo.ca, bell.net, rogers.com, shaw.ca
- **Business**: .ca domains common alongside .com

### Australia
- **Personal**: gmail.com, outlook.com, bigpond.com, iinet.net.au, optusnet.com.au
- **Business**: .com.au domains dominant; heavy Google Workspace adoption

### New Zealand
- **Personal**: gmail.com, outlook.com, xtra.co.nz, vodafone.co.nz, paradise.net.nz
- **Business**: .co.nz and .nz domains

### Jamaica
- **Personal**: gmail.com, yahoo.com, hotmail.com
- **Business**: .com.jm and .jm domains, plus .com

### Common Business Email Patterns (All Regions)
Regardless of country, the following generic business email prefixes are ubiquitous:
- `info@`, `contact@`, `hello@`, `sales@`, `support@`, `enquiries@`, `admin@`, `office@`, `bookings@`, `reservations@`

---

## Validation Tools & Libraries

### Python Libraries
- **`email-validator`** (pip install email-validator): Comprehensive syntax and deliverability validation. Handles IDN domains, checks MX records, and provides detailed validation results. Recommended as the first-choice library for most validation needs.
- **`dnspython`** (pip install dnspython): Full-featured DNS toolkit for programmatic MX, A, AAAA, TXT, and other DNS record queries. Used under the hood by `email-validator` and essential for custom MX lookup logic.
- **`smtplib`** (built-in): Python's standard library SMTP client. Used for direct SMTP verification as demonstrated in the code examples above.
- **`aiosmtplib`** (pip install aiosmtplib): Async-compatible SMTP client for parallel verification workflows.
- **`valid_email`** (pip install valid-email): Lightweight syntax checker with disposable email detection.

### API Services
Several third-party APIs provide email validation as a service (e.g., Hunter.io, NeverBounce, ZeroBounce, Abstract API). These are not required for repository operations but may be useful for high-volume validation where self-hosted SMTP verification is impractical due to rate limiting or port 25 blocking. When evaluating API services, consider their throughput limits, pricing per verification, and whether they provide the full metadata needed for the repository schema.

### Command-Line Tools
- **`dig`**: DNS lookup utility. Usage: `dig MX example.com +short` for quick MX record checks.
- **`nslookup`**: Alternative DNS tool available on most operating systems. Usage: `nslookup -type=MX example.com`.
- **`swaks`** (Swiss Army Knife for SMTP): Advanced SMTP testing tool that can perform RCPT TO verification from the command line. Usage: `swaks --to user@example.com --server mail.example.com`.
- **`host`**: Simple DNS lookup. Usage: `host -t MX example.com`.

---

*This document is maintained as part of the English Nations Hub repository. Update it whenever validation methods, tools, or regional patterns change. For questions about validation implementation, contact the data quality team.*
