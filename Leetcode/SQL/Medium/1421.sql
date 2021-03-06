-- Write your MySQL query statement below
SELECT 
    A.id,
    A.year,
    COALESCE(B.npv, 0) as npv
FROM
    Queries A
LEFT JOIN
    NPV B
ON
    A.id = B.id
AND
    A.year = B.year