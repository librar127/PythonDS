-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        A.id,
        A.name,
        login_date,
        LEAD(login_date, 4) OVER(PARTITION BY A.id ORDER BY login_date) fifth_date
    FROM
        Accounts A    
    JOIN
        Logins B
    ON
        A.id = B.id
    GROUP BY
        id, 
        name,
        login_date
)
SELECT
    DISTINCT
    id,
    name
FROM
    nT
WHERE
    datediff(fifth_date, login_date) = 4
    