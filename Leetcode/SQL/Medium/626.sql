-- Write your MySQL query statement below
SELECT
    CASE
        WHEN MOD(id, 2) != 0 and id = counts then id
        WHEN MOD(id, 2) = 0 and id = counts then id-1
        WHEN MOD(id, 2) != 0 and id < counts then id+1
        WHEN MOD(id, 2) = 0 and id < counts then id-1
    END as id,
    student
FROM
    seat,
(SELECT count(*) counts from seat) ss
ORDER BY
    id
    