-- Write your MySQL query statement below
WITH nT AS
(    
    SELECT
        visited_on,
        SUM(amount) amount
        -- SUM(amount) over(ORDER BY visited_on ROWS BETWEEN 7 PRECEDING and CURRENT ROW) 7_day_sum,
        -- DENSE_RANK() OVER (ORDER BY visited_on) rn
    FROM
        Customer
    GROUP BY
        visited_on
), nT2 AS
(
    SELECT
        visited_on,
        ROUND(SUM(amount) over(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING and CURRENT ROW), 2) 7_day_sum,
        RANK() OVER (ORDER BY visited_on) rn
    FROM
        nT
)

SELECT 
    visited_on,
    7_day_sum amount,
    ROUND((7_day_sum/7), 2)average_amount
FROM 
    nT2
WHERE 
    rn > 6
ORDER BY
    visited_on