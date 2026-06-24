# whatweb

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `whatweb` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Web technology fingerprint

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
whatweb -a 3 -v http://aegis-target 2>&1 | head -40
```

| Metric | Value |
|--------|-------|
| Duration | 19.46s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Server version:** Apache/2.4.25
- **Server version:** Apache/2.4.25

## Full Output Summary
```
WhatWeb report for [1m[34mhttp://aegis-target/[0m
Status    : 302 Found
Title     : [1m[33m<None>[0m
IP        : 172.22.0.2
Country   : [1m[31mRESERVED, ZZ[0m

Summary   : [1mApache[0m[[1m[32m2.4.25[0m], [1mCookies[0m[[0m[22mPHPSESSID,security[0m], [1mHTTPServer[0m[[1m[31mDebian Linux[0m][[1m[36mApache/2.4.25 (Debian)[0m], [1mRedirectLocation[0m[[0m[22mlogin.php[0m]

Detected Plugins:
[ [1mApache[0m ]
	The Apache HTTP Server Project is an effort to develop and 
	maintain an open-source HTTP server for modern operating 
	systems including UNIX and Windows NT. The goal of this 
	project is to provide a secure, efficient and extensible 
	server that provides HTTP services in sync with the current 
	HTTP standards. 

	Version      : [1m[32m2.4.25[0m (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ [1mCookies[0m ]
	Display the names of cookies in the HTTP headers. The 
	values are not returned to save on space. 

	String       : [1m[36mPHPSESSID[0m
	String       : [1m[36mPHPSESSID[0m
	String       : [1m[36msecurity[0m

[ [1mHTTPServer[0m ]
	HTTP server header string. This plugin also attempts to 
	identify the operating system from the server header. 

	OS           : [1m[31mDebian Linux[0m
	String       : [1m[36mApache/2.4.25 (Debian)[0m (from server string)

[ [1mRedirectLocation[0m ]
	HTTP Server string location. used with http-status 301 and 
	302 


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `whatweb -a 3 {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 90s

## Next Steps for Exploration & Development
Combine with `httpx -tech-detect` for pipeline fingerprinting.

---
*GrokStrike v2 — 2026-06-24T05:41:34.949040+00:00*
