# feroxbuster

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `feroxbuster` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Recursive content discovery

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
feroxbuster -u http://aegis-target -w /usr/share/wordlists/dirb/common.txt -q --time-limit 120s
```

| Metric | Value |
|--------|-------|
| Duration | 2.82s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- See output summary for raw tool data.

## Full Output Summary
```
403      GET       11l       32w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

404      GET        9l       32w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

302      GET        0l        0w        0c http://aegis-target/ => login.php

301      GET        9l       28w      313c http://aegis-target/config => http://aegis-target/config/

200      GET       47l      282w     1864c http://aegis-target/config/config.inc.php.dist

200      GET        0l        0w        0c http://aegis-target/config/config.inc.php

301      GET        9l       28w      311c http://aegis-target/docs => http://aegis-target/docs/

404      GET        9l       34w      298c http://aegis-target/Documents%20and%20Settings

301      GET        9l       28w      315c http://aegis-target/external => http://aegis-target/external/

200      GET        2l        6w     1688c http://aegis-target/favicon.ico

200      GET        0l        0w        0c http://aegis-target/external/recaptcha/recaptchalib.php

302      GET        0l        0w        0c http://aegis-target/index.php => login.php

200      GET        5l       20w      148c http://aegis-target/php.ini

302      GET        0l        0w        0c http://aegis-target/phpinfo.php => login.php

404      GET        9l       33w      289c http://aegis-target/Program%20Files

404      GET        9l       33w      288c http://aegis-target/reports%20list

200      GET        2l        4w       26c http://aegis-target/robots.txt

200      GET     2922l    17217w   730335c http://aegis-target/docs/DVWA_v1.3.pdf

200      GET        1l       10w      105c http://aegis-target/docs/pdf.html

301      GET        9l       28w      326c http://aegis-target/external/phpids/0.6 => http://aegis-target/external/phpids/0.6/


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `feroxbuster -u {web} -q {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Add `-x php,txt,bak,old` extensions for PHP targets like DVWA.

---
*GrokStrike v2 — 2026-06-24T05:47:19.764523+00:00*
