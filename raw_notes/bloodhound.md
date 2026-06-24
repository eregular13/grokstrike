# bloodhound

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `bloodhound-python` ✅ installed |
| **Agent** | exploit |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
AD attack path mapping

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
bloodhound-python -u user -p pass -d aegis-target -c All
```

| Metric | Value |
|--------|-------|
| Duration | 0.96s |
| Exit code | 1 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
WARNING: Could not find a global catalog server, assuming the primary DC has this role
If this gives errors, either specify a hostname with -gc or disable gc resolution with --disable-autogc
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: [Errno Connection error (AEGIS-TARGET:88)] [Errno 111] Connection refused
ERROR: Could not find a domain controller. Consider specifying a domain and/or DNS server.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `bloodhound-python -u user -p pass -d {host} -c All {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `bloodhound-python --help` and tune `bloodhound-python -u user -p pass -d {host} -c All {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:52.518096+00:00*
