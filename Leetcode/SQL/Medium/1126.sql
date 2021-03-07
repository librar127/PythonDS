--Write your MySQL query statement below
WITH nT as
(
SELECT
    -- business_id,
    event_type,
    AVG(occurences) avg_occurences
FROM
   Events 
GROUP BY
    -- business_id,
    event_type
)

SELECT
    A.business_id
FROM
   Events A
JOIN
    nT B
ON
    A.event_type = B.event_type
GROUP BY
    A.business_id
HAVING
    SUM(CASE
        WHEN A.occurences > B.avg_occurences THEN 1 ELSE 0 
    END) > 1