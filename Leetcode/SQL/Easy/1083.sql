/* Write your MySQL query statement below */
select 
    distinct buyer_id 
from
    sales s
join
    product p
on
    s.product_id = p.product_id
where
    p.product_name = 'S8' 
and
    buyer_id not in (

select 
    distinct buyer_id 
from
    sales s
join
    product p
on
    s.product_id = p.product_id
where
    p.product_name = 'iPhone')
