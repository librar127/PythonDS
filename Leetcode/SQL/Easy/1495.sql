# Write your MySQL query statement below
SELECT
    DISTINCT B.TITLE
FROM
    TVProgram A
JOIN
    Content B
ON
    A.content_id = B.content_id
WHERE
    B.Kids_content = 'Y'
AND
    month(program_date) = 6
AND
    content_type = 'Movies'