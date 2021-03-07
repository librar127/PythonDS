# Write your MySQL query statement below

WITH nT1 as 
(
    SELECT
        product_id,
        -- change_date,
        new_price price,
        ROW_NUMBER() OVER(partition by product_id order by change_date DESC) rn
    FROm
       Products
    WHERE
        change_date <= '2019-08-16'
), nT2 AS
(
    SELECT
        product_id,
        10 AS price
    FROM
        Products
    WHERE
        change_date > '2019-08-16'
    AND
       product_id not in (SELECT DISTINCT product_id from nT1 ) 
)

SELECT 
    product_id,
    price
FROM
    nT1
WHERE
    rn = 1
UNION
SELECT
    product_id,
    price
FROM
    nT2
    