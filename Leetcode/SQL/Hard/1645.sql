-- Write your MySQL query statement below
WITH Recursive months AS
(
    SELECT 
        1 as month
    UNION ALL
    SELECT
        month + 1
    FROM
        months
    WHERE
        month < 12
),

driver_joined AS
(
    SELECT 
        month, 
        ifnull(count(distinct driver_id), 0) drivers_joined
    FROM
    ( 
        SELECT
            driver_id, 1 as month
        FROM
            Drivers
        WHERE
            YEAR(join_date) < 2020
        UNION ALL
        SELECT
            driver_id, MONTH(join_date) month
        FROM
            Drivers
        WHERE
            YEAR(join_date) = 2020
    )T
    GROUP BY
        month
),

driver_accepted AS
(
    SELECT
        month(requested_at) month,
        count(distinct driver_id) drivers_accepted
    FROM
        AcceptedRides A
    JOIN
        Rides B
    ON
        A.ride_id = B.ride_id
    WHERE
        year(requested_at) = 2020
    GROUP BY
        month(requested_at)
),

driver_available AS
(
    SELECT
        A.month,
        ifnull(SUM(B.drivers_joined) over(order by month rows between unbounded preceding and current row), 0) drivers_available
    FROM
        months A
    LEFT JOIN
        driver_joined B
    ON
        A.month = B.month
    GROUP BY
        A.month
)

SELECT
    A.month,
    round(ifnull(B.drivers_accepted*100/A.drivers_available, 0), 2) working_percentage
FROM
    driver_available A
LEFT JOIN
    driver_accepted B
ON
    A.month = B.month
ORDER BY
    A.month