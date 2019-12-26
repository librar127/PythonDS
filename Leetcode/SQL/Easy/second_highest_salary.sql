# Write your MySQL query statement below
SELECT max(Salary) as SecondhighestSalary
FROM Employee
Where Salary < (Select max(Salary)
               From Employee)
