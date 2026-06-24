# nmap-quick

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `nmap` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | True |
| **Lab target** | `aegis-target` |

## Official Purpose
Fast top-port scan

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nmap -F -T4 aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.74s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Open port/service:** open  http
MAC

## Full Output Summary
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-24 05:36 +0000
Nmap scan report for aegis-target (172.22.0.2)
Host is up (0.000014s latency).
rDNS record for 172.22.0.2: aegis-target.aegiscontrolplane_default
Not shown: 99 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http
MAC Address: 22:44:33:39:AA:11 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.62 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nmap -F -T4 {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `nmap --help` and tune `nmap -F -T4 {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:36:47.104261+00:00*
