-- Write your MySQL query statement below

SELECT
    A.follower,
    COUNT(DISTINCT B.follower) num
FROM
    follow A
JOIN
    follow B
ON
    A.follower = B.followee
GROUP BY
    A.follower