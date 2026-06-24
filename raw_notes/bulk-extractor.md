# bulk-extractor

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `bulk_extractor` ❌ missing |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Feature extraction

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
bulk_extractor -o /results/bulk /workspace/image.dd
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
command not found: bulk_extractor
```

## What I Learned / Edge Cases / Gotchas
- `bulk_extractor` not found — run `scripts/kali-full-bootstrap.sh`
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `bulk_extractor -o /results/bulk /workspace/image.dd {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `bulk_extractor --help` and tune `bulk_extractor -o /results/bulk /workspace/image.dd {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:31.591652+00:00*
