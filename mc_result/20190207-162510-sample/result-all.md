# Model Checking Result

## 1 Client `{c1}` + 1 Char `{a}`
| Protocol               | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States |
| ---------------------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- |
| AbsJupiter             | WLSpec         | 2019-02-07 16:25:10 | 10        | 0:00:00       | 5        | 7          | 6                 |
| CJupiterImplAbsJupiter | AbsJ!Spec      | 2019-02-07 16:25:13 | 10        | 0:00:00       | 5        | 7          | 6                 |
| XJupiterImplCJupiter   | CJ!Spec        | 2019-02-07 16:25:16 | 10        | 0:00:00       | 5        | 7          | 6                 |
| AJupiterImplXJupiter   | XJ!Spec        | 2019-02-07 16:25:19 | 10        | 0:00:00       | 5        | 7          | 6                 |

## 1 Client `{c1}` + 2 Chars `{a, b}`
| Protocol               | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States |
| ---------------------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- |
| AbsJupiter             | WLSpec         | 2019-02-07 16:25:11 | 10        | 0:00:01       | 9        | 86         | 57                |
| CJupiterImplAbsJupiter | AbsJ!Spec      | 2019-02-07 16:25:14 | 10        | 0:00:00       | 9        | 86         | 57                |
| XJupiterImplCJupiter   | CJ!Spec        | 2019-02-07 16:25:17 | 10        | 0:00:01       | 9        | 86         | 57                |
| AJupiterImplXJupiter   | XJ!Spec        | 2019-02-07 16:25:20 | 10        | 0:00:00       | 9        | 86         | 57                |
