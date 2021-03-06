-- Write your MySQL query statement below

WITH nT as
(
    SELECT
        company_id,
        employee_id,
        employee_name,
        salary,
        max(salary) over(partition by company_id) max_salary
    FROM
        Salaries
)
SELECT
    company_id,
    employee_id,
    employee_name,
    ROUND(CASE 
        WHEN max_salary < 1000 THEN salary
        WHEN max_salary >= 1000 and max_salary <= 10000 THEN (1-0.24)*salary
        WHEN max_salary >10000 THEN (1-0.49)*salary 
    END, 0) salary
FROM
    nT