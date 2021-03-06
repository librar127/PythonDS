--  Write your MySQL query statement below

WITH RECURSIVE nT AS
(
    SELECT 1 as ids
    UNION ALL
    SELECT ids + 1
    FROM nT
    WHERE ids < (SELECT max(customer_id) FROM Customers)     
)

SELECT 
    ids 
FROM
    nT
WHERE
    ids not in (SELECT customer_id FROM Customers)