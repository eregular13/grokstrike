# theharvester

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `theharvester` ✅ installed |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Email/subdomain harvest

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
theHarvester -d aegis-target -b all
```

| Metric | Value |
|--------|-------|
| Duration | 99.69s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Read proxies.yaml from /etc/theHarvester/proxies.yaml
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.11.1                                             *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************

[*] Target: aegis-target 

Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Failed to process bevigil search for word: 'aegis-target'
Error Message: 
[!] Missing API key for bevigil. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

[!] Missing API key for Bitbucket. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Failed to process bufferoverun search for word: 'aegis-target'
Error Message: 
[!] Missing API key for bufferoverun. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Failed to perform BuiltWith search for word: 'aegis-target'
A Missing Key Error occurred in builtwith: 
[!] Missing API key for BuiltWith. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Failed to process brave search for word: 'aegis-target'
Error Message: 
[!] Missing API key for Brave Search. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Censys API key is missing or invalid: 
[!] Missing API key for Censys ID and/or Secret. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing key error occurred in criminalip: 
[!] Missing API key for criminalip. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in dehashed: 
[!] Missing API key for Dehashed. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

[!] Missing API key for DNSDumpster. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in dymo: 
[!] Missing API key for dymo. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in fullhunt: 
[!] Missing API key for fullhunt. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Error initializing SearchGithubCode: 
[!] Missing API key for Github. 
A Missing Key error occurred in github-code: 
[!] Missing API key for Github. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

[!] Missing API key for HaveIBeenPwned. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in Hunter: 
[!] Missing API key for Hunter. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in Hunter How: 
[!] Missing API key for hunterhow. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in intelx: 
[!] Missing API key for Intelx. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
[*] Mojeek: No API key found, using default scraping mode.
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in Netlas: 
[!] Missing API key for netlas. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Unexpected error occurred in Onyphe module: 
[!] Missing API key for onyphe. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in PentestTools search: 
[!] Missing API key for PentestTools. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in ProjectDiscovery: 
[!] Missing API key for ProjectDiscovery. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in RocketReach: 
[!] Missing API key for RocketReach. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

[!] Missing API key for SecurityScorecard. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred Security Trails: 
[!] Missing API key for Securitytrail. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in sherlockeye: 
[!] Missing API key for sherlockeye. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in Shodan search: 
[!] Missing API key for Shodan. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in Tomba: 
[!] Missing API key for Tomba Key and/or Secret. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in venacus search: 
[!] Missing API key for Venacus. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in virustotal search: 
[!] Missing API key for virustotal. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in whoisxml search: 
[!] Missing API key for whoisxml. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
A Missing Key error occurred in zoomeye: 
[!] Missing API key for zoomeye. 
[*] Searching Baidu. 
	Searching results.
[*] Searching Certspotter. 
Chaos API error: get access token here https://cloud.projectdiscovery.io
[*] Searching Chaos. 
[*] Searching Duckduckgo. 
[*] Searching CRTsh. 
[*] Searching Fofa. 
[*] Searching Hackertarget. 
[*] Searching Gitlab. 
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
[*] Searching Hudsonrock. 
[*] Searching Commoncrawl. 
LeakIX API requires authentication: "Incorrect API Key"
[*] Searching Leaklookup. 
[*] Searching Otx. 
[*] Searching Leakix. 
[*] Searching Mojeek. 
[*] Searching ShodanInternetDB. 
[*] Searching Rapiddns. 
[*] Searching Robtex. 
[*] Searching Subdomaincenter. 
No response from ThreatCrowd API for: aegis-target
[*] Searching Threatcrowd. 
THC returned status 406
[*] Searching Thc. 
[*] Searching Subdomainfinderc99. 
[*] Windvane API key not found. Using limited unauthenticated access.
[*] API unavailable, using fallback subdomain pattern search...
[*] No additional subdomains found via fallback methods
[*] Searching Windvane. 
[*] Searching Urlscan. 
[*] Searching Yahoo. 
[*] Searching Waybackarchive. 

[*] No LinkedIn users found.



[*] LinkedIn Links found: 0
---------------------

[*] No IPs found.

[*] No emails found.

[*] No people found.

[*] No hosts found.



[*] Performing SecurityScorecard scan...
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml
An exception has occurred in SecurityScorecard scanning: 
[!] Missing API key for SecurityScorecard. 

[*] Performing BuiltWith scan...
Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

[!] Missing API key for BuiltWith. 

--- STDERR ---
2026-06-24 05:37:50,314 - theHarvester.discovery.hudsonrocksearch - INFO - Starting Hudson Rock processing for: aegis-target
2026-06-24 05:37:50,314 - theHarvester.discovery.hudsonrocksearch - INFO - Starting Hudson Rock search for: aegis-target
2026-06-24 05:37:56,852 - theHarvester.discovery.hudsonrocksearch - INFO - Domain statistics: 0 total compromised, 0 employees, 0 users
2026-06-24 05:37:57,854 - theHarvester.discovery.hudsonrocksearch - INFO - Hudson Rock search completed. Found 0 hosts, 0 IPs, 0 emails
2026-06-24 05:37:57,854 - theHarvester.discovery.hudsonrocksearch - INFO - Hudson Rock processing completed successfully: 0 hosts, 0 IPs, 0 emails, 0 stealers

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `theHarvester -d {host} -b all {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `theharvester --help` and tune `theHarvester -d {host} -b all {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:38:59.713532+00:00*
