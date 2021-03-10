-- Write your MySQL query statement below
WITH RECURSIVE months as 
(
    SELECT 1 as month
    UNION ALL
    SELECT
        month + 1
    FROM
        months
    WHERE 
        month < 12
)

SELECT * FROM  
(
SELECT
    month,
    ROUND(AVG(ride_distance) over(order by month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2)average_ride_distance,
    ROUND(AVG(ride_duration) over(order by month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2)average_ride_duration
FROM
    (
SELECT
    A.month,
    ifnull(B.ride_distance, 0) ride_distance,
    ifnull(B.ride_duration, 0) ride_duration
FROM
    months A
LEFT JOIN
    (SELECT
        MONTH(A.requested_at) month,
        SUM(B.ride_distance) ride_distance,
        SUM(B.ride_duration) ride_duration
    FROM
        Rides A
    JOIN
        AcceptedRides B
    ON
        A.ride_id = B.ride_id
    WHERE
        year(requested_at) = 2020
    GROUP BY
        MONTH(A.requested_at)) B
ON
    A.month = B.month)T
)T
WHERE
month <= 10