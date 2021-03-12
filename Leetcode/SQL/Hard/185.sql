-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        A.Name AS Department,
        B.Name AS Employee,
        salary,
        dense_rank() over(partition by A.name order by salary desc) dns_rank
    FROM
        Department A 
    JOIN
        Employee B
    ON
        A.Id = B.DepartmentId
)

SELECT
    Department,
    Employee,
    salary
FROM
    nT
WHERE
    dns_rank <= 3  