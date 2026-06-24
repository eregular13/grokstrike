# hping3

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `hping3` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Crafted packet probe

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hping3 -S -p 80 -c 3 aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 2.14s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
HPING aegis-target (eth0 172.22.0.2): S set, 40 headers + 0 data bytes
len=44 ip=172.22.0.2 ttl=64 DF id=0 sport=80 flags=SA seq=0 win=64240 rtt=1.0 ms
len=44 ip=172.22.0.2 ttl=64 DF id=0 sport=80 flags=SA seq=1 win=64240 rtt=0.9 ms
len=44 ip=172.22.0.2 ttl=64 DF id=0 sport=80 flags=SA seq=2 win=64240 rtt=0.7 ms

--- STDERR ---

--- aegis-target hping statistic ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.7/0.8/1.0 ms

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `hping3 -S -p 80 -c 3 {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `hping3 --help` and tune `hping3 -S -p 80 -c 3 {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:06.215156+00:00*
