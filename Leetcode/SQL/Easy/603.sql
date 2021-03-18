-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        seat_id, 
        free,
        seat_id - row_number() over(order by seat_id) rn
    From
        cinema
    WHERE
        free = 1
    ORDER BY
        seat_id
), nT2 AS
(
    SELECT
        rn
    FROM
        nT
    GROUP BY
        rn
    HAVING
        count(distinct seat_id) >= 2
)

SELECT
    distinct seat_id
FROM
    nT 
WHERE
    rn in (SELECT DISTINCT rn from nT2)
ORDER BY
    seat_id


select 
    distinct a.seat_id
from
    cinema a
join
    cinema b
on
    a.seat_id = b.seat_id+1 or a.seat_id = b.seat_id-1
where
    a.free = 1 and b.free = 1
order by
    a.seat_id
