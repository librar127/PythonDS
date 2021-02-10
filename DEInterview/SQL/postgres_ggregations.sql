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

 -- 5. Rank members by (rounded) hours used
 select m.firstname, m.surname, round((sum(b.slots)+10)/20, 0)*10  as hours,
rank() over(order by round((sum(b.slots)+10)/20, 0)*10 desc) rank
from cd.members m
join cd.bookings b
on m.memid = b.memid
group by m.firstname, m.surname
order by rank, m.surname, m.firstname


-- 6. Find the top three revenue generating facilities
select name, rank from (
	select facs.name as name, rank() over (order by sum(case
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) desc) as rank
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as subq
	where rank <= 3
order by rank;  

with nT as (
select f.name, ntile(3) over (order by sum(case
				when memid = 0 then slots * f.guestcost
				else slots * membercost
			end) desc) as class
from cd.bookings b
inner join cd.facilities f
on b.facid = f.facid			
group by f.name)


-- 7. Classify facilities by value
select name, case when class=1 then 'high' when class=2 then 'average' else 'low' end as revenue
from nT order by class, name


