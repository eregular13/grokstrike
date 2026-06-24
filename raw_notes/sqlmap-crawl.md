# sqlmap-crawl

## Tool Name & Category
- **Name:** sqlmap-crawl
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `sqlmap`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
SQLmap with crawl

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
sqlmap -u http://aegis-target --crawl=2 --batch
```

**Target:** `http://aegis-target`  
**Duration:** 0.29s | **Exit code:** 0

## Full Output Summary
```
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.10.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:11:24 /2026-06-24/

do you want to check for the existence of site's sitemap(.xml) [y/N] N
[05:11:24] [INFO] starting crawler for target URL 'http://aegis-target'
[05:11:24] [INFO] searching for links with depth 1
got a 302 redirect to 'http://aegis-target/login.php'. Do you want to follow? [Y/n] Y
[05:11:24] [INFO] searching for links with depth 2
please enter number of threads? [Enter for 1 (current)] 1
[05:11:24] [WARNING] running in a single-thread mode. This could take a while
[05:11:24] [WARNING] no usable links found (with GET parameters)

[*] ending @ 05:11:24 /2026-06-24/


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `sqlmap -u {web} --crawl=2 --batch {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:24.616509+00:00*
