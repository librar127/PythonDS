-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        A.user_id,
        A.join_date,
        B.order_date
        -- SUM(CASE WHEN YEAR(B.order_date) = 2019 THEN 1 ELSE 0 END)orders_in_2019
    FROM
        Users A
    LEFT JOIN
        Orders B
    ON 
        A.user_id = B.buyer_id
    LEFT JOIN
        Items C
    ON
        B.item_id = C.item_id
)

SELECT 
    user_id buyer_id,
    join_date,
    SUM(CASE WHEN YEAR(order_date) = 2019 THEN 1 ELSE 0 END)orders_in_2019
FROM
    nT
GROUp BY
    user_id,
    join_date
    

-- ANSWER 2
SELECT
    A.user_id buyer_id,
    A.join_date,
    SUM(CASE WHEN B.order_date IS NOT NULL AND YEAR(B.order_date) = 2019 THEN 1 ELSE 0 END)orders_in_2019
FROM
    Users A
LEFT JOIN
    Orders B
ON 
    A.user_id = B.buyer_id
GROUP BY
    A.user_id,
    A.join_date