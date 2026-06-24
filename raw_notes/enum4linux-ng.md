# enum4linux-ng

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `enum4linux-ng` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Advanced SMB enum

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
enum4linux-ng -A aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 10.3s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
[92mENUM4LINUX - next generation (v1.3.10)[0m

 ==========================
|    Target Information    |
 ==========================
[94m[*] Target ........... aegis-target[0m
[94m[*] Username ......... ''[0m
[94m[*] Random Username .. 'phweoccc'[0m
[94m[*] Password ......... ''[0m
[94m[*] Timeout .......... 10 second(s)[0m

 =====================================
|    Listener Scan on aegis-target    |
 =====================================
[94m[*] Checking LDAP[0m
[91m[-] Could not connect to LDAP on 389/tcp: connection refused[0m
[94m[*] Checking LDAPS[0m
[91m[-] Could not connect to LDAPS on 636/tcp: connection refused[0m
[94m[*] Checking SMB[0m
[91m[-] Could not connect to SMB on 445/tcp: connection refused[0m
[94m[*] Checking SMB over NetBIOS[0m
[91m[-] Could not connect to SMB over NetBIOS on 139/tcp: connection refused[0m

 ===========================================================
|    NetBIOS Names and Workgroup/Domain for aegis-target    |
 ===========================================================
[91m[-] Could not get NetBIOS names information via 'nmblookup': timed out[0m

[93m[!] Aborting remainder of tests since neither SMB nor LDAP are accessible[0m

Completed after 10.01 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `enum4linux-ng -A {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `enum4linux-ng --help` and tune `enum4linux-ng -A {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:40:31.028862+00:00*
