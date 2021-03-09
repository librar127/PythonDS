-- Write your MySQL query statement below

WITH nT as
(
    SELECT
        count(distinct B.post_id) * 100 / count(distinct A.post_id) percentage
    FROM
        Actions A
    LEFT JOIN Removals B
        On A.post_id = B.post_id 
    WHERE
        A.extra = 'spam'
    GROUP BY    
        action_date
)

SELECT 
    round(avg(percentage), 2)average_daily_percent
    FROM nT