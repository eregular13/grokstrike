# testdisk

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `testdisk` ✅ installed |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Partition recovery

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
testdisk /list /workspace/disk.img
```

| Metric | Value |
|--------|-------|
| Duration | 0.1s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
TestDisk 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org
Please wait...
Disk /workspace/disk.img - 1048 KB / 1024 KiB - CHS 1 255 63
Sector size:512


Disk /workspace/disk.img - 1048 KB / 1024 KiB - CHS 1 255 63
     Partition			Start        End    Size in sectors


```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `testdisk /list /workspace/disk.img {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `testdisk --help` and tune `testdisk /list /workspace/disk.img {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:30.989735+00:00*
