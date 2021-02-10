SELECT  
    FIRST_NAME,
    SECOND_NAME,
    ATTRIBUTE
FROM
    users
WHERE
    ATTRIBUTE LIKE BINARY CONCAT('_%', CONCAT('\%', FIRST_NAME, '\_', SECOND_NAME,'\%'), '%')
ORDER BY
    ATTRIBUTE;     