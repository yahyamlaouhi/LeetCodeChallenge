# Write your MySQL query statement below
SELECT Max(salary) as SecondHighestSalary
FROM employee where salary <> (select max(salary) from employee);
