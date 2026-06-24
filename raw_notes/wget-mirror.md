# wget-mirror

## Tool Name & Category
- **Name:** wget-mirror
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `wget`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Mirror web content

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
wget -mk http://aegis-target -P /results/
```

**Target:** `http://aegis-target`  
**Duration:** 0.11s | **Exit code:** 0

## Full Output Summary
```
--2026-06-24 05:11:26--  http://aegis-target/
Resolving aegis-target (aegis-target)... 172.22.0.2
Connecting to aegis-target (aegis-target)|172.22.0.2|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: login.php [following]
--2026-06-24 05:11:26--  http://aegis-target/login.php
Reusing existing connection to aegis-target:80.
HTTP request sent, awaiting response... 200 OK
Length: 1523 (1.5K) [text/html]
Saving to: ‘/results/aegis-target/index.html’

     0K .                                                     100%  132M=0s

Last-modified header missing -- time-stamps turned off.
2026-06-24 05:11:26 (132 MB/s) - ‘/results/aegis-target/index.html’ saved [1523/1523]

Loading robots.txt; please ignore errors.
--2026-06-24 05:11:26--  http://aegis-target/robots.txt
Reusing existing connection to aegis-target:80.
HTTP request sent, awaiting response... 200 OK
Length: 26 [text/plain]
Saving to: ‘/results/aegis-target/robots.txt’

     0K                                                       100% 5.03M=0s

2026-06-24 05:11:26 (5.03 MB/s) - ‘/results/aegis-target/robots.txt’ saved [26/26]

FINISHED --2026-06-24 05:11:26--
Total wall clock time: 0.01s
Downloaded: 2 files, 1.5K in 0s (92.8 MB/s)
Converting links in /results/aegis-target/index.html... 3.
1-2
Converted links in 1 files in 0.005 seconds.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `wget -mk {web} -P /results/ {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.651339+00:00*
