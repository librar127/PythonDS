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

--- Second Attempt Below

-CREATE PROCEDURE soccerGameSeries()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
     with nT as 
    (
        select
            sum(case when first_team_score > second_team_score then 1 
                when first_team_score < second_team_score then -1 else 0 end) as diff_score,
            sum(first_team_score) as total_first,
            sum(second_team_score) as total_second,
            sum(case when match_host = 2 then first_team_score
                     when match_host = 1 then -1*second_team_score
                     else 0 end) as home_away_score            
        from 
            scores
    )
    select 
        case 
            when diff_score > 0 then 1 
            when diff_score < 0 then 2
            when diff_score = 0 and total_first > total_second then 1 
            when diff_score = 0 and total_first < total_second then 2
            when diff_score = 0 and total_first = total_second and home_away_score > 0 then 1
            when diff_score = 0 and total_first = total_second and home_away_score < 0 then 2
            else 0 
        end as winner
    from
        nT;    
END