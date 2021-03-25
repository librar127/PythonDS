-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        business_id,
        event_type,
        occurences,
        avg(occurences) over(partition by event_type) avg_occurences
    FROM
        Events
    GROUP BY
        business_id,
        event_type
)

SELECT
    business_id
FROM
    nT
GROUP BY
    business_id
HAVING
   SUM(CASE WHEN occurences > avg_occurences THEN 1 ELSE 0 END) > 1 