-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        DISTINCT
        A.TIV_2016
    FROM
        insurance A
    JOIN
        insurance B
    ON
        A.PID <> B.PID
    AND
        A.TIV_2015 = B.TIV_2015
    AND
        CONCAT(A.LAT, A.LON) IN (SELECT CONCAT(LAT, LON) FROM insurance GROUP BY LAT, LON HAVING count(*) = 1)
)

SELECT
    SUM(TIV_2016)TIV_2016
FROM
    nT