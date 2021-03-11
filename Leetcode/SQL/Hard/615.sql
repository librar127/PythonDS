-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        date_format(pay_date, "%Y-%m") pay_month,
        department_id,
        AVG(amount) OVER(PARTITION BY date_format(pay_date, "%Y-%m"), department_id) month_dept_avg,
        AVG(amount) OVER(PARTITION BY date_format(pay_date, "%Y-%m")) month_avg
    FROM
        employee A
    JOIN
        salary B
    ON
        A.employee_id = B.employee_id
)

SELECT
    pay_month,
    department_id,
    CASE
        WHEN month_dept_avg = month_avg THEN 'same'
        WHEN month_dept_avg > month_avg THEN 'higher'
        WHEN month_dept_avg < month_avg THEN 'lower'  
    END AS comparison
FROM
    nT
GROUP BY
    pay_month,
    department_id,
    comparison    
ORDER BY
    pay_month DESC,
    department_id