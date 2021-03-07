-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        customer_id,
        min(order_date) first_order
    FROM
        Delivery
    GROUP BY
        customer_id
)

SELECT
    ROUND(SUM(CASE WHEN first_order = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100/ COUNT(*), 2) immediate_percentage
FROM
    nT A
JOIN
   Delivery B
ON 
    A.customer_id = B.customer_id
AND
    A.first_order = B.order_date