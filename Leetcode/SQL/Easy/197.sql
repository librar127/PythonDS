/* Write your MySQL query statement below */

select id from
(select
    CASE WHEN DATEDIFF(B.RecordDate, A.RecordDate) =1 and B.Temperature > A.Temperature THEN B.ID end Id
from
    Weather A
JOIN
    Weather B)T
where id is not null

SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature


SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
      TO_DAYS(wt1.RecordDate)-TO_DAYS(wt2.RecordDate)=1;