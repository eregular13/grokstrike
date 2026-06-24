# enum4linux

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `enum4linux` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
SMB enumeration

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
enum4linux -a aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 20.24s |
| Exit code | 1 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Jun 24 05:40:00 2026

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
- Executed successfully in isolated lab
- Registry template: `enum4linux -a {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `enum4linux --help` and tune `enum4linux -a {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:40:20.628043+00:00*
