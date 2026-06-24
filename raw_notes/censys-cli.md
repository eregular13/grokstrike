# censys-cli

## Tool Name & Category
- **Name:** censys-cli
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `censys`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Censys search

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
censys search localhost
```

**Target:** `localhost`  
**Duration:** 0.23s | **Exit code:** 1

## Full Output Summary
```
Traceback (most recent call last):
  File "/usr/bin/censys", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/usr/lib/python3/dist-packages/censys/cli/__init__.py", line 27, in main
    args.func(args)
    ~~~~~~~~~^^^^^^
  File "/usr/lib/python3/dist-packages/censys/cli/commands/search.py", line 91, in cli_search
    c = SearchClient(**censys_args)
  File "/usr/lib/python3/dist-packages/censys/search/client.py", line 69, in __init__
    self.v1 = self._V1(**kwargs)
              ~~~~~~~~^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/censys/search/client.py", line 37, in __init__
    self.data = CensysData(*args, **kwargs)
                ~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/censys/search/v1/api.py", line 68, in __init__
    raise CensysException("No API ID or API secret configured.")
censys.common.exceptions.CensysException: No API ID or API secret configured.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `censys search {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:36.710665+00:00*
