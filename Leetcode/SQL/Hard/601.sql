-- Write your MySQL query statement below

-- First Approach
WITH rn_visits AS
(
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER(order by visit_date) rn
    FROM
        Stadium
    WHERE
        people >= 100
),

seq_visits AS
(
    SELECT
        rn,
        count(distinct visit_date) cnt
    FROM
        rn_visits
    WHERE
        people >= 100
    GROUP BY
        rn
    Having
        count(distinct visit_date) >= 3
)
    
SELECT
    id, 
    visit_date,
    people
FROM
    rn_visits A
JOIN
    seq_visits B
ON
    A.rn = B.rn
ORDER BY
    id

-- SECOND Approach

SELECT
    distinct
    A.id,
    A.visit_date,
    A.people
FROM
    Stadium A, Stadium B, Stadium C
WHERE
    A.people >= 100
AND
    B.people >= 100
AND
    C.people >= 100
AND
    ((A.id +1 = B.id AND A.id + 2 = C.id AND B.id+1 = C.id) 
OR
    (A.id -1 = B.id AND A.id + 1 = C.id AND B.id+2 = C.id)  
OR
    (A.id -2 = B.id AND A.id - 1 = C.id AND B.id+1 = C.id))
ORDER BY
    ID