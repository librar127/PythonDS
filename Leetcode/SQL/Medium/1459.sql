-- Write your MySQL query statement below
SELECT
    A.id as p1,
    B.id as p2,
    abs(A.x_value - B.x_value) * abs(A.y_value - B.y_value) as area
FROM
    Points A, Points B
WHERE
    A.id != B.id
AND
    A.id < B.id
AND
    abs(A.x_value - B.x_value) * abs(A.y_value - B.y_value) > 0
ORDER BY
    area DESC,
    p1,
    p2    