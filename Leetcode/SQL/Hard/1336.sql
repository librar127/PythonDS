-- Write your MySQL query statement below

WITH recursive count_seq AS
(
    SELECT
        0 as n
    UNION ALL
    SELECT
        n+1
    FROM
       count_seq
    WHERE
        n < (SELECT max(transaction_cnt) from (SELECT COUNT(user_id) transaction_cnt FROM Transactions GROUP BY user_id, transaction_date)T)
),

trans_counts AS
(
    SELECT
        user_id,
        transaction_date,
        COUNT(*) transactions_count
    FROM    
        Transactions 
    GROUP BY    
        user_id,
        transaction_date
),
    
visit_counts AS
(
    SELECT
        user_id,
        visit_date,
        COUNT(*) visit_count
    FROM    
        Visits 
    GROUP BY    
        user_id,
        visit_date
), 

trans_visit AS
(
    SELECT
        ifnull(A.transactions_count, 0) transactions_count,
        ifnull(count(B.visit_count), 0) visit_count
    FROM
        trans_counts A
    RIGHT JOIN
        visit_counts B
    ON
        A.user_id = B.user_id
    AND
        A.transaction_date = B.visit_date
    GROUP BY
        A.transactions_count
)

SELECT
    A.n as transactions_count,
    ifnull(visit_count, 0) visits_count
FROM
    count_seq A
LEFT JOIN
    trans_visit B
ON
    A.n = B.transactions_count