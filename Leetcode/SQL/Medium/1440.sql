--  Write your T-SQL query statement below 
WITH nT as
(
    SELECT
        left_operand,
        operator,
        right_operand,
        B.value lvalue,
        C.value rvalue
    FROM
        Expressions A
    JOIN
        Variables B
    ON
        A.left_operand = B.name
    JOIN
        Variables C
    ON
        A.right_operand = C.name
)

SELECT    
    left_operand,
    operator,
    right_operand,
    CASE
    WHEN operator = '>' AND lvalue > rvalue THEN 'true'
    WHEN operator = '<' AND lvalue < rvalue THEN 'true'
    WHEN operator = '=' AND lvalue = rvalue THEN 'true'
    ELSE "false" END as value        
FROM
    nT