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

- LC_1174
    - Delivery:
        - delivery_id (Unique)
        - customer_id ()
        - order_date 
        - customer_pref_delivery_date

- Approach:
    - How to find first order?

sE


- LC_1141
    - Activity
        - user_id

```sql
SELECT activity_date as day ,COUNT(DISTINCT user_id) as active_users
WHERE DATEDIFF('2019-07-27',active_date)<=30
GROUP BY activity_date;
```

- LC 596

- Course:
    - student
    - class

```sql
SELECT class
from Courses
group by class
having COUNT(student)>=5;
```

LC 1729
- Followers:
    - user_id
    - follower_id

```sql
select user_id,count(follower_id) as followers_count
from Followers
group by user_id
order by user_id ASC;
```

- LC 619
- MyNumbers
```sql
select ifnull(distinct num,null)
from MyNumbers
order by num DESC
limit 1;
```
# TO-DO
- sorting + revision
- pandas and numpy
- statistic 50%
- project complete report and enhancement
- go basics
- python http project
- sql