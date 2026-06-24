# dirsearch

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `dirsearch` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Advanced directory discovery

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
dirsearch -u http://aegis-target --quiet
```

| Metric | Value |
|--------|-------|
| Duration | 13.23s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
[05:47:20] 200 -   57B  - http://aegis-target/.gitignore
[05:47:20] 403 -  298B  - http://aegis-target/.ht_wsr.txt
[05:47:20] 403 -  301B  - http://aegis-target/.htaccess.bak1
[05:47:20] 403 -  301B  - http://aegis-target/.htaccess.orig
[05:47:20] 403 -  301B  - http://aegis-target/.htaccess.save
[05:47:20] 403 -  303B  - http://aegis-target/.htaccess.sample
[05:47:20] 403 -  301B  - http://aegis-target/.htaccess_orig
[05:47:20] 403 -  302B  - http://aegis-target/.htaccess_extra
[05:47:20] 403 -  299B  - http://aegis-target/.htaccessBAK
[05:47:20] 403 -  299B  - http://aegis-target/.htaccess_sc
[05:47:20] 403 -  300B  - http://aegis-target/.htaccessOLD2
[05:47:20] 403 -  299B  - http://aegis-target/.htaccessOLD
[05:47:20] 403 -  291B  - http://aegis-target/.htm
[05:47:20] 403 -  292B  - http://aegis-target/.html
[05:47:20] 403 -  297B  - http://aegis-target/.htpasswds
[05:47:20] 403 -  301B  - http://aegis-target/.htpasswd_test
[05:47:20] 403 -  298B  - http://aegis-target/.httr-oauth
[05:47:21] 403 -  292B  - http://aegis-target/.php3
[05:47:21] 403 -  291B  - http://aegis-target/.php
[05:47:22] 200 -    2KB - http://aegis-target/about.php
[05:47:25] 200 -    7KB - http://aegis-target/CHANGELOG.md
[05:47:25] 301 -  313B  - http://aegis-target/config  ->  http://aegis-target/config/
[05:47:25] 200 -  469B  - http://aegis-target/config/
[05:47:26] 301 -  311B  - http://aegis-target/docs  ->  http://aegis-target/docs/
[05:47:26] 200 -  486B  - http://aegis-target/docs/
[05:47:26] 200 -  471B  - http://aegis-target/dvwa/
[05:47:26] 200 -    1KB - http://aegis-target/favicon.ico
[05:47:28] 200 -  697B  - http://aegis-target/login.php
[05:47:29] 200 -  148B  - http://aegis-target/php.ini
[05:47:30] 200 -    9KB - http://aegis-target/README.md
[05:47:30] 200 -   26B  - http://aegis-target/robots.txt
[05:47:30] 403 -  300B  - http://aegis-target/server-status
[05:47:30] 403 -  301B  - http://aegis-target/server-status/
[05:47:30] 200 -    2KB - http://aegis-target/setup.php

--- STDERR ---
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `dirsearch -u {web} --quiet {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `dirsearch --help` and tune `dirsearch -u {web} --quiet {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:33.105593+00:00*
