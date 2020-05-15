/* Write your MySQL query statement below */

SELECT 
    E1.NAME Employee
FROM
    EMPLOYEE E1
JOIN
    EMPLOYEE E2
ON
    E1.MANAGERID = E2.ID
AND
    E1.SALARY > E2.SALARY