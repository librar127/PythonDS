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


-- Combination Lock - Copy
SET @comb = 1;
SELECT max(@comb:= @comb*length(characters)) as combinations
FROM discs;  

-- Find in SET
SELECT name
FROM people_interests
WHERE interests & (find_in_set('reading', interests) > 0) AND interests & (find_in_set('drawing', interests) > 0)
ORDER BY name;

-- Personal Hobbies
SELECT name
FROM people_hobbies
WHERE hobbies & (find_in_set('sports', hobbies) > 0) AND hobbies & (find_in_set('reading', hobbies) > 0)
ORDER BY name;

-- Books Catalog
SELECT
    DISTINCT SUBSTRING_INDEX(EXTRACTVALUE(xml_doc, "//author"), " ", 2)author
FROM    
    catalogs
ORDER BY author;