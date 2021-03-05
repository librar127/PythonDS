-- 1. Company Employees
CREATE PROCEDURE companyEmployees()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        D.DEP_NAME,
        E.EMP_NAME
    FROM    
        departments D, employees E
    ORDER BY
        D.DEP_NAME,
        E.EMP_NAME;
END

-- 2. Scholership Distribution
CREATE PROCEDURE scholarshipsDistribution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        candidate_id AS student_id
    FROM 
        candidates
    WHERE 
        candidate_id NOT IN (SELECT DISTINCT student_id FROM detentions)
    ORDER BY 
        student_id;
END

-- 3. User Countries
CREATE PROCEDURE userCountries()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        ID,
        COALESCE(COUNTRY, "unknown")
    FROM
        users U
    LEFT JOIN
        cities C
    ON 
        U.city = C.city;
END

-- 4. Places of Interest
CREATE PROCEDURE placesOfInterestPairs()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        A.NAME AS place1,
        B.NAME AS place2
    FROM
        sights A
    CROSS JOIN
        sights B
    WHERE
        SQRT(POWER((A.X - B.X), 2) + POWER((A.Y - B.Y), 2)) < 5
    AND
        A.NAME < B.NAME
    ORDER BY 
        PLACE1, PLACE2;
END

-- 5. Local calendar
CREATE PROCEDURE localCalendar()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        A.event_id,
        CASE WHEN B.hours=24 THEN date_format(date_add(A.DATE, interval B.timeshift minute), "%Y-%m-%d %H:%i") 
        
        WHEN B.hours=12 AND EXTRACT(hour from date_add(A.DATE, interval B.timeshift minute)) > 12 THEN
        concat(date_format(date_sub(date_add(A.DATE, interval B.timeshift minute), interval 12 hour), "%Y-%m-%d %H:%i"), " PM") 
        
        WHEN B.hours=12 AND EXTRACT(hour from date_add(A.DATE, interval B.timeshift minute)) = 12 THEN
        concat(date_format(date_add(A.DATE, interval B.timeshift minute), "%Y-%m-%d %H:%i"), " PM")
        
        WHEN B.hours=12 AND EXTRACT(hour from date_add(A.DATE, interval B.timeshift minute)) < 12 THEN
        concat(date_format(date_add(A.DATE, interval B.timeshift minute), "%Y-%m-%d %H:%i"), " AM")
        END as formatted_date
    FROM
        events A
    JOIN
        settings B
    ON 
        A.user_id = B.user_id 
    ORDER BY
        A.event_id;         
END

-- 6. Route Length
CREATE PROCEDURE routeLength()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select 
        round(sum(sqrt(power((c1.x-c2.x), 2) + power((c1.y-c2.y), 2))), 9)total
    from cities c1
    join cities c2
    on c1.id = c2.id+1;
END

-- 6. Scond Solution using window function
CREATE PROCEDURE routeLength()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    with nT as
    (
        SELECT t.*,
            LAG(t.x) OVER (ORDER BY t.ID) as prev_x, 
            LAG(t.y) OVER (ORDER BY t.ID) as prev_y 
        FROM 
            cities AS t)
            
    select 
        round(sum(sqrt(power((x-prev_x), 2) + power((y-prev_y), 2))), 9)
    FROM
        nT;
END