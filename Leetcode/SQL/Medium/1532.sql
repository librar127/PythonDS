# Write your MySQL query statement below

WITH nT AS
(
    SELECT
        A.name customer_name,
        A.customer_id,
        B.order_id,
        B.order_date,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date DESC) rn
    FROM
        Customers A
    JOIN
        Orders B
    ON
        A.customer_id = B.customer_id
)

SELECT
    customer_name,
    customer_id,
    order_id,
    order_date
FROM
    nT
WHERE 
    rn < 4
ORDER BY
    customer_name, 
    customer_id,
    order_date DESC
    