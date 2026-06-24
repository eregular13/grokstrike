# nmap-udp

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `nmap` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
UDP top ports

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nmap -sU --top-ports 20 aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 8.51s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Potential vulnerability signal:** sql

## Full Output Summary
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-24 05:36 +0000
Nmap scan report for aegis-target (172.22.0.2)
Host is up (0.000074s latency).
rDNS record for 172.22.0.2: aegis-target.aegiscontrolplane_default

PORT      STATE         SERVICE
53/udp    closed        domain
67/udp    closed        dhcps
68/udp    closed        dhcpc
69/udp    closed        tftp
123/udp   open|filtered ntp
135/udp   closed        msrpc
137/udp   closed        netbios-ns
138/udp   closed        netbios-dgm
139/udp   open|filtered netbios-ssn
161/udp   closed        snmp
162/udp   closed        snmptrap
445/udp   open|filtered microsoft-ds
500/udp   open|filtered isakmp
514/udp   open|filtered syslog
520/udp   open|filtered route
631/udp   open|filtered ipp
1434/udp  open|filtered ms-sql-m
1900/udp  closed        upnp
4500/udp  open|filtered nat-t-ike
49152/udp closed        unknown
MAC Address: 22:44:33:39:AA:11 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 8.40 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nmap -sU --top-ports 20 {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `nmap --help` and tune `nmap -sU --top-ports 20 {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:36:55.704286+00:00*
