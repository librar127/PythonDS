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

-- LegCount
SELECT SUM(CASE WHEN type = 'human' then 2 else 4 end) as summary_legs
FROM creatures
ORDER BY id;
