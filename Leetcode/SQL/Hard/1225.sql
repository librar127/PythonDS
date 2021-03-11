-- Write your MySQL query statement below

SELECT
    "failed" as period_state,
    min(fail_date) start_date,
    max(fail_date) end_date
FROM
    (SELECT
        fail_date,
        DAYOFYEAR(date_sub(fail_date, INTERVAL row_number() over (order by fail_date) day)) id
    FROM
        Failed
    )T
WHERE
    year(fail_date) = 2019
GROUP BY
    period_state,
    id
    
UNION

SELECT
    "succeeded" as period_state,
    min(success_date) start_date,
    max(success_date) end_date
FROM
    (SELECT
        success_date,
        DAYOFYEAR(date_sub(success_date, INTERVAL row_number() over (order by success_date) day)) id
    FROM
        Succeeded
    )T
WHERE
    year(success_date) = 2019
GROUP BY
    period_state,
    id
    
ORDER BY start_date

