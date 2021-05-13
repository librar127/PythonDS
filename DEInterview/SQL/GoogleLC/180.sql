SELECT    
    DISTINCT
    A.num ConsecutiveNums
FROM
    Logs A
JOIN
    Logs B
ON
    A.id = B.id-1
JOIN
    Logs C
ON
    A.id = C.id-2
AND
    A.num = B.num
AND
    B.num = C.num