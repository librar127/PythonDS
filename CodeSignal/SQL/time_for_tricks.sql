-- Website Hacking
SELECT id,login,name
FROM users
WHERE type='user'
OR type !='user'
ORDER BY id

-- NullIntern
SELECT count(*) number_of_nulls FROM departments
WHERE DESCRIPTION is NULL
OR UPPER(trim(DESCRIPTION)) = 'NULL'
OR trim(DESCRIPTION) = '-'
OR UPPER(trim(DESCRIPTION)) = 'NIL';