/* Write your SQL here. Terminate each statement with a semicolon. */
SELECT
    ID,
    A,
    B,
    OPERATION,
    C
FROM
    expressions
WHERE
    C = CASE WHEN OPERATION = '+' THEN A+B
                WHEN OPERATION = '-' THEN A-B
                WHEN OPERATION = '*' THEN A*B
                WHEN OPERATION = '/' THEN (A/B)
            END 
ORDER BY 
    ID;