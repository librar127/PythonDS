# Write your MySQL query statement below
SELECT 
    SELL_DATE,
    COUNT(DISTINCT ProDUCT) num_sold,
    GROUP_CONCAT(DISTINCT ProDUCT ORDER BY ProDUCT) AS products
FROM
    Activities
GROUP BY
    SELL_DATE
ORDER BY    
    SELL_DATE