-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        A.contest_id,
        count(distinct A.user_id) user_count
    FROM
        Register A
    JOIN
        Users B
    ON
        A.user_id = B.user_id
    GROUP BY
        A.contest_id
)

SELECT
    A.contest_id,
    round(A.user_count*100 / (SELECT count(DISTINCT USER_ID) from Users), 2) as percentage
FROM
    nT A
ORDER BY
    percentage DESC,
    contest_id


-- Write your MySQL query statement below
SELECT
    A.contest_id,
    round(count(distinct A.user_id)*100 / (SELECT count(DISTINCT USER_ID) from Users), 2) as percentage
FROM
    Register A
JOIN
    Users B
ON
    A.user_id = B.user_id
GROUP BY
    A.contest_id
ORDER BY
    percentage DESC,
    contest_id