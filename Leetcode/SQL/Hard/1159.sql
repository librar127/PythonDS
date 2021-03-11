-- Write your MySQL query statement below

WITH nT AS
(    
    SELECT
        user_id,
        favorite_brand,
        order_date,
        item_brand,
        dense_rank() OVER (partition by user_id order by order_date) order_rank
    FROM
        users A
    LEFT JOIN
        Orders B
    JOIN
        Items C
    ON
        B.item_id = C.item_id
    ON
        A.user_id = B.seller_id
), second_favorite AS
(
    SELECT
        user_id seller_id,
        'yes' 2nd_item_fav_brand
    FROM
        nT
    WHERE
        order_rank=2
    AND
        favorite_brand=item_brand
        
)

SELECT
    *
FROM
    second_favorite 
UNION
SELECT
    user_id seller_id,
    'no' 2nd_item_fav_brand
FROM
    nT
WHERE
    user_id not in (SELECT DISTINCT seller_id FROM second_favorite)
GROUP BY
    user_id

ORDER BY
    seller_id