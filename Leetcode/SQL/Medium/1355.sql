-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        activity, COUNT(id) participants
    FROM
        Friends
    GROUP BY
        activity
)

SELECT
    activity
FROM
    nT
WHERE
   participants > (select min(participants) from nT)
AND
   participants < (select max(participants) from nT)  