# nmap-udp

## Tool Name & Category
- **Name:** nmap-udp
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `nmap`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
UDP top ports

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nmap -sU --top-ports 20 aegis-target
```

**Target:** `aegis-target`  
**Duration:** 8.1s | **Exit code:** 0

## Full Output Summary
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-24 05:05 +0000
Nmap scan report for aegis-target (172.22.0.2)
Host is up (0.000070s latency).
rDNS record for 172.22.0.2: aegis-target.aegiscontrolplane_default

PORT      STATE         SERVICE
53/udp    closed        domain
67/udp    closed        dhcps
68/udp    open|filtered dhcpc
69/udp    closed        tftp
123/udp   closed        ntp
135/udp   open|filtered msrpc
137/udp   closed        netbios-ns
138/udp   closed        netbios-dgm
139/udp   open|filtered netbios-ssn
161/udp   open|filtered snmp
162/udp   open|filtered snmptrap
445/udp   open|filtered microsoft-ds
500/udp   closed        isakmp
514/udp   open|filtered syslog
520/udp   closed        route
631/udp   closed        ipp
1434/udp  open|filtered ms-sql-m
1900/udp  open|filtered upnp
4500/udp  closed        nat-t-ike
49152/udp closed        unknown
MAC Address: 22:44:33:39:AA:11 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 7.95 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `nmap -sU --top-ports 20 {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:06:04.163704+00:00*
