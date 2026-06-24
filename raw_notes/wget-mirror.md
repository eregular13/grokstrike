# wget-mirror

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `wget` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Mirror web content

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
wget -mk http://aegis-target -P /results/
```

| Metric | Value |
|--------|-------|
| Duration | 0.14s |
| Exit code | 0 |
| Effectiveness | **5/10** — Ran successfully, limited findings |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
--2026-06-24 05:47:43--  http://aegis-target/
Resolving aegis-target (aegis-target)... 172.22.0.2
Connecting to aegis-target (aegis-target)|172.22.0.2|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: login.php [following]
--2026-06-24 05:47:43--  http://aegis-target/login.php
Reusing existing connection to aegis-target:80.
HTTP request sent, awaiting response... 200 OK
Length: 1523 (1.5K) [text/html]
Saving to: ‘/results/aegis-target/index.html’

     0K .                                                     100%  202M=0s

Last-modified header missing -- time-stamps turned off.
2026-06-24 05:47:43 (202 MB/s) - ‘/results/aegis-target/index.html’ saved [1523/1523]

Loading robots.txt; please ignore errors.
--2026-06-24 05:47:43--  http://aegis-target/robots.txt
Reusing existing connection to aegis-target:80.
HTTP request sent, awaiting response... 200 OK
Length: 26 [text/plain]
Saving to: ‘/results/aegis-target/robots.txt’

     0K                                                       100% 4.79M=0s

2026-06-24 05:47:43 (4.79 MB/s) - ‘/results/aegis-target/robots.txt’ saved [26/26]

FINISHED --2026-06-24 05:47:43--
Total wall clock time: 0.03s
Downloaded: 2 files, 1.5K in 0s (119 MB/s)
Converting links in /results/aegis-target/index.html... 3.
1-2
Converted links in 1 files in 0.005 seconds.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `wget -mk {web} -P /results/ {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `wget --help` and tune `wget -mk {web} -P /results/ {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:43.292749+00:00*
