# Write your MySQL query statement below
with exam_min_max as
(
    select 
        exam_id, 
        max(score) max_score, 
        min(score) min_score
    from 
        Exam
    group by
        exam_id
),

student_with_min_max AS 
(
    select
        distinct
        student_id
    from 
        Exam A
    JOIN
        exam_min_max B
    ON
        A.exam_id = B.exam_id
    AND
        (A.score = B.max_score or A.score = B.min_score)
)

SELECT
    distinct
    A.student_id,
    B.student_name
FROm
    Exam A
JOIN
    Student B
ON
    A.student_id = B.student_id
WHERE
    A.student_id not in (select student_id from student_with_min_max)
ORDER BY
    A.student_id