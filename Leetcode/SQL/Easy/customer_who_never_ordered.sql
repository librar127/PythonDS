# Write your MySQL query statement below
SELECT
    Name Customers
FROM
    Customers 
WHERE 
    ID NOT IN (SELECT DISTINCT CustomerId FROM ORDERS)
