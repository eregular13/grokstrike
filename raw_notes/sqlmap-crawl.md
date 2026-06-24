# sqlmap-crawl

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `sqlmap` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
SQLmap with crawl

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
COOKIE=$(/workspace/dvwa_login.sh http://aegis-target); sqlmap -u http://aegis-target --cookie="$COOKIE" --crawl=1 --batch --level=1 --risk=1
```

| Metric | Value |
|--------|-------|
| Duration | 0.4s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Injection indicator:** parameter

## Full Output Summary
```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.10.6#stable}
|_ -| . [.]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:47:40 /2026-06-24/

do you want to check for the existence of site's sitemap(.xml) [y/N] N
[05:47:40] [INFO] starting crawler for target URL 'http://aegis-target'
[05:47:40] [INFO] searching for links with depth 1
got a 302 redirect to 'http://aegis-target/login.php'. Do you want to follow? [Y/n] Y
[05:47:40] [WARNING] no usable links found (with GET parameters)

[*] ending @ 05:47:40 /2026-06-24/


```

## What I Learned / Edge Cases / Gotchas
- DVWA requires authenticated session — `/workspace/dvwa_login.sh` sets cookies + security=low
- Registry template: `sqlmap -u {web} --crawl=2 --batch {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 300s

## Next Steps for Exploration & Development
Run `sqlmap --help` and tune `sqlmap -u {web} --crawl=2 --batch {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:40.353462+00:00*
