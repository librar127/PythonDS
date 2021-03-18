-- Write your MySQL query statement below


SELECT
    A.name,
    SUM(B.amount) balance
FROM
    Users A
JOIN
    Transactions B
ON
    A.account = B.account
GROUP BY
    A.account
HAVING
    SUM(B.amount) > 10000