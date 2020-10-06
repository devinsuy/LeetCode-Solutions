-- Write a SQL query to get the second highest salary from the Employee table.

SELECT MAX(e.salary) AS "SecondHighestSalary" FROM Employee e
WHERE e.salary < (SELECT MAX(e.salary) FROM Employee e)