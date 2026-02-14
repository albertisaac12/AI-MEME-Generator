# SQL Commands Cheat Sheet

## Database Management
Create and select the working database.

```sql
-- List all databases
show databases;

-- Create a new database if it doesn't exist
create database if not exists tutorialdb;

-- Select the database to use
use tutorialdb;
```

## Table Creation
Create a table to store data.

```sql
-- List all tables in the current database
show tables;

-- Create a 'people' table with columns for id, name, age, and height
create table if not exists people (
    p_id integer unique primary key,
    p_name varchar(255),
    p_age integer,
    p_height float
);
```

## Inserting Data
Add new records to the table.

```sql
-- Insert into specific columns
insert into people (p_id, p_name) values (1, "Mike");

-- Insert into all columns
insert into people values (2, "John", 78, 180);

-- Insert multiple records at once
insert into people values 
    (3, "Anna", 28, 180),
    (4, "Bob", 38, 178),
    (5, "Kate", 48, 182),
    (6, "James", 55, 183),
    (7, "Samuel", 38, 181),
    (8, "Lisa", 28, 177);
```

## Querying Data
Retrieve data from the table.

```sql
-- Select all data
select * from people;

-- Select specific columns
select p_name, p_age from people;

-- Select with conditions (filter)
select p_name, p_age from people where p_age < 40 and p_age is not null;
```

## Updating and Deleting
Modify existing data.

```sql
-- Update specific fields for a record
update people set p_age = 30, p_height = 179 where p_id = 1;

-- Delete a specific record
delete from people where p_id = 6;

-- Disable safe update mode to allow deleting by non-key columns
set sql_safe_updates = 0;

-- Delete records based on a condition
delete from people where p_age > 50;
```

## Altering Table Structure
Change the table schema.

```sql
-- Insert a record to test
insert into people (p_id, p_name, p_height) values (10, "James", 178.23);

-- Change a column's data type
alter table people modify column p_height integer;

-- Verify changes
select * from people where p_id = 10;

-- Rename a column
alter table people rename column p_height to p_size;
alter table people rename column p_size to p_height;

-- Add a new column
alter table people add column p_weight float;

-- Remove a column
alter table people drop column p_weight;
```