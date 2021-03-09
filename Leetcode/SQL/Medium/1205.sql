-- Write your MySQL query statement below
WITH nT AS
(    
    SELECT
        DATE_FORMAT(trans_date, "%Y-%m")month,
        country,
        COUNT(*) approved_count,
        SUM(amount)approved_amount
    FROM
        Transactions
    WHERE  
        state = 'approved'
    GROUP BY
        DATE_FORMAT(trans_date, "%Y-%m"),
        country
), nT2 AS
( 
    SELECT
        DATE_FORMAT(A.trans_date, "%Y-%m")month,
        B.country,
        COUNT(B.id) chargeback_count,
        SUM(amount) chargeback_amount
    FROM
        Chargebacks A
    JOIN
        Transactions B
    ON 
        A.trans_id = B.id 
    GROUP BY
        DATE_FORMAT(A.trans_date, "%Y-%m"),
        B.country
)

SELECT 
    A.month,
    A.country,
    COALESCE(approved_count, 0) approved_count,
    COALESCE(approved_amount, 0)approved_amount,
    COALESCE(chargeback_count, 0)chargeback_count,
    COALESCE(chargeback_amount, 0)chargeback_amount
FROM
    nT2 A
LEFT JOIN
    nT B
USING
    (country, month)
UNION

SELECT 
    B.month,
    B.country,
    COALESCE(approved_count, 0) approved_count,
    COALESCE(approved_amount, 0)approved_amount,
    COALESCE(chargeback_count, 0)chargeback_count,
    COALESCE(chargeback_amount, 0)chargeback_amount
FROM
    nT2 A
RIGHT JOIN
    nT B
USING
    (country, month)