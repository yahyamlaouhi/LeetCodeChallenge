# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete from Person
where Id in (select r.Id from  
             (select Id, row_number() over(partition by Email 
                                          order by Id
                                         ) as rk
             from Person) r
            where r.rk > 1
            );
