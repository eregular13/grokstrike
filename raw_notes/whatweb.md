# whatweb

## Tool Name & Category
- **Name:** whatweb
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `whatweb`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Web technology fingerprint

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
whatweb -a 3 http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 19.41s | **Exit code:** 0

## Full Output Summary
```
[1m[34mhttp://aegis-target/[0m [302 Found] [1mApache[0m[[1m[32m2.4.25[0m], [1mCookies[0m[[0m[22mPHPSESSID,security[0m], [1mCountry[0m[[0m[22mRESERVED[0m][[1m[31mZZ[0m], [1mHTTPServer[0m[[1m[31mDebian Linux[0m][[1m[36mApache/2.4.25 (Debian)[0m], [1mIP[0m[[0m[22m172.22.0.2[0m], [1mRedirectLocation[0m[[0m[22mlogin.php[0m]
[1m[34mhttp://aegis-target/login.php[0m [200 OK] [1mApache[0m[[1m[32m2.4.25[0m], [1mCountry[0m[[0m[22mRESERVED[0m][[1m[31mZZ[0m], [1mDVWA[0m, [1mHTTPServer[0m[[1m[31mDebian Linux[0m][[1m[36mApache/2.4.25 (Debian)[0m], [1mIP[0m[[0m[22m172.22.0.2[0m], [1mPHP[0m, [1mPasswordField[0m[[0m[22mpassword[0m], [1mTitle[0m[[1m[33mLogin :: Damn Vulnerable Web Application (DVWA) v1.10 *Development*[0m]

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `whatweb -a 3 {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:54.636201+00:00*
