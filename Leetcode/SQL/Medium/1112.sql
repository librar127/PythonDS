-- Write your MySQL query statement below
WITH nT AS
(
    SELECT
        student_id,
        course_id,
        grade,
        ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id) rn
    FROM
        Enrollments
)

SELECT
    student_id,
    course_id,
    grade
FROM 
    nT
WHERE
    rn = 1
ORDER BY
    student_id
