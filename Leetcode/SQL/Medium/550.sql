-- Write your MySQL query statement below
WITH nT as
(    
    SELECT
        player_id,
        min(event_date) min_event_date
    FROM
        Activity
    GROUP BY    
        player_id
)

SELECT
    ROUND(SUM(CASE WHEN DATEDIFF(event_date, min_event_date) = 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT nT.player_id), 2)fraction
FROM
    nT 
JOIN
    Activity
ON
    Activity.player_id = nT.player_id