# Write your MySQL query statement below

SELECT
    P.FirstName, 
    P.LastName, 
    A.City, 
    A.State
FROM
    PERSON P
LEFT JOIN
    ADDRESS A
ON
    P.PersonId = A.PersonId
