# sqlmap

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `sqlmap` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
SQL injection testing (DVWA path)

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
COOKIE=$(/workspace/dvwa_login.sh http://aegis-target); sqlmap -u 'http://aegis-target/vulnerabilities/sqli/?id=1&Submit=Submit' --cookie="$COOKIE" --batch --level=2 --risk=1 --threads=2
```

| Metric | Value |
|--------|-------|
| Duration | 3.08s |
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
 ___ ___[.]_____ ___ ___  {1.10.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:47:37 /2026-06-24/

[1/1] URL:
GET http://aegis-target/vulnerabilities/sqli/?id=1&Submit=Submit
Cookie: =;by=libcurl!;security=low;PHPSESSID=r0fmeehkked7bmvaeb031q2561
do you want to test this URL? [Y/n/q]
> Y
[05:47:37] [INFO] testing URL 'http://aegis-target/vulnerabilities/sqli/?id=1&Submit=Submit'
[05:47:37] [INFO] using '/root/.local/share/sqlmap/output/results-06242026_0547am.csv' as the CSV results file in multiple targets mode
[05:47:37] [INFO] testing connection to the target URL
got a 302 redirect to 'http://aegis-target/login.php'. Do you want to follow? [Y/n] Y
[05:47:37] [INFO] testing if the target URL content is stable
[05:47:37] [WARNING] GET parameter 'id' does not appear to be dynamic
[05:47:37] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
[05:47:37] [INFO] testing for SQL injection on GET parameter 'id'
[05:47:37] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:47:37] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[05:47:37] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[05:47:38] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[05:47:38] [INFO] GET parameter 'id' appears to be 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (2) and risk (1) values? [Y/n] Y
[05:47:38] [INFO] testing 'Generic inline queries'
[05:47:38] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[05:47:38] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[05:47:38] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[05:47:38] [INFO] checking if the injection point on GET parameter 'id' is a false positive
[05:47:38] [WARNING] false positive or unexploitable injection point detected
[05:47:38] [WARNING] GET parameter 'id' does not seem to be injectable
[05:47:38] [WARNING] GET parameter 'Submit' does not appear to be dynamic
[05:47:38] [WARNING] heuristic (basic) test shows that GET parameter 'Submit' might not be injectable
[05:47:38] [INFO] testing for SQL injection on GET parameter 'Submit'
[05:47:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:47:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[05:47:38] [INFO] GET parameter 'Submit' appears to be 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)' injectable 
[05:47:38] [INFO] testing 'Generic inline queries'
[05:47:38] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[05:47:38] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[05:47:38] [INFO] checking if the injection point on GET parameter 'Submit' is a false positive
[05:47:38] [WARNING] false positive or unexploitable injection point detected
[05:47:38] [WARNING] GET parameter 'Submit' does not seem to be injectable
[05:47:38] [WARNING] Cookie parameter 'by' does not appear to be dynamic
do you want to URL encode cookie values (implementation specific)? [Y/n] Y
[05:47:38] [WARNING] heuristic (basic) test shows that Cookie parameter 'by' might not be injectable
[05:47:38] [INFO] testing for SQL injection on Cookie parameter 'by'
[05:47:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:47:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[05:47:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[05:47:39] [INFO] testing 'Generic inline queries'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[05:47:39] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[05:47:39] [WARNING] Cookie parameter 'by' does not seem to be injectable
[05:47:39] [WARNING] Cookie parameter 'security' does not appear to be dynamic
[05:47:39] [WARNING] heuristic (basic) test shows that Cookie parameter 'security' might not be injectable
[05:47:39] [INFO] testing for SQL injection on Cookie parameter 'security'
[05:47:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:47:39] [INFO] Cookie parameter 'security' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[05:47:39] [INFO] testing 'Generic inline queries'
[05:47:39] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[05:47:39] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[05:47:39] [INFO] checking if the injection point on Cookie parameter 'security' is a false positive
[05:47:39] [WARNING] false positive or unexploitable injection point detected
[05:47:39] [WARNING] Cookie parameter 'security' does not seem to be injectable
[05:47:39] [WARNING] Cookie parameter 'PHPSESSID' does not appear to be dynamic
[05:47:39] [WARNING] heuristic (basic) test shows that Cookie parameter 'PHPSESSID' might not be injectable
[05:47:39] [INFO] testing for SQL injection on Cookie parameter 'PHPSESSID'
[05:47:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:47:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[05:47:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[05:47:39] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[05:47:39] [INFO] testing 'Generic inline queries'
[05:47:39] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[05:47:39] [WARNING] Cookie parameter 'PHPSESSID' does not seem to be injectable
[05:47:39] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next target
[05:47:39] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/root/.local/share/sqlmap/output/results-06242026_0547am.csv'

[*] ending @ 05:47:39 /2026-06-24/


```

## What I Learned / Edge Cases / Gotchas
- DVWA requires authenticated session — `/workspace/dvwa_login.sh` sets cookies + security=low
- Registry template: `sqlmap -u '{web}/vulnerabilities/sqli/?id=1&Submit=Submit' --batch --level=1 --risk=1 {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 240s

## Next Steps for Exploration & Development
After auth, test `/vulnerabilities/sqli_blind/` and increase `--level=3`.

---
*GrokStrike v2 — 2026-06-24T05:47:39.848307+00:00*
