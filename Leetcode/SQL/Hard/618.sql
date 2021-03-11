-- Write your MySQL query statement below

WITH nT AS
(   
    SELECT
        name,
        continent,
        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) rn    
    FROM
        student
)
SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) Europe
FROM
    nT
GROUP BY
    rn
ORDER BY
    rn