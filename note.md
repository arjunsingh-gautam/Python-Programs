64:modules
65:Packages
66:Decorators
69:Exception Handling
73:Files
80:PDBC
90: Pickling,Unpickling

## Leetcode sql

1. LC_1193:

- Approach:
  - Table
    - Transactions
      - id (PK)
      - country
      - state
      - amount
      - trans_date
- Query: for each month and country the number of transactons and their total amount,approved transactions and their total amount

```sql
SELECT DATE_FORMAT(trans_date,"%Y %M") as month,country,COUNT(*) as trans_count,SELECT COUNT(state) as approved_count From Transactions where state="approved",SUM(amount) as trans_total_amount,SELECT SUM(amount) as approved_total_amount FROM Transactions where state="approved"
FROM Transactions
GROUP BY  DATE_FORMAT(trans_date,"%Y %M"),country;

- for condtional aggregation use case statement
```
