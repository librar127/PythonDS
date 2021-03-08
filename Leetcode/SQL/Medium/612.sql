-- Write your MySQL query statement below

SELECT
    round(min(sqrt(power(abs(A.x - B.x), 2) + power(abs(A.y - B.y), 2))), 2)shortest
FROM
    point_2d A, point_2d B
WHERE
    (A.x, A.y) <> (B.x, B.y)