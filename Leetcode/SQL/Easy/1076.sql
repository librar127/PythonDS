/* Write your MySQL query statement below */
select
    project_id
from    
    Project
group by 
    project_id 
having
    count(distinct employee_id) = (

select num_employees from
(select
    project_id,
    count(distinct employee_id) num_employees
from    
    Project
group by 
    project_id 
order by 
    num_employees desc)T LIMIT 1)
