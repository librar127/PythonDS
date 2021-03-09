-- Write your MySQL query statement below

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
