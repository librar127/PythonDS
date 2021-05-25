# Write your MySQL query statement below
WITH state_date_tbl as
(
    SELECT
        "failed" as period_state,
        fail_date as state_date
    FROM
        Failed
    WHERE 
        fail_date between '2019-01-01' and '2019-12-31'
    UNION ALL
    SELECT
        "succeeded" as period_state,
        success_date as state_date
    FROM
        Succeeded
    WHERE 
        success_date between '2019-01-01' and '2019-12-31' 
),

state_min_max_date_tbl AS
(
    SELECT
        period_state,
        state_date,
        date_sub(state_date, interval row_number() over(partition by period_state order by state_date) day) dt
    FROM
       state_date_tbl 
)

SELECT
    period_state,
    min(state_date) start_date,
    max(state_date) end_date
FROM
    state_min_max_date_tbl
GROUP BY
    period_state,
    dt
ORDER BY
    start_date
