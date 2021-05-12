-- Write your MySQL query statement below
SELECT
    DISTINCT
    A.employee_id
FROM
    Employees A
JOIN
    Employees M1
ON
    A.manager_id = M1.employee_id
JOIN
    Employees M2
ON
    M1.manager_id = M2.employee_id
JOIN
    Employees M3
ON
    M2.manager_id = M3.employee_id    
AND
    (M1.employee_id = 1 OR M2.employee_id = 1 OR M3.employee_id = 1)
AND
    A.employee_id !=1