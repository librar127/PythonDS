-- Write your MySQL query statement below

WITH nT as 
(
    SELECT
        B.ID,
        B.Name Department,
        max(Salary) Salary
    FROM
        Employee A
    JOIN
        Department B
    ON
        A.DepartmentId = B.Id
    GROUP BY
        B.ID,
        B.Name
)

SELECT
    A.Department,
    B.Name Employee,
    A.Salary
FROm
    nT A
JOIN
    Employee B
ON
    A.ID = B.DepartmentId
AND
    A.Salary = B.Salary