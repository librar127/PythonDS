-- Write your MySQL query statement below
SELECT
    CASE 
        when id % 2 > 0 and id <> t.cnt then id+1
        when id % 2 > 0 and id = t.cnt then id
        else id-1
    end as id,
    student
FROM
    seat,
    (select count(*) cnt from seat)t
ORDER BY
    id 
        