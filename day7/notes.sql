
-- the comment in sql file starts with -- 
-- to list all available dataabases --> postgres, template01 , template
\l 

-- to check currect connection info 
\conninfo 

-- to connect to specific data-->

\c databasename

-- to list all tables / relations in the database 
\d 
\dt --> list all tables in this database 

\du --> list all database users 

\dT  --> to list all types 

\d tablename --> to display table architecture ? 
----------------------------------------------------------------
-- to create new database  (queries )
-- DDL operation

create database databasename ; 

-- semicolon at the end of the query is mandatory 
--> when create new database 0--> make a copy from the database template01

-----

create database databasename template templatename; --> default template 


-- drop database 

drop database databasename;

--------------------------------------Create & drop type ------------------

create type emp_geneder as enum ('male', 'female');

drop type typename; 


------------------------------------CREATE Table ----------------------------------

-- table 

create table employees(id int primary key ,name varchar(40), salary money, 
logintime timestamp, absent boolean, gender emp_geneder);

-- once you create new table  (directly from the data --> using query)--> all columns in the table by 
-- defaults accept null, unless you say something else. ===> via constraints  

---< in frameworks that uses ORM --> tables columns created via migration files -->  by default not null 


create table departments(id serial primary key, name varchar(20));




--- drop table 
drop table tablename;


---------------------------- Alter  (modify table architecture )---------------------------
-- rename table
ALTER TABLE table_name RENAME TO new_name;

alter table departments rename to depts;

-- add column to the table 
ALTER TABLE table_name ADD column data_type;

alter table employees add column dept_id int;

-- drop column from the table
ALTER TABLE table_name DROP column_name;

alter table employees drop dropped; 

-- change datatype of table 
ALTER TABLE table_name ALTER column SET DATA TYPE data_type;

alter table employees alter id set data type bigint;
-- rename column
ALTER TABLE table_name RENAME COLUMN column TO new_column;
alter table employees rename  column dept_id to d_id;

-- add constraint to the table 
alter table table_name add constraint user_defined_constraint_name constraint_type ---;
ALTER TABLE table_name
ADD CONSTRAINT fk_name FOREIGN KEY (col1)
REFERENCES foreign_table (foreign_field)
ON DELETE CASCADE;

alter table employees 
add constraint employees_dept_fk 
FOREIGN KEY(d_id)
REFERENCES depts(id)
on DELETE CASCADE
on update set null; 

-- drop constraint 
alter table employees 
drop constraint employees_dept_fk; 



alter table tablaname  add constraint not_null_emp_name not null colname;


alter table depts alter column name set not null;



------------------------ DML 
-----------------------------------INSERT----------------------------------