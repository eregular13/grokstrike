# kerbrute

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `kerbrute` ❌ missing |
| **Agent** | exploit |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Kerberos user enum

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
kerbrute userenum --dc aegis-target -d domain.local /workspace/users.txt
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
command not found: kerbrute
```

## What I Learned / Edge Cases / Gotchas
- `kerbrute` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `kerbrute userenum --dc {host} -d domain.local /workspace/users.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `kerbrute --help` and tune `kerbrute userenum --dc {host} -d domain.local /workspace/users.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:52.937595+00:00*
