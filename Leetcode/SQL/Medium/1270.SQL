# Write your MySQL query statement below
SELECT
    E1.employee_id
FROM
    Employees E1
JOIN
    Employees E2
ON
    E1.manager_id = E2.employee_id
JOIN
    Employees E3
ON
    E3.employee_id = E2.manager_id
JOIN
    Employees E4
ON
    E3.manager_id = E4.employee_id
AND
    E4.employee_id = 1
AND
    E1.employee_id != 1
