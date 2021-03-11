WITH CTE AS
(
    SELECT 
        player_id, 
        SUM(score) AS total_score
    FROM
        (SELECT 
            first_player AS player_id,
            SUM(first_score) AS score
        FROM 
            Matches
        GROUP BY 
            first_player

        UNION ALL

        SELECT
            second_player AS player_id,
            SUM(second_score) AS score
        FROM 
            Matches
        GROUP BY
            second_player
        ) T
    GROUP BY 
        player_id
)

SELECT 
    group_id, 
    player_id
FROM
    (SELECT 
        group_id, 
        p.player_id, 
        DENSE_RANK() OVER(PARTITION BY group_id ORDER BY total_score DESC, p.player_id ASC) AS rank1
    FROM 
        Players p
    LEFT JOIN 
        CTE
    ON 
        p.player_id = CTE.player_id
    ) R
WHERE 
    rank1 = 1