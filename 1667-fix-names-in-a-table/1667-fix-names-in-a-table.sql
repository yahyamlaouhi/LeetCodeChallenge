# Write your MySQL query statement below
Select user_id,CONCAT(upper(SUBSTR(name,1,1)),lower(SUBSTR(name,2))) name
FROM Users
Order by 1;


