-- Write your MySQL query statement below
SELECT
    SUM(A.apple_count + COALESCE(B.apple_count, 0)) apple_count,
    SUM(A.orange_count + COALESCE(B.orange_count, 0)) orange_count 
FROM
    Boxes A
LEFT JOIN
   Chests B
ON
    A.chest_id = B.chest_id