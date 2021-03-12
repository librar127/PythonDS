-- Write your MySQL query statement below

WITH non_banned_clients_tbl AS
(
    SELECT
        A.*
    FROM
        Trips A
    JOIN
        Users B
    ON
        A.Client_Id = B.Users_id
    AND
       Banned = 'No' 
),

non_banned_tbl AS
(
    SELECT
        A.*
    FROM
        non_banned_clients_tbl A
    JOIN
        Users B
    ON
        A.Driver_Id = B.Users_id
    AND
       Banned = 'No'         
),

total_trips_tbl as
(
    SELECT 
        request_at,
        count(id) total_trips
    FROM
        non_banned_tbl
    GROUP BY
        request_at
),

total_cancelled_tbl as
(
    SELECT 
        request_at,
        count(id) total_cancelled_trips
    FROM
        non_banned_tbl
    WHERE
        Status like "cancelled_by_%"
    GROUP BY
        request_at
)

SELECT
    A.request_at day,
    round(ifnull(total_cancelled_trips / total_trips, 0), 2) `Cancellation Rate`
FROM
    total_trips_tbl A
LEFT JOIN
    total_cancelled_tbl B
ON
    A.request_at = B.request_at
WHERE
    A.request_at between '2013-10-01' and '2013-10-03'
ORDER BY
    A.request_at