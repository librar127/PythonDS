-- https://www.pgexercises.com/questions/aggregates/

-- 1. List each member's first booking after September 1st 2012
-- 2. Produce a list of member names, with each row containing the total member count
-- 3. Produce a numbered list of members
-- 4. Output the facility id that has the highest number of slots booked, again
-- 5. Rank members by (rounded) hours used
-- 6. Find the top three revenue generating facilities
-- 7. Classify facilities by value
-- 8. Calculate the payback time for each facility
-- 9. Calculate a rolling average of total revenue

-- 1. List each member's first booking after September 1st 2012
select surname, firstname, memid, starttime from 
(select m.surname, m.firstname, b.memid, b.starttime, to_char(b.starttime, 'YYYY-MM-DD')dd,
row_number() over (partition by m.surname, m.firstname, b.memid order by b.starttime) as rank
from cd.members m
join cd.bookings b
on m.memid = b.memid
WHERE to_char(b.starttime, 'YYYY-MM-DD') > '2012-08-31')nT where rank=1
order by memid;

-- OR 
select mems.surname, mems.firstname, mems.memid, min(bks.starttime) as starttime
	from cd.bookings bks
	inner join cd.members mems on
		mems.memid = bks.memid
	where starttime >= '2012-09-01'
	group by mems.surname, mems.firstname, mems.memid
order by mems.memid;

-- 2. Produce a list of member names, with each row containing the total member count
select count(*) over() as count, firstname, surname
from cd.members 
order by joindate;

-- 3. Produce a numbered list of members
select row_number() over(order by joindate) row_number,
firstname, surname
from cd.members;

-- 4. Output the facility id that has the highest number of slots booked, again
with nT as (
  select facid, sum(slots) as total
  ,rank() over(order by sum(slots) desc) rank
  from cd.bookings
  group by facid)
  
 select facid, total from nT where rank=1;