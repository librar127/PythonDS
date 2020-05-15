/* Write your MySQL query statement below */
select 
    IFNULL(round(
        (select count(*) from (select distinct requester_id , accepter_id from request_accepted)B)/(select count(*) from (select distinct sender_id, send_to_id from friend_request)A), 2), 0) accept_rate
        
        