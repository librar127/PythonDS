# Write your MySQL query statement below
WITH nT as
(
    SELECT
        stock_name,
        sum(case when operation = 'Buy' then price else 0 end) as buy_price,
        sum(case when operation = 'Sell' then price else 0 end) as sell_price
    FROM
        Stocks
    GROUP BY
        stock_name
)

SELECT
    stock_name,
    (sell_price - buy_price) as capital_gain_loss
FROM
    nT