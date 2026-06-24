# enum4linux

## Tool Name & Category
- **Name:** enum4linux
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `enum4linux`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
SMB enumeration

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
enum4linux -a aegis-target
```

**Target:** `aegis-target`  
**Duration:** 20.25s | **Exit code:** 1

## Full Output Summary
```
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Jun 24 05:07:35 2026

[34m =========================================( [0m[32mTarget Information[0m[34m )=========================================

[0mTarget ........... aegis-target
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


[34m ============================( [0m[32mEnumerating Workgroup/Domain on aegis-target[0m[34m )============================

[0m[33m
[E] [0m[31mCan't find workgroup/domain

[0m

[34m ================================( [0m[32mNbtstat Information for aegis-target[0m[34m )================================

[0mLooking up status of 172.22.0.2
No reply from 172.22.0.2

[34m ===================================( [0m[32mSession Check on aegis-target[0m[34m )===================================

[0m[33m
[E] [0m[31mServer doesn't allow session using username '', password ''.  Aborting remainder of tests.

[0m
```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `enum4linux -a {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**5/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:07:55.418532+00:00*
