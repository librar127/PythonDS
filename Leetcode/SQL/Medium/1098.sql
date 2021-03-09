-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        A.book_id,
        A.name
    FROM
        Books A
    WHERE
        datediff("2019-06-23", available_from) > 30
)

SELECT
    A.book_id,
    A.name
FROM
    nT A
LEFT JOIN
    Orders B
ON
    A.book_id = B.book_id
AND
    datediff("2019-06-23", dispatch_date) <= 365
GROUP BY
    A.book_id,
    A.name
HAVING
    SUM(ifnull(quantity, 0)) < 10
    