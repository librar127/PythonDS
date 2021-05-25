# Write your MySQL query statement below
SELECT
    DISTINCT
    s1.id,
    s1.visit_date,
    s1.people
FROM
    Stadium s1, 
    Stadium s2,
    Stadium s3
WHERE
    ((s1.id = s2.id-1 and s1.id = s3.id-2) 
OR 
    (s1.id = s2.id+1 and s1.id = s3.id-1) 
OR 
    (s1.id = s2.id+2 and s1.id = s3.id+1))
AND 
    s1.people >= 100
AND 
    s2.people >= 100
AND 
    s3.people >= 100
ORDER BY
    s1.id
    


/*
WITH filtered_tbl AS
(
    SELECT
        id,
        visit_date,
        people,
        id - row_number() over(order by visit_date) row_n
    FROM
        Stadium
    WHERE
        people >= 100
),
final_tbl as
(
    SELECT
        id, 
        visit_date,
        people,
        count(id) over(partition by row_n) cons_cnt
    FROM
       filtered_tbl 
)

SELECT    
    id, 
    visit_date,
    people
FROM
    final_tbl
WHERE
    cons_cnt >= 3
ORDER BY
    id
*/