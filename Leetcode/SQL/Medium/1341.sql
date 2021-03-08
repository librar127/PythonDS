-- Write your MySQL query statement below
WITH nT AS
(
    SELECT 
        title,
        AVG(rating)rating
    FROM 
        Movies A
    JOIN
        Movie_Rating B
    ON
        A.movie_id = B.movie_id
    WHERE
        DATE_FORMAT(created_at, "%Y-%m") = "2020-02"
    GROUP BY
        title
)

(SELECT
    name results  
FROM
    Users A
JOIN
    Movie_Rating B
ON
    A.user_id = B.user_id
GROUP BY
    name
ORDER BY
    COUNT(distinct movie_id) DESC,
    NAME
LIMIT 1)
UNION
(
SELECT
    min(title) results
FROM
    nT
WHERE
    rating = (SELECT MAX(rating) FROM nT)
)