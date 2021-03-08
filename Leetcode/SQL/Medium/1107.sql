-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        user_id,
        min(activity_date) activity_date
    FROM
        Traffic
    WHERE
        activity = 'login'
    GROUP BY
        user_id
)

SELECT
    activity_date login_date,
    COUNT(distinct user_id) user_count
FROM
    nT
WHERE    
    datediff('2019-06-30', activity_date) <= 90
GROUP BY
    activity_date


-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        user_id,
        min(activity_date) activity_date
    FROM
        Traffic
    WHERE
        activity = 'login'
    GROUP BY
        user_id
)

SELECT
    activity_date login_date,
    COUNT(distinct user_id) user_count
FROM
    nT
WHERE    
    activity_date BETWEEN date_sub("2019-06-30", INTERVAL 90 DAY) AND "2019-06-30"  
GROUP BY
    activity_date