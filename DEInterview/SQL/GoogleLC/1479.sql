# Write your MySQL query statement below
WITH sale_by_weekday_tbl AS
(
    SELECT
        CASE
            WHEN DAYOFWEEK(order_date) = 2 THEN 'Monday' 
            WHEN DAYOFWEEK(order_date) = 3 THEN 'Tuesday' 
            WHEN DAYOFWEEK(order_date) = 4 THEN 'Wednesday' 
            WHEN DAYOFWEEK(order_date) = 5 THEN 'Thursday' 
            WHEN DAYOFWEEK(order_date) = 6 THEN 'Friday' 
            WHEN DAYOFWEEK(order_date) = 7 THEN 'Saturday' 
            ELSE 'Sunday'
        END AS WeekDay,
        item_category as Category,
        SUM(IFNULL(quantity, 0)) quantity
    FROM
        Orders A
    RIGHT JOIN
       Items B
    ON
        A.item_id = B.item_id
    GROUP BY
        WeekDay,
        Category
)

SELECT
    Category,
    SUM(CASE WHEN WeekDay = 'Monday' THEN quantity else 0 END) Monday,
    SUM(CASE WHEN WeekDay = 'Tuesday' THEN quantity else 0 END) Tuesday,
    SUM(CASE WHEN WeekDay = 'Wednesday' THEN quantity else 0 END) Wednesday,
    SUM(CASE WHEN WeekDay = 'Thursday' THEN quantity else 0 END) Thursday,
    SUM(CASE WHEN WeekDay = 'Friday' THEN quantity else 0 END) Friday,
    SUM(CASE WHEN WeekDay = 'Saturday' THEN quantity else 0 END) Saturday,
    SUM(CASE WHEN WeekDay = 'Sunday' THEN quantity else 0 END) Sunday
FROM
    sale_by_weekday_tbl
GROUP BY
    Category
ORDER BY
    Category