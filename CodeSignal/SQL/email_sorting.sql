CREATE PROCEDURE orderingEmails()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        id,
        email_title,
        case when size >= 1024*1024 then CONCAT(floor(size/(1024*1024)), ' Mb') else CONCAT(floor(size/(1024)), ' Kb') end as short_size
    from 
        emails
    order by 
        size desc;        
END