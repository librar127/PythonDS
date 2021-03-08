-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        SUBSTRING_INDEX(phone_number, "-", 1) country,
        duration country_duration
    FROM
        Person A
    JOIN
        Calls B
    ON
        A.id = B.caller_id
    UNION ALL
    SELECT
        SUBSTRING_INDEX(phone_number, "-", 1) country,
        duration country_duration
    FROM
        Person A
    JOIN
        Calls B
    ON
        A.id = B.callee_id
)

SELECT
   name as country
FROM
    Country A
JOIN
    nT B
ON
    A.country_code = B.country
GROUP BY
    name
HAVING avg(country_duration) > (SELECT AVG(duration) FROM Calls)
