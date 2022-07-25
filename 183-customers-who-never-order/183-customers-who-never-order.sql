# Write your MySQL query statement below
Select customers.name as Customers from Customers left join
Orders on orders.customerId=Customers.id where customerId is Null;