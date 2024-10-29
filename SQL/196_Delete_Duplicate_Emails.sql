
delete from Person where Id not in(select MIN(Id) from Person group by email)