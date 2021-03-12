-- Write your MySQL query statement below

WITH distinct_platform AS
(
    SELECT "desktop" AS platform
    UNION ALL
    SELECT "mobile" AS platform
    UNION ALL
    SELECT "both" AS platform
),

date_platform AS
(
    SELECT
        DISTINCT(A.spend_date)spend_date ,
        B.platform
    FROM
        Spending A, distinct_platform B
),

user_platform AS
(
    SELECT
        user_id,
        spend_date,
        CASE WHEN GROUP_CONCAT(platform) like "%,%" THEN "both" else GROUP_CONCAT(platform) END AS platform,
        SUM(amount) total_amount
    FROM
        Spending 
    GROUP BY
        user_id,
        spend_date
)

SELECT
    A.spend_date,
    A.platform,
    ifnull(SUM(B.total_amount), 0) total_amount,
    ifnull(count(distinct B.user_id), 0)total_users 
FROM
    date_platform A
LEFT JOIN
    user_platform B
ON
    A.spend_date = B.spend_date
AND
    A.platform = B.platform
GROUP BY
    A.platform,
    A.spend_date