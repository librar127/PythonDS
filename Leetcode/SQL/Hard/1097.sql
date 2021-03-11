-- Write your MySQL query statement below
WITH nT as
(
    SELECT
        player_id,
        min(event_date) install_dt
    FROM
        Activity
    group by
        player_id
)

SELECT
    install_dt,
    count(distinct A.player_id)installs,
    ROUND(SUM(CASE WHEN datediff(event_date, install_dt)=1 THEN 1 ELSE 0 END) / count(distinct A.player_id), 2) Day1_retention
FROM
    nT A
JOIN
    Activity B
ON
    A.player_id = B.player_id
GROUP BY
    install_dt
ORDER BY
    install_dt
        