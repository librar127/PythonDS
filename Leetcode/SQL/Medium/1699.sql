# Write your MySQL query statement below

WITH nT1 AS
(
    SELECT
        A.from_id,
        A.to_id,
        count(*) cnt,
        SUM(A.duration) t_duration
    FROM
        Calls A
    WHERE
        A.from_id < A.to_id
    GROUP BY
        A.from_id,
        A.to_id
), nT2 AS
(
    SELECT
        A.from_id to_id,
        A.to_id from_id,
        count(*) cnt,
        SUM(A.duration) t_duration
    FROM
        Calls A
    WHERE
        A.to_id < A.from_id
    GROUP BY
        A.from_id,
        A.to_id
)

-- select * from nT1;
SELECT
    A.from_id person1,
    A.to_id person2,
    A.cnt + B.cnt call_count,
    A.t_duration + B.t_duration as total_duration
FROM
    nT1 A
JOIN
    nT2 B
ON
    A.from_id = B.from_id
AND
    A.to_id = B.to_id
UNION
SELECT
    A.from_id person1,
    A.to_id person2,
    A.cnt call_count,
    A.t_duration as total_duration
FROM
    nT1 A
LEFT JOIN
    nT2 B
ON
    A.from_id = B.from_id
AND
    A.to_id = B.to_id
WHERE
    B.from_id is NULL
UNION
SELECT
    B.from_id person1,
    B.to_id person2,
    B.cnt call_count,
    B.t_duration as total_duration
FROM
    nT1 A
RIGHT JOIN
    nT2 B
ON
    A.from_id = B.from_id
AND
    A.to_id = B.to_id
WHERE
    A.from_id is NULL