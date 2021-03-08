-- Write your MySQL query statement below
WITH nT as
(    
    SELECT
        paid_to user_id,
        SUM(amount) total_amt
    FROM
        Transactions
    GROUP BY
        paid_to
    UNION ALL
    SELECT
        paid_by user_id,
        SUM(-1*amount) total_amt
    FROM
        Transactions
    GROUP BY
        paid_by
), nT2 AS
(
    SELECT
        user_id,
        SUM(total_amt) total
    FROM
        nT
    GROUP BY
        user_id
)

SELECT
    A.user_id,
    A.user_name,
    A.credit + COALESCE(B.total, 0) as credit,
    CASE WHEN A.credit + COALESCE(B.total, 0)  < 0 THEN 'Yes' ELSE 'No' END AS credit_limit_breached
FROM
    Users A
LEFT JOIN
    nT2 B
ON
    A.user_id = B.user_id