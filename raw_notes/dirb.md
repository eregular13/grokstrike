# dirb

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `dirb` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Web content scanner

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
dirb http://aegis-target /usr/share/wordlists/dirb/common.txt -S -r
```

| Metric | Value |
|--------|-------|
| Duration | 0.82s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Jun 24 05:47:33 2026
URL_BASE: http://aegis-target/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt
OPTION: Not Recursive
OPTION: Silent Mode

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://aegis-target/ ----
==> DIRECTORY: http://aegis-target/config/
==> DIRECTORY: http://aegis-target/docs/
==> DIRECTORY: http://aegis-target/external/
+ http://aegis-target/favicon.ico (CODE:200|SIZE:1406)
+ http://aegis-target/index.php (CODE:302|SIZE:0)
+ http://aegis-target/php.ini (CODE:200|SIZE:148)
+ http://aegis-target/phpinfo.php (CODE:302|SIZE:0)
+ http://aegis-target/robots.txt (CODE:200|SIZE:26)
+ http://aegis-target/server-status (CODE:403|SIZE:300)

-----------------
END_TIME: Wed Jun 24 05:47:34 2026
DOWNLOADED: 4612 - FOUND: 6

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `dirb {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `dirb --help` and tune `dirb {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:34.497245+00:00*
