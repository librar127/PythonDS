-- Write your MySQL query statement below
WITH nT AS
(
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY Company ORDER BY Salary) AS rk,
        COUNT(Id) OVER (PARTITION BY Company) AS size
    FROM 
        Employee
)
SELECT
    id,
    company,
    salary
FROM
    nT
WHERE
    rk = size/2
OR
    rk = (size+2)/2
OR
    rk = (size+1)/2
    
ORDER BY
    company

-- Write your MySQL query statement below
WITH nT AS
(
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY Company ORDER BY Salary) AS rk,
        COUNT(Id) OVER (PARTITION BY Company) AS size
    FROM 
        Employee
)

SELECT
    id,
    company,
    salary
FROM
    nT
WHERE
    rk >= size/2 and rk <= size/2+1    
ORDER BY
    company