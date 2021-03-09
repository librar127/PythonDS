-- Write your MySQL query statement below

-- First Solution
SELECT    
    DISTINCT
    A.num ConsecutiveNums
FROM
    Logs A
JOIN
    Logs B
ON
    A.id+1 = B.id
JOIN
    Logs C
ON
    B.id+1 = C.id
AND
    A.num = B.num
AND
    B.num = C.num

-- Second Solution
SELECT
    DISTINCT
    A.num ConsecutiveNums
FROM
    Logs A,
    Logs B,
    Logs C
WHERE
    A.id <> B.id and B.id <> C.id
AND 
    A.num = B.num 
AND 
    B.num = C.num
AND
   ((A.id+1 = B.id and A.id+2 = C.id)
OR
    (A.id-1 = B.id and A.id+1 = C.id)
OR
    (A.id-2 = B.id and A.id-1 = C.id))