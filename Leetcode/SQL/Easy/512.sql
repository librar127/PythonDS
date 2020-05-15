/* Write your MySQL query statement below */

WITH T AS(
SELECT
    *, 
    RANK() OVER (PARTITION BY PLAYER_ID ORDER BY EVENT_DATE) RN
FROM
    ACTIVITY)
     
    
SELECT
    player_id,
    device_id
FROM T
WHERE
    RN=1
    