-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        A.project_id,
        A.employee_id,
        RANK() OVER (PARTITION BY project_id ORDER BY experience_years DESC) rn
    FROM
        Project A
    JOIN
        Employee B
    ON
        A.employee_id = B.employee_id
)

SELECT
    project_id,
    employee_id
FROM
    nT
WHERE 
    rn = 1
    