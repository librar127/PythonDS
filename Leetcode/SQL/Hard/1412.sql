-- Write your MySQL query statement below

WITH min_max_score as
(
    SELECT
        exam_id,
        min(score) min_score,
        max(score) max_score
    FROM
       Exam 
    group by
        exam_id
), min_max_score_student AS

(
    SELECT
        distinct
        student_id
    FROm
        Exam A
    LEFT JOIN
        min_max_score B
    ON
        A.exam_id = B.exam_id
    WHERE
        (A.score = B.min_score OR A.score = B.max_score)   
    UNION 
    SELECT
        student_id
    FROM
        Student 
    WHERE
        student_id not in (SELECT distinct student_id from exam)
)

SELECT
    student_id,
    student_name
FROM
    Student
WHERE
    student_id not in (select student_id from min_max_score_student)