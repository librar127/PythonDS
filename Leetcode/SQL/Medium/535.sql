-- Write your MySQL query statement below
SELECT
    player_id,
    event_date,
    SUM(games_played) OVER(partition by player_id order by event_date)games_played_so_far
FROM
    Activity