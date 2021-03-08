-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        team_id,
        team_name,
        CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            WHEN host_goals < guest_goals THEN 0
            ELSE 0
        END AS num_points
    FROM
        Teams A
    LEFT JOIN
        Matches B
    ON
        A.team_id = B.host_team 
    UNION ALL
    SELECT
        team_id,
        team_name,
        CASE
            WHEN guest_goals > host_goals THEN 3
            WHEN guest_goals = host_goals THEN 1
            WHEN guest_goals < host_goals THEN 0
            ELSE 0
         END AS num_points
    FROM
        Teams A
    LEFT JOIN
        Matches B
    ON
        A.team_id = B.guest_team 
)

SELECT
    team_id,
    team_name,
    SUM(num_points)num_points
FROM
    nT
GROUP BY
    team_id,
    team_name
ORDER BY 
    num_points DESC,
    team_id