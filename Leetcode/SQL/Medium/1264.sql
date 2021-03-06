-- Write your MySQL query statement below

WITH nT AS
(    
    SELECT
        user1_id user_id
    FROM
        Friendship
    WHERE
        user2_id = 1
    UNION
    SELECT
        user2_id user_id
    FROM
        Friendship
    WHERE
        user1_id = 1
)

SELECT
  DISTINCT
  page_id recommended_page
FROM
    Likes A
JOIN
    nT B
ON
    A.user_id = B.user_id
AND
   page_id not in (SELECT DISTINCT page_id from Likes WHERE user_id =1)