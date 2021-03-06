-- Write your MySQL query statement below

SELECT
    id,
    CASE
        WHEN p_id is NULL then "Root"
        WHEN id in (select distinct p_id from tree where p_id is not null) THEN "Inner"
        ELSE "Leaf" END as Type
FROm
    tree