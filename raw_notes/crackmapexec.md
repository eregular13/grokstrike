# crackmapexec

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `crackmapexec` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Network pentest Swiss army knife

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
crackmapexec smb aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.69s |
| Exit code | 0 |
| Effectiveness | **5/10** — Ran successfully, limited findings |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `crackmapexec smb {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `crackmapexec --help` and tune `crackmapexec smb {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:03.969314+00:00*
