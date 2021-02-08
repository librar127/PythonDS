/* Write your SQL here. Terminate each statement with a semicolon. */
select 
    subscriber
from
    full_year
where
    newspaper like '%Daily%'
UNION
select 
    subscriber
from
    half_year
where
    newspaper like '%Daily%'
order by
    SUBSTRING_INDEX(subscriber, ' ', 1);