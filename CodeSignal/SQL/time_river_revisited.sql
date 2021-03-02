-- 1: Important Events
CREATE PROCEDURE importantEvents()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        id
        ,name	
        ,event_date	
        ,participants
    FROM
        events
    ORDER BY
        WEEKDAY(event_date),
        participants DESC;
END

-- 2: dateFormatting
CREATE PROCEDURE dateFormatting()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        DATE_FORMAT(date_str, '%Y-%m-%d') AS date_iso
    FROM
        documents;
END

--3: pastEvents
CREATE PROCEDURE pastEvents()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        name,
        event_date
    FROM
        Events
    WHERE
        DATEDIFF((select max(event_date) from Events), event_date) >0 and DATEDIFF((select max(event_date) from Events), event_date) <= 7
    ORDER BY 
        event_date DESC;
END

--4: Net Income
CREATE PROCEDURE netIncome()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SET sql_mode = 'NO_UNSIGNED_SUBTRACTION';
    SELECT
        YEAR(DATE)  AS YEAR,
        QUARTER(DATE) AS quarter,
        SUM(profit-loss) AS net_profit
    FROM
        accounting
    GROUP BY
        YEAR(DATE),
        QUARTER(DATE)
    ORDER BY
        YEAR, quarter;        
END

-- 5: Alarm Clock- Copied solution, I do not understand it!
CREATE PROCEDURE alarmClocks()
BEGIN
    select @a alarm_date
        from userInput, 
             (select 1 union select 2 union select 3 union select 4) x,
             (select 1 union select 2 union select 3 union select 4) y,
             (select 1 union select 2 union select 3 union select 4) z
        where year(ifnull(@a:=date_add(@a, interval 1 week), @a:=input_date)) 
            = year(input_date);
END