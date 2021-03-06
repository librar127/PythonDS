-- Write your MySQL query statement below
SELECT
    DISTINCT 
    A.account_id
FROM
    LogInfo A
JOIN
    LogInfo B
ON
    A.account_id = B.account_id
AND
    A.ip_address != B.ip_address
AND
    B.login > A.login
AND
    B.login <= A.logout   
    