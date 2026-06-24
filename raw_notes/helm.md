# helm

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | cloud — Cloud & Container Security |
| **Binary** | `helm` ❌ missing |
| **Agent** | cloud |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Helm releases

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
helm list -A
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
command not found: helm
```

## What I Learned / Edge Cases / Gotchas
- `helm` not found — run `scripts/kali-full-bootstrap.sh`
- Cloud tools may need API credentials; container scans work offline with trivy/grype
- Registry template: `helm list -A {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `helm --help` and tune `helm list -A {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:30.075016+00:00*
