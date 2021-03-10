-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        *,
        rank() OVER (partition by username order by startdate desc) recency
    FROM
        UserActivity
)

SELECT
    username,
    activity,
    startDate,
    endDate
FROM
    nT
WHERE
    recency = 2
UNION
SELECT
    username,
    activity,
    startDate,
    endDate
FROM
    nT
WHERE
    recency = 1 and username not in (select distinct username from nT where recency = 2)