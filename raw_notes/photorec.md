# photorec

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `photorec` ✅ installed |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
File recovery

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
photorec /log /workspace/recovery
```

| Metric | Value |
|--------|-------|
| Duration | 0.1s |
| Exit code | 1 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- **Open port/service:** open file or

## Full Output Summary
```
PhotoRec 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org

Unable to open file or device /workspace/recovery: No such file or directory

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `photorec /log /workspace/recovery {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `photorec --help` and tune `photorec /log /workspace/recovery {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:30.798419+00:00*
