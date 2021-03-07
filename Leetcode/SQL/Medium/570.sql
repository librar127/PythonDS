-- Write your MySQL query statement below
WITH nT as 
(        
    SELECT 
        ManagerId
    FROM
        Employee
    WHERE
        ManagerId is not null
    group by
        ManagerId
    HAVING 
        count(*) >= 5
)

SELECT
    Name
FROM
    Employee
JOIN
    nT
ON
    Employee.id = nT.ManagerId
