# curl-headers

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `curl` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Fetch response headers

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
curl -sI http://aegis-target 2>&1
```

| Metric | Value |
|--------|-------|
| Duration | 0.09s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Server version:** Apache/2.4.25

## Full Output Summary
```
HTTP/1.1 302 Found
Date: Wed, 24 Jun 2026 05:47:42 GMT
Server: Apache/2.4.25 (Debian)
Set-Cookie: PHPSESSID=k8df89akam2a0i2dm9fr2oofn3; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=k8df89akam2a0i2dm9fr2oofn3; path=/
Set-Cookie: security=low
Location: login.php
Content-Type: text/html; charset=UTF-8


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `curl -sI {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `curl --help` and tune `curl -sI {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:42.831331+00:00*
