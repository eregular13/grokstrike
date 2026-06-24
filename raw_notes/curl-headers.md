# curl-headers

## Tool Name & Category
- **Name:** curl-headers
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `curl`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Fetch response headers

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
curl -sI http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.1s | **Exit code:** 0

## Full Output Summary
```
HTTP/1.1 302 Found
Date: Wed, 24 Jun 2026 05:11:26 GMT
Server: Apache/2.4.25 (Debian)
Set-Cookie: PHPSESSID=pk7vk12vavh1oor0mhidqh6i82; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=pk7vk12vavh1oor0mhidqh6i82; path=/
Set-Cookie: security=low
Location: login.php
Content-Type: text/html; charset=UTF-8


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `curl -sI {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.428741+00:00*
