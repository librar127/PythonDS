-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        user_id,
        visit_date,
        COALESCE(LEAD(visit_date, 1) OVER(PARTITION BY user_id order by visit_date), STR_TO_DATE('2021-01-01', "%Y-%m-%d")) next_visit_date
    FROM
        UserVisits
)

SELECT
    user_id,
    MAX(DATEDIFF(next_visit_date, visit_date))biggest_window
FROM
    nT
GROUP BY
    user_id