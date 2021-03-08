-- Solution 1
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Write your MySQL query statement below.
      WITH nT AS
      (          
        SELECT
            salary,
            dense_rank() over(order by salary desc) rn
        FROM
            Employee
      )
      
      SELECT
        DISTINCT
        CASE WHEN N<=counts THEN salary ELSE NULL END as salary
      FROM
        nT, (SELECT count(*) counts from nT)tt
      WHERE rn = N      
  );
END

-- Second Solutino
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
        DISTINCT
        SALARY
      FROM
        Employee
      ORDER BY SALARY DESC
      LIMIT 1 OFFSET N
  );
END