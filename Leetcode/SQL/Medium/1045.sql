-- Write your MySQL query statement below
SELECT
    customer_id
    -- COUNT(DISTINCT product_key) product_cnt
FROM
    Customer
GROUP BY
    customer_id
HAVING 
    COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)