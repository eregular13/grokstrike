# evil-winrm

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `evil-winrm` ❌ missing |
| **Agent** | auth |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
WinRM shell

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
evil-winrm -i aegis-target -u administrator -p password
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
command not found: evil-winrm
```

## What I Learned / Edge Cases / Gotchas
- `evil-winrm` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `evil-winrm -i {host} -u administrator -p password {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `evil-winrm --help` and tune `evil-winrm -i {host} -u administrator -p password {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:53.407964+00:00*
