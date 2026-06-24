# nuclei

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `nuclei` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Template-based vuln scan

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nuclei -u http://aegis-target -severity low,medium,high -silent -stats
```

| Metric | Value |
|--------|-------|
| Duration | 13.15s |
| Exit code | 0 |
| Effectiveness | **5/10** — Ran successfully, limited findings |

## Key Findings
- See output summary for raw tool data.

## Full Output Summary
```

--- STDERR ---
[0:00:05] | Templates: 5025 | Hosts: 1 | RPS: 143 | Matched: 0 | Errors: 10 | Requests: 755/11482 (6%)
[0:00:10] | Templates: 5025 | Hosts: 1 | RPS: 171 | Matched: 0 | Errors: 31 | Requests: 1757/11482 (15%)
[0:00:12] | Templates: 5025 | Hosts: 1 | RPS: 177 | Matched: 0 | Errors: 69 | Requests: 2072/11482 (18%)
[0:00:12] | Templates: 5025 | Hosts: 1 | RPS: 177 | Matched: 0 | Errors: 69 | Requests: 2072/11482 (18%)

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nuclei -u {web} -severity low,medium,high,critical {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 300s

## Next Steps for Exploration & Development
Add `-tags dvwa,apache,misconfig` and export with `-jsonl -o /results/nuclei.jsonl`.

---
*GrokStrike v2 — 2026-06-24T05:47:13.824695+00:00*
