-- Write your MySQL query statement below

WITH nT AS
(
    SELECT
        requester_id id,
        COUNT(DISTINCT accepter_id) num
    FROM 
        request_accepted
    GROUP BY
        requester_id
    UNION ALL
    SELECT
        accepter_id id,
        COUNT(DISTINCT requester_id) num
    FROM 
        request_accepted
    GROUP BY
        accepter_id
)

SELECT
    id,
    SUM(num) num
FROM
    nT
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1
    
    