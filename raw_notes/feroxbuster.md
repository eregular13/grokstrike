# feroxbuster

## Tool Name & Category
- **Name:** feroxbuster
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `feroxbuster`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Recursive content discovery

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
feroxbuster -u http://aegis-target -q
```

**Target:** `http://aegis-target`  
**Duration:** 6.13s | **Exit code:** 0

## Full Output Summary
```
403      GET       11l       32w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

404      GET        9l       32w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

302      GET        0l        0w        0c http://aegis-target/ => login.php

301      GET        9l       28w      311c http://aegis-target/docs => http://aegis-target/docs/

301      GET        9l       28w      313c http://aegis-target/config => http://aegis-target/config/

200      GET        1l       10w      105c http://aegis-target/docs/pdf.html

301      GET        9l       28w      315c http://aegis-target/external => http://aegis-target/external/

200      GET     2922l    17217w   730335c http://aegis-target/docs/DVWA_v1.3.pdf

404      GET        9l       33w      288c http://aegis-target/Reports%20List

404      GET        9l       33w      290c http://aegis-target/external%20files

200      GET       47l      282w     1864c http://aegis-target/config/config.inc.php.dist

200      GET        0l        0w        0c http://aegis-target/config/config.inc.php

404      GET        9l       33w      286c http://aegis-target/modern%20mom

404      GET        9l       34w      291c http://aegis-target/neuf%20giga%20photo

200      GET        0l        0w        0c http://aegis-target/external/recaptcha/recaptchalib.php

301      GET        9l       28w      326c http://aegis-target/external/phpids/0.6 => http://aegis-target/external/phpids/0.6/

404      GET        9l       33w      290c http://aegis-target/Web%20References

404      GET        9l       33w      286c http://aegis-target/Contact%20Us

404      GET        9l       33w      285c http://aegis-target/Home%20Page

404      GET        9l       33w      290c http://aegis-target/Planned%20Giving

404      GET        9l       33w      290c http://aegis-target/Press%20Releases

404      GET        9l       33w      288c http://aegis-target/Bequest%20Gift


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `feroxbuster -u {web} -q {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:20.770326+00:00*
