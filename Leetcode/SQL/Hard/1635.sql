-- Write your MySQL query statement below
WITH recursive months as
(   
    select 1 as month
    UNION ALL
    SELECT
        month +1
    FROM
        months
    WHERE
        month < 12
),

driver AS
(   
    select 
        case 
            when year(join_date) < 2020 then 1
            when year(join_date) = 2020 then month(join_date)
            else 0 
        end as driver_month
    from 
        drivers
), 

active_drivers AS
(
    SELECT
        month,
        -- count(B.driver_month) active_drivers
        SUM(count(B.driver_month)) over (order by month) active_drivers
    FROM
        months A
    LEFT JOIN
        driver B
    ON
        A.month = B.driver_month    
    GROUP BY
        A.month
),

accepted_rides AS
(
    SELECT
        month(requested_at) month,
        count(distinct A.ride_id) accepted_rides
    FROM
        Rides A
    JOIN
        AcceptedRides B
    ON
        A.ride_id = B.ride_id
    WHERE 
        YEAR(requested_at) =  2020
    GROUP BY
        month(requested_at)
)

SELECT
    A.month,
    A.active_drivers,
    ifnull(B.accepted_rides, 0)accepted_rides
FROM
    active_drivers A
LEFT JOIN
    accepted_rides B
ON
    A.month = B.month
ORDER BY
    A.month
