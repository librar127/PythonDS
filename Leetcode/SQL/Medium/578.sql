-- Write your MySQL query statement below
SELECT
    question_id as survey_log
FROM
    survey_log
GROUP BY
    question_id
ORDER BY
    SUM(CASE WHEN action = 'answer' then 1 else 0 end)/SUM(CASE WHEN action = 'show' then 1 else 0 end) DESC
LIMIT 1
