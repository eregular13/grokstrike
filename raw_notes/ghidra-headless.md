# ghidra-headless

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | binary — Binary Analysis / Reverse Engineering |
| **Binary** | `analyzeHeadless` ❌ missing |
| **Agent** | binary |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Ghidra headless analysis

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
analyzeHeadless /workspace ghidra_proj -import /workspace/binary
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
command not found: analyzeHeadless
```

## What I Learned / Edge Cases / Gotchas
- `analyzeHeadless` not found — run `scripts/kali-full-bootstrap.sh`
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `analyzeHeadless /workspace ghidra_proj -import /workspace/binary {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `analyzeHeadless --help` and tune `analyzeHeadless /workspace ghidra_proj -import /workspace/binary {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:54.892871+00:00*
