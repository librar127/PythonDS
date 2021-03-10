-- Write your MySQL query statement below

WITH recursive years AS
(
    SELECT
        min(YEAR(period_start)) year
    FROM
        Sales
    UNION ALL
    SELECT
        year+1
    FROM
        years
    WHERE
        year < (SELECT MAX(YEAR(period_end)) FROM sales)
    
), year_prod as
(
    SELECT
        A.year,
        B.product_id,
        B.product_name,
        C.period_start,
        C.period_end,
        C.average_daily_sales
    FROM
        years A,
        Product B,
        Sales C
    WHERE
        A.year >= YEAR(C.period_start) and YEAR <= YEAR(C.period_end)
    AND
        B.product_id = C.product_id
)

SELECT 
    CAST(product_id AS CHAR)product_id,
    product_name,
    CAST(year as CHAR) report_year,
    CASE
        WHEN year = YEAR(period_start) and year = YEAR(period_end) THEN (datediff(period_end, period_start)+1) * average_daily_sales 
        WHEN year = YEAR(period_start) and year < YEAR(period_end) THEN (datediff(str_to_date(concat(year, "-12-31"), "%Y-%m-%d"), period_start)+1) * average_daily_sales 
        WHEN year > YEAR(period_start) and year = YEAR(period_end) THEN (datediff(period_end, str_to_date(concat(year, "-01-01"), "%Y-%m-%d"))+1) * average_daily_sales
        WHEN year > YEAR(period_start) and year < YEAR(period_end) THEN 365 * average_daily_sales        
    END as total_amount
FROM
    year_prod
ORDER BY
    product_id,
    report_year
    