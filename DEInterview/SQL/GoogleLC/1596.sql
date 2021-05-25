# Write your MySQL query statement below

WITH customer_product_tbl AS
(
    SELECT
        customer_id,
        product_id,
        count(product_id) prod_cnt
    FROm
        Orders 
    GROUP BY
        customer_id,
        product_id
),

customer_max_product_tbl AS
(
    SELECT        
        customer_id,
        max(prod_cnt) max_cnt
    FROM
        customer_product_tbl
    GROUP BY
        customer_id
)
-- SELECT * FROM customer_max_product_tbl ORDER BY customer_id

SELECT
    A.customer_id,
    A.product_id,
    B.product_name
FROm
    customer_product_tbl A
JOIN
    Products B
ON
    A.product_id = B.product_id
JOIN
    customer_max_product_tbl C
ON  
    A.customer_id = C.customer_id
AND
    A.prod_cnt = C.max_cnt
    