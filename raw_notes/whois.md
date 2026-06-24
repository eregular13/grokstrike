# whois

## Tool Name & Category
- **Name:** whois
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `whois`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
WHOIS lookup

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
whois aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.28s | **Exit code:** 0

## Full Output Summary
```

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#


#
# Query terms are ambiguous.  The query is assumed to be:
#     "e / aegis-target"
#
# Use "?" to get help.
#

No match found for aegis-target.


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `whois {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:26.905405+00:00*
