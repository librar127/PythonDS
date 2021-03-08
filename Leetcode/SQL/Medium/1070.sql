-- Write your MySQL query statement below
WITH nT AS
(    
    SELECT
       product_id,
       year as first_year,
       quantity,
       price,
       RANK() OVER(PARTITION BY product_id ORDER BY YEAR) rn
    FROM
        Sales   
)

SELECT
   product_id,
   first_year,
   quantity,
   price
FROM
    nT
WHERE
    rn = 1