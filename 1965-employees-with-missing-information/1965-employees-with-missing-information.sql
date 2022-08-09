/* Write your PL/SQL query statement below */
select e.employee_id from Employees e LEFT JOIN Salaries s on s.employee_id = e.employee_id
union
select s.employee_id from Employees e Right JOIN Salaries s on s.employee_id = e.employee_id
MINUS
select s.employee_id from Employees e inner JOIN Salaries s on s.employee_id = e.employee_id;
