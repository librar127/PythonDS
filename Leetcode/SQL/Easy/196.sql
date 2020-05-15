/* Write your MySQL query statement below */
delete 
from
    person
where
    id not in (select * from 
        (select
            min(Id)
        from
            person
        group by
            email)T)