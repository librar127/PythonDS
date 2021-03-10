-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        item_category Category,
        CASE 
            WHEN weekday(order_date) = 0 THEN 'Monday'
            WHEN weekday(order_date) = 1 THEN 'Tuesday'
            WHEN weekday(order_date) = 2 THEN 'Wednesday'
            WHEN weekday(order_date) = 3 THEN 'Thursday'
            WHEN weekday(order_date) = 4 THEN 'Friday'
            WHEN weekday(order_date) = 5 THEN 'Saturday'
            WHEN weekday(order_date) = 6 THEN 'Sunday'
        END as weekday,
        sum(ifnull(quantity, 0)) quantity
    FROM
        Items A
    LEFT JOIN    
        Orders B
    ON
        A.item_id = B.item_id
    GROUP BY
        item_category,
        weekday
)
SELECT
    Category,
    SUM(CASE WHEN weekday = 'Monday' THEN quantity ELSE 0 END) as Monday,
    SUM(CASE WHEN weekday = 'Tuesday' THEN quantity ELSE 0 END) as Tuesday,
    SUM(CASE WHEN weekday = 'Wednesday' THEN quantity ELSE 0 END) as Wednesday,
    SUM(CASE WHEN weekday = 'Thursday' THEN quantity ELSE 0 END) as Thursday,
    SUM(CASE WHEN weekday = 'Friday' THEN quantity ELSE 0 END) as Friday,
    SUM(CASE WHEN weekday = 'Saturday' THEN quantity ELSE 0 END) as Saturday,
    SUM(CASE WHEN weekday = 'Sunday' THEN quantity ELSE 0 END) as Sunday
FROM
    nT
GROUP BY
    Category
ORDER BY
    Category
        