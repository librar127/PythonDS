# Write your MySQL query statement below

WITH unbanned_users_trips AS
(
    SELECT
        DISTINCT
        A.*
    FROM
        Trips A
    JOIN
        Users B
    ON
        A.Client_Id = B.Users_Id
    JOIN
        Users C
    ON 
        A.Driver_Id = C.Users_Id
    AND
        B.banned = 'No'
    AND
        C.banned = 'No'
    AND
        Request_at >= "2013-10-01"
    AND
        Request_at <= "2013-10-03"
)


SELECT
   Request_at Day,
   round((SUM(CASE WHEN Status LIKE 'cancelled_%' THEN 1 ELSE 0 END) *1.0)/ count(ID), 2)`Cancellation Rate`
FROM
    unbanned_users_trips
GROUP BY
    Request_at
ORDER BY
    Request_at
    