# Model Checking Result

## 1 Client `{c1}` + 1 Char `{a}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:30:51 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-20 23:30:52 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-20 23:30:53 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-20 23:30:55 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-20 23:30:56 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-20 23:30:57 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-20 23:30:58 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-20 23:30:59 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-20 23:31:01 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| AJupiter               | No       | QC             | 2019-01-20 23:31:02 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-20 23:31:03 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-20 23:31:04 | 10        | 0:00:00       | 5        | 7          | 6                 | NO               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-20 23:31:05 | 10        | 0:00:01       | 5        | 7          | 6                 | NO               | NO                  |

## 1 Client `{c1}` + 2 Chars `{a, b}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:31:06 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-20 23:31:07 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-20 23:31:09 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-20 23:31:10 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-20 23:31:11 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-20 23:31:12 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-20 23:31:13 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-20 23:31:14 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-20 23:31:16 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| AJupiter               | No       | QC             | 2019-01-20 23:31:17 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-20 23:31:18 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-20 23:31:19 | 10        | 0:00:00       | 9        | 86         | 57                | YES               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-20 23:31:20 | 10        | 0:00:01       | 9        | 86         | 57                | YES               | NO                  |

## 1 Client `{c1}` + 3 Chars `{a, b, c}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:31:21 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-20 23:31:23 | 10        | 0:00:00       | 13       | 1696       | 1014              | YES               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-20 23:31:24 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-20 23:31:26 | 10        | 0:00:00       | 13       | 1696       | 1014              | YES               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-20 23:31:27 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-20 23:31:29 | 10        | 0:00:00       | 13       | 1696       | 1014              | YES               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-20 23:31:30 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-20 23:31:32 | 10        | 0:00:00       | 13       | 1696       | 1014              | YES               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-20 23:31:33 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| AJupiter               | No       | QC             | 2019-01-20 23:31:35 | 10        | 0:00:00       | 13       | 1696       | 1014              | YES               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-20 23:31:36 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-20 23:31:37 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-20 23:31:39 | 10        | 0:00:01       | 13       | 1696       | 1014              | YES               | NO                  |

## 2 Clients `{c1, c2}` + 1 Char `{a}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:31:41 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-20 23:31:42 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-20 23:31:43 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-20 23:31:44 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-20 23:31:45 | 10        | 0:00:01       | 10       | 71         | 53                | NO               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-20 23:31:46 | 10        | 0:00:01       | 10       | 71         | 53                | NO               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-20 23:31:48 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-20 23:31:49 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-20 23:31:50 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |
| AJupiter               | No       | QC             | 2019-01-20 23:31:51 | 10        | 0:00:01       | 10       | 71         | 51                | NO               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-20 23:31:52 | 10        | 0:00:01       | 10       | 71         | 51                | NO               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-20 23:31:53 | 10        | 0:00:01       | 10       | 71         | 53                | NO               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-20 23:31:55 | 10        | 0:00:00       | 10       | 71         | 53                | NO               | NO                  |

## 2 Clients `{c1, c2}` + 2 Chars `{a, b}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:31:56 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-20 23:31:59 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-20 23:32:03 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-20 23:32:07 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-20 23:32:10 | 10        | 0:00:05       | 19       | 50215      | 28307             | YES               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-20 23:32:15 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-20 23:32:19 | 10        | 0:00:03       | 19       | 50215      | 28307             | YES               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-20 23:32:23 | 10        | 0:00:05       | 19       | 50215      | 28307             | YES               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-20 23:32:28 | 10        | 0:00:07       | 19       | 50215      | 28307             | YES               | NO                  |
| AJupiter               | No       | QC             | 2019-01-20 23:32:36 | 10        | 0:00:02       | 17       | 26877      | 12409             | YES               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-20 23:32:39 | 10        | 0:00:02       | 19       | 29621      | 14079             | YES               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-20 23:32:42 | 10        | 0:00:02       | 19       | 30301      | 14567             | YES               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-20 23:32:45 | 10        | 0:00:05       | 19       | 50215      | 28307             | YES               | NO                  |

## 2 Clients `{c1, c2}` + 3 Chars `{a, b, c}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-20 23:32:51 | 10        | 2:17:34       | 28       | 150627005  | 75726121          | YES               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-21 01:50:26 | 10        | 1:54:46       | 28       | 150627005  | 75726121          | YES               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-21 03:45:13 | 10        | 3:25:45       | 28       | 150627005  | 75726121          | YES               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-21 07:10:59 | 10        | 2:21:37       | 28       | 150627005  | 75726121          | YES               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-21 09:32:38 | 10        | 4:37:36       | 28       | 150627005  | 75726121          | YES               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-21 14:10:16 | 10        | 2:27:35       | 28       | 150627005  | 75726121          | YES               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-21 16:37:52 | 10        | 2:44:36       | 28       | 150627005  | 75726121          | YES               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-21 19:22:29 | 10        | 2:50:52       | 28       | 150627005  | 75726121          | YES               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-21 22:13:23 | 10        | 5:38:00       | 28       | 150627005  | 75726121          | YES               | NO                  |
| AJupiter               | No       | QC             | 2019-01-22 03:51:25 | 10        | 0:04:06       | 28       | 16726093   | 6537725           | YES               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-22 03:55:32 | 10        | 0:05:21       | 28       | 26878375   | 10884889          | YES               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-22 04:00:54 | 10        | 0:11:17       | 28       | 22227417   | 8859849           | YES               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-22 04:12:12 | 10        | 4:23:52       | 28       | 150627005  | 75726121          | YES               | NO                  |

## 3 Clients `{c1, c2, c3}` + 1 Char `{a}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-22 08:36:06 | 10        | 0:00:00       | 17       | 2785       | 1288              | NO               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-22 08:36:07 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-22 08:36:09 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-22 08:36:10 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-22 08:36:12 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-22 08:36:14 | 10        | 0:00:00       | 17       | 2785       | 1288              | NO               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-22 08:36:15 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-22 08:36:17 | 10        | 0:00:00       | 17       | 2785       | 1288              | NO               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-22 08:36:18 | 10        | 0:00:02       | 17       | 2785       | 1288              | NO               | NO                  |
| AJupiter               | No       | QC             | 2019-01-22 08:36:21 | 10        | 0:00:00       | 17       | 2488       | 1108              | NO               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-22 08:36:22 | 10        | 0:00:01       | 17       | 2488       | 1108              | NO               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-22 08:36:24 | 10        | 0:00:00       | 17       | 2785       | 1288              | NO               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-22 08:36:25 | 10        | 0:00:01       | 17       | 2785       | 1288              | NO               | NO                  |

## 3 Clients `{c1, c2, c3}` + 2 Chars `{a, b}`
| Protocol               | Fairness | Property       | Start Time          | # Workers | Checking Time | Diameter | # States   | # Distinct States | Symmetry for Char | Symmetry for Client |
| ---------------------- | -------- | -------------- | ------------------- | --------- | ------------- | -------- | ---------- | ----------------- | ----------------- | ------------------- |
| AbsJupiter             | No       | TypeOK         | 2019-01-22 08:36:27 | 10        | 2:51:01       | 33       | 206726218  | 74737027          | YES               | NO                  |
| AbsJupiterH            | No       | WLSpec         | 2019-01-22 11:27:30 | 10        | 2:46:02       | 33       | 206726218  | 74737027          | YES               | NO                  |
| CJupiter               | No       | Compactness    | 2019-01-22 14:13:33 | 10        | 3:23:33       | 33       | 206726218  | 74737027          | YES               | NO                  |
| CJupiterH              | No       | WLSpec         | 2019-01-22 17:37:07 | 10        | 3:12:00       | 33       | 206726218  | 74737027          | YES               | NO                  |
| CJupiterImplAbsJupiter | No       | AbsJ!Spec (NO) | 2019-01-22 20:49:08 | 10        | 5:43:26       | 33       | 206726218  | 74737027          | YES               | NO                  |
| XJupiter               | No       | CSSync         | 2019-01-23 02:32:35 | 10        | 2:16:09       | 33       | 206726218  | 74737027          | YES               | NO                  |
| XJupiterH              | No       | WLSpec         | 2019-01-23 04:48:45 | 10        | 2:27:17       | 33       | 206726218  | 74737027          | YES               | NO                  |
| XJupiterExtended       | No       | CSSync         | 2019-01-23 07:16:04 | 10        | 2:42:41       | 33       | 206726218  | 74737027          | YES               | NO                  |
| XJupiterImplCJupiter   | No       | CJ!Spec (NO)   | 2019-01-23 09:58:46 | 10        | 8:50:40       | 33       | 206726218  | 74737027          | YES               | NO                  |
| AJupiter               | No       | QC             | 2019-01-23 18:49:28 | 10        | 0:08:30       | 33       | 34254553   | 11075356          | YES               | NO                  |
| AJupiterH              | No       | WLSpec         | 2019-01-23 18:57:59 | 10        | 0:06:57       | 33       | 38975340   | 12701443          | YES               | NO                  |
| AJupiterExtended       | No       | QC             | 2019-01-23 19:04:57 | 10        | 0:26:29       | 33       | 58104154   | 19220632          | YES               | NO                  |
| AJupiterImplXJupiter   | No       | XJ!Spec (NO)   | 2019-01-23 19:31:27 | 10        | 4:52:39       | 33       | 206726218  | 74737027          | YES               | NO                  |
