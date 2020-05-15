select ifnull(round(sum(session)/count(user_id), 2), 0) average_sessions_per_user from
(select
    user_id,
    count(distinct session_id) session
from
    Activity
where
    activity_date <='2019-07-27' and activity_date >= '2019-06-28'
group by
    user_id)T