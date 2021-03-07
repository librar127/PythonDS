--  your MySQL query statement below
WITH nT AS
(
    SELECT
        B.product_name,
        B.product_id,
        A.order_id,
        A.order_date,
        DENSE_RANK() OVER (PARTITION BY product_name ORDER BY order_date DESC) rn
    FROM
        Orders A
    JOIN
        Products B
    ON
        A.product_id = B.product_id
    
)

SELECT
    product_name,
    product_id,
    order_id,
    order_date
FROM
    nT
WHERE
    rn = 1
ORDER BY
    product_name,
    product_id,
    order_id