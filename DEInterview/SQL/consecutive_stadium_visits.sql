SELECT DISTINCT A.* FROM stadium A, stadium B, stadium C WHERE A.people>100 AND B.people>100 AND C.people > 100 
AND ((A.id+1 = B.id AND B.id+1 = C.ID) OR (A.id-1 = B.id AND A.id+1 = C.id) OR (A.id-2 = B.id AND A.id-1 = C.id)) ORDER BY ID;

SELECT DISTINCT A.* FROM stadium A, stadium B WHERE A.people>100 AND B.people>100
AND ((A.id+1 = B.id) OR (A.id-1 = B.id)) order by id;


with tab_1 as 
(
    select 
        * 
    from 
        stadium 
    where 
        people > 100
),
tab_2 as (
    select *, id - ROW_NUMBER() over (order by id) as diff
    from tab_1
),
tab_3 as (
    select 
        *, count(*) over(partition by diff) diff_c 
    from 
        tab_2
)
select id, date, people from tab_3 where diff_c >= 2;