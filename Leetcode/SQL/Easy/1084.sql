/* Write your MySQL query statement below */

SELECT
    product_id,
    product_name
FROM 
    PRODUCT
WHERE
    product_id NOT IN (
SELECT
    DISTINCT p.product_id
from
    Product p
JOIN
    Sales s
ON
    p.product_id = s.product_id
WHERE
    (s.sale_date < '2019-01-01' OR s.sale_date > '2019-03-31'))
    