--  Write your MySQL query statement below
WITH nT AS
(
    SELECT
        A.customer_id,
        A.customer_name,
        GROUP_CONCAT(product_name) products_purchased
    FROM
        Customers A
    JOIN
        Orders B
    ON 
        A.customer_id = B.customer_id
    GROUP BY
        A.customer_id
)

SELECT
    customer_id,
    customer_name
FROM
    nT
WHERE 
    FIND_IN_SET('A', products_purchased) > 0 
AND
    FIND_IN_SET('B', products_purchased) > 0 
AND
    FIND_IN_SET('C', products_purchased) = 0     
    