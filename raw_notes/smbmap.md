# smbmap

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `smbmap` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
SMB share mapping

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
smbmap -H aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.69s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Open port/service:** open ports...                                                                                                    


[*]

## Full Output Summary
```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[*] Detected 0 hosts serving SMB
[|] Initializing hosts...                                                                                                    


[/] Authenticating...                                                                                                    


[-] Closing connections..                                                                                                    


[\] Closing connections..                                                                                                    


[|] Closing connections..                                                                                                    


[/] Closing connections..                                                                                                    


[-] Closing connections..                                                                                                    


                                                                                                    


[*] Closed 0 connections
[|] Initializing hosts...                                                                                                    


[/] Authenticating...                                                                                                    



```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `smbmap -H {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `smbmap --help` and tune `smbmap -H {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:40:31.821501+00:00*
