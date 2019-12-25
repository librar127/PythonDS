# Write your MySQL query statement below

SELECT DISTINCT(salary) AS salary
FROM EMPLOYEE
ORDER BY salary DESC
LIMIT 1 OFFSET (n - 1);