--  Write your MySQL query statement below
WITH nT as
(
    SELECT 
        log_id,
        -- row_number() over (order by log_id) as row_nbr,
        log_id - row_number() over (order by log_id) as diff
    FROM
      Logs  
)

SELECT 
    min(log_id) start_id, 
    max(log_id) end_id
FROM 
    nT
GROUP BY
    diff