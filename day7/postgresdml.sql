

--- DML --> Data manipulation lang. 



-- insert 
    -- insert new data to the table 

    INSERT INTO  tablaname VALUES  (values for all columns in this table );
    --  id | name | salary | logintime | absent | gender | d_id 
 
    insert into employees values(1,'ahmed', 1000, now(), false, 'male', null);

    -- insert data in specific fields

    insert into employees (id , name, gender) values(2, 'ali','male');

    insert into depts(name) values ('php'), ('ai'), ('ds');



-- update

    -- update departments for current employees
    update tablename set colname=value  [where condition];

    update employees set d_id = 3;

    update employees set d_id=4 where id=1;

    update employees set salary=2000 , absent=false where id=2;

-- delete
    delete from tablaname [where condition];

    delete from employees;

    delete from employees where id > 1;


update employees set name='updated';

update employees set salary = 10000 where id%2=0 ;
update employees set salary = 50000 where id%2!=0 ;

-- create function 

-- -------- select 
---> select retrieve data from tables 

select fieldlist, *
from tablaname
[where condition] , 
[GROUP BY  column]  -- used with aggregation functions
[Having condition] --- used with group by to customize group by result
[order by colname]
[limit no]

;


select id , name from employees;

--- where condition
select id , name from employees where id > 3;
select * from employees where id%3=0;   -- expression 

-- select users == where names starts with a 

select * from employees where name like 'a%';


select * from employees where name like '%d';

---- select employees --> salary between 10000 and 40000 

SELECT * FROM employees WHERE ID between 3 AND 10;
-- select * from employees where salary between 10000 and 40000;


NOTE THIS : 
stpy123=# select * from employees where salary between 10000 and 40000;
-- ERROR:  operator does not exist: money >= integer
-- LINE 1: select * from employees where salary between 10000 and 40000...
--                                              ^
-- HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
-- stpy123=# select * from employees where salary between 10000 and 40000;

SOLUTION01:
select * from employees where salary between '10000' AND '40000';


select * from employees where salary between 10000::money AND 40000::MONEY;




--- cast money to int 
SELECT SALARY::numeric::int FROM employees ;

------------in operator 
SELECT * FROM employees WHERE ID in (3,10);


-- to apply commulative action on db records

--> Aggregation function ?

select count(*) from employees;


select min(salary) from employees;

select max(salary) from employees;

select sum(salary) from employees;

select avg(salary::numeric::int) from employees;

--- select number of employees 40000?
-- with aggregation function you can only select the column appears
-- in the GROUP BY  scope
select salary, count(salary) from employees GROUP BY  salary;

---- having 
select  count(salary), salary from employees
 GROUP BY  salary 
 having count(salary)> 1;

----------------------- order by 
 -- by defaut data in postgres tables are sorted ascending 
 --from the older updated record to the newers

select * from employees order by id ; --> sort asceding

select * from employees order by id desc;

--- limit

select  * from employees order by id desc limit 1;

-------------- get data from different tables ------------------
--- joins 

---> inner join 

select * 
from employees, depts
where employees.d_id = depts.id; 


---------------- DCL 


--> create user ? -
--> make sure that you logining with user postgres 

create user username with password yourpassword;

create user stpy123 with password 'iti';


-- to display users in the system 
\du 

-- to make user super user 

alter user stpy123 superuser;




































