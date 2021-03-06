# Write your MySQL query statement below

WITH nT as
(

    SELECT 
        A.customer_id,
        A.product_id,
        B.product_name,
        COUNT(*) cnt
    FROM
        Orders A
    JOIN
        Products B
    ON
        A.product_id = B.product_id
    GROUP BY
        A.customer_id,
        A.product_id
    ORDER BY
        A.customer_id
), nT2 AS
(
    SELECT
        customer_id,
        product_id,
        product_name,
        rank() OVER (PARTITION BY customer_id order by cnt DESC) rn
    FROM
        nT
)

SELECT 
        customer_id,
        product_id,
        product_name
FROM
    nT2
WHERE
    rn = 1