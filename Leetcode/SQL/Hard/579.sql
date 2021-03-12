-- Write your MySQL query statement below
WITH exclude_recent_month_tbl AS
(   
    SELECT
        *
    FROM
        Employee
    WHERE
        (id, month) not in (SELECT id, MAX(month) FROM Employee group by ID)
)

SELECT
    ID,
    Month,
    SUM(Salary) over (partition by ID order by month ROWS Between 2 PRECEDING and CURRENT ROW) salary
FROM
    exclude_recent_month_tbl
ORDER BY
    ID,
    Month DESC