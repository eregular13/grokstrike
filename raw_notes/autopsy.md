# autopsy

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `autopsy` ❌ missing |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Digital forensics platform

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
autopsy --version
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
command not found: autopsy
```

## What I Learned / Edge Cases / Gotchas
- `autopsy` not found — run `scripts/kali-full-bootstrap.sh`
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `autopsy --version {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `autopsy --help` and tune `autopsy --version {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:31.699187+00:00*
