-- Write your MySQL query statement below
WITH RECURSIVE nT AS
(   
    SELECT
        task_id, 
        1 as subtask_id 
    FROM
        Tasks
    UNION ALL
    SELECT
        A.task_id,
        subtask_id+1
    FROM
        nT A
    JOIN
        Tasks B
    ON
        A.task_id = B.task_id
    AND
        subtask_id < subtasks_count
)

SELECT 
    A.task_id, 
    A.subtask_id    
FROM 
    nT A
LEFT JOIN
    Executed B
ON
    A.task_id = B.task_id
AND
    A.subtask_id = B.subtask_id
WHERE
    B.task_id is NULL
    