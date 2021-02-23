CREATE PROCEDURE soccerGameSeries()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
     with nT as 
    (
        select
            sum(case when first_team_score-second_team_score > 0 then 1 
                when first_team_score-second_team_score < 0 then -1 else 0 end) as diff_score,
            sum(first_team_score) as total_first,
            sum(second_team_score) as total_second,
            sum(case when first_team_score-second_team_score > 0 and match_host=2 then first_team_score
                     when second_team_score-first_team_score > 0 and match_host=1 then -1*second_team_score
                     else 0 end) as frequent_host            
        from 
            scores
    )
    select 
        case when diff_score > 0 then 1 
        when diff_score < 0 then 2
        when diff_score = 0 and (total_first - total_second) > 0 then 1 
        when diff_score = 0 and (total_first - total_second) < 0 then 2
        when diff_score = 0 and (total_first - total_second) = 0 and frequent_host > 0 then 1
        when diff_score = 0 and (total_first - total_second) = 0 and frequent_host < 0 then 2 else 0 end as winner
    from
        nT;    
END

--- 7/8 Test cases passed

--- Someone else's code
/*Please add ; after each select statement*/
CREATE PROCEDURE soccerGameSeries()
BEGIN
    SELECT
        CASE
            WHEN stats.`first_team_wins` > stats.`second_team_wins` THEN 1
            WHEN stats.`second_team_wins` > stats.`first_team_wins` THEN 2
            WHEN stats.`goal_diff` > 0 THEN 1
            WHEN stats.`goal_diff` < 0 THEN 2
            WHEN stats.`first_team_points` > stats.`second_team_points` THEN 1
            WHEN stats.`second_team_points` > stats.`first_team_points` THEN 2
            ELSE 0
        END AS `winner`
    FROM
    (
        SELECT
            SUM(scores.`first_team_score` > scores.`second_team_score`) `first_team_wins`,
            SUM(scores.`first_team_score` < scores.`second_team_score`) `second_team_wins`,
            SUM(scores.`first_team_score` - scores.`second_team_score`) `goal_diff`,
            SUM((scores.`match_host` = 2) * scores.`first_team_score`) `first_team_points`,
            SUM((scores.`match_host` = 1) * scores.`second_team_score`) `second_team_points`
        FROM
            scores
    ) AS stats;
END