# Write your MySQL query statement below
SELECT
    sale_date,
    (sum(CASE WHEN fruit='apples' then sold_num else 0 end) - sum(CASE WHEN fruit='oranges' then sold_num else 0 end)) as diff
FROM
    Sales
GROUP BY
    sale_date
ORDER BY
    sale_date
    