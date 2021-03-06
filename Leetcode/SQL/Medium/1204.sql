-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        person_id,
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn) running_weight
    FROm
        Queue
    ORDER By
        running_weight
)
SELECT
    person_name
FROM
    nT
WHERE
    running_weight <= 1000
ORDER BY
    running_weight DESC
LIMIT 1