#   SQL - Introduction
##  **What's a database**
A **database** is an organized collection of structured data stored and accessed electronically.  
It allows data to be easily stored, retrieved, managed, and updated.  
Databases are managed by a Database Management System (DBMS).

---

##  **What's a relational database**
A relational database is a type of database that organizes data into tables (rows and columns) that can be related to one another through keys.  
Relationships between tables allow for efficient querying and data integrity.  
Examples: MySQL, PostgreSQL, SQLite, Oracle.

---

##  **What does SQL stand for**
SQL stands for **Structured Query Language**.  
It is the standard language used to communicate with relational databases — allowing you to `create`, `read`, `update`, and `delete` data.

---

##  **What's MySQL**
MySQL is an open-source Relational Database Management System (RDBMS) that uses SQL.  
It is one of the most widely used databases in the world, commonly used in web development (e.g., LAMP stack).  
It is owned by Oracle Corporation.

---

##  **How to create a database in MySQL**
```sql
CREATE DATABASE my_database;
```
To use it:
```sql
USE my_database;
```
To create it only if it doesn't already exist:
```sql
CREATE DATABASE IF NOT EXISTS my_database;
```

---

##  **What does DDL and DML stand for**
| Acronym | Full Name | Description |
| :... | :...| :... |
| DDL | Data Definition | **LanguageCommands** that define or modify the structure of the database (tables, schemas). Examples: `CREATE`, `ALTER`, `DROP` |
| DML | Data Manipulation | **LanguageCommands** that manipulate the data inside tables. Examples: `SELECT`, `INSERT`, `UPDATE`, `DELETE` |

---

##  **How to CREATE or ALTER a table**
### **CREATE a table:**
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(150) UNIQUE
);
```
### **ALTER a table:**
```sql
-- Add a column
ALTER TABLE students ADD COLUMN grade CHAR(2);

-- Modify a column
ALTER TABLE students MODIFY COLUMN age TINYINT;

-- Drop a column
ALTER TABLE students DROP COLUMN grade;

-- Rename a column
ALTER TABLE students RENAME COLUMN email TO contact_email;
```

---

##  **How to SELECT data from a table**
```sql
-- Select all columns
SELECT * FROM students;

-- Select specific columns
SELECT name, age FROM students;

-- With a condition
SELECT * FROM students WHERE age > 18;

-- Order results
SELECT * FROM students ORDER BY name ASC;

-- Limit results
SELECT * FROM students LIMIT 10;

-- With alias
SELECT name AS student_name FROM students;
```

---

##  **How to INSERT, UPDATE or DELETE data**
### **INSERT:**
```sql
INSERT INTO students (name, age, email)
VALUES ('John Doe', 22, 'john@example.com');
```
### **UPDATE:**
```sql
UPDATE students
SET age = 23
WHERE name = 'John Doe';
```
### D**ELETE:**
```sql
DELETE FROM students
WHERE name = 'John Doe';
```
⚠️ Always use WHERE with UPDATE and DELETE to avoid modifying/deleting all rows.

---

##  **What are subqueries**
A subquery is a query nested inside another query. It can be used in SELECT, FROM, WHERE, or HAVING clauses.
```sql
-- Subquery in WHERE
SELECT name FROM students
WHERE id IN (
    SELECT student_id FROM enrollments WHERE course = 'Math'
);

-- Subquery in SELECT
SELECT name, (SELECT MAX(grade) FROM grades WHERE grades.student_id = students.id) AS top_grade
FROM students;

-- Subquery in FROM (derived table)
SELECT avg_age FROM (
    SELECT AVG(age) AS avg_age FROM students
) AS age_summary;
```

---

##  **How to use MySQL functions**
### **String functions:**
```sql
SELECT UPPER(name) FROM students;          -- Uppercase
SELECT LOWER(name) FROM students;          -- Lowercase
SELECT LENGTH(name) FROM students;         -- String length
SELECT CONCAT(name, ' - ', email) FROM students; -- Concatenate
SELECT SUBSTRING(name, 1, 3) FROM students; -- Substring
```
### **Numeric functions:**
```sql
SELECT ROUND(4.567, 2);   -- 4.57
SELECT FLOOR(4.9);        -- 4
SELECT CEIL(4.1);         -- 5
SELECT ABS(-10);          -- 10
```
### **Date functions:**
```sql
SELECT NOW();             -- Current datetime
SELECT CURDATE();         -- Current date
SELECT YEAR(NOW());       -- Current year
SELECT DATEDIFF('2025-12-31', '2025-01-01'); -- Days between dates
```
### **Aggregate functions:**
```sql
SELECT COUNT(*) FROM students;            -- Total rows
SELECT AVG(age) FROM students;            -- Average
SELECT SUM(age) FROM students;            -- Sum
SELECT MAX(age) FROM students;            -- Maximum
SELECT MIN(age) FROM students;            -- Minimum
```
### **Control flow:**
```sql
SELECT name,
    IF(age >= 18, 'Adult', 'Minor') AS status
FROM students;

SELECT name,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age BETWEEN 18 AND 25 THEN 'Young Adult'
        ELSE 'Adult'
    END AS age_group
FROM students;
```

---
---

#   Quiz
# MySQL Quiz — Answers

---

## Question #0 — What does SQL stand for?

- [ ] Sequences of Query Logic
- [x] Structured Query Language
- [ ] Solid Query Language
- [ ] Structured Question Language

---

## Question #1 — What is a relational database?

- [x] a database
- [x] a collection of data
- [ ] married databases
- [x] data are organized by tables, records and columns
- [ ] data are organized by tables and indexes
- [ ] a table containing multiple object representation
- [x] a table containing only one object representation

---

## Question #2 — What does DDL stand for?

- [x] Data Definition Language
- [ ] Database Definition Language
- [ ] Data Document Language
- [ ] Document Data Language

---

## Question #3 — What does DML stand for?

- [ ] Database Manipulation Language
- [ ] Document Manipulation Language
- [x] Data Manipulation Language
- [ ] Document Model Language

---

## Question #4 — How do you list all users in this table?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

- [ ] DELETE * FROM users;
- [x] SELECT * FROM users;
- [ ] SELECT ALL users;

---

## Question #5 — How do you add a new record in the table users?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

- [ ] INSERT users (id, name, age) VALUES (2, "Betty", 30);
- [ ] INSERT INTO users (id, name) VALUES (2, "Betty", 30);
- [x] INSERT INTO users (id, name, age) VALUES (2, "Betty", 30);
- [ ] INSERT INTO users (id, name, age) VALUES (2, "Betty");

---

## Question #6 — How do you delete the users record with id = 89?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

- [ ] DELETE users WHERE id = 89;
- [x] DELETE FROM users WHERE id = 89;
- [ ] DELETE FROM users;
- [ ] DELETE FROM users WHERE id IS EQUAL TO 89;

---

## Question #7 — How do you change the name of the users record with id = 89 to Holberton?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

- [x] UPDATE users SET name = "Holberton" WHERE id = 89;
- [ ] CHANGE users SET name = "Holberton" WHERE id = 89;
- [ ] UPDATE users SET name = "Holberton";

---

## Question #8 — How do you list all users records with age > 21?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

- [ ] SELECT * FROM users WHERE age < 21;
- [ ] SELECT * FROM users WHERE age IS UP TO 21;
- [x] SELECT * FROM users WHERE age > 21;
- [ ] SELECT * FROM users WHERE age BETWEEN 21 AND 89;


---
---

#   Exercises
##  0. List databases
Write a script that lists all databases of your MySQL server.

`0-list_databases.sql`
```SQL
-- Script that lists all databases of your MySQL server
SHOW DATABASES;
```
**Logic**

**Try**
```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
With the `.my.cnf` file
```bash
cat 0-list_databases.sql | mysql
```
**Output**
```bash
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

---

##  1. Create a database
Write a script that creates the database hbtn_0c_0 in your MySQL server.
-   If the database hbtn_0c_0 already exists, your script should not fail
-   You are not allowed to use the SELECT or SHOW statements
``
```
```
`1-create_database_if_missing.sql`
```SQL
-- Script that creates the hbtn_0c_0 database in the MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0c_0

```
**Logic**

**Try**
Check if it's there (using your task 0 script):
```bash
cat 0-list_databases.sql | sudo mysql -hlocalhost -uroot -p
```
With the `.my.cnf` file
```bash
cat 0-list_databases.sql | mysql
```
**Output**
```bash
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```
Run the script:
```bash
cat 1-create_database_if_missing.sql | sudo mysql -hlocalhost -uroot -p
```
```bash
cat 1-create_database_if_missing.sql | mysql
```
**Output**
```bash
Enter password: 
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
```

---

##  2. Delete a database
Write a script that deletes the database hbtn_0c_0 in your MySQL server.
-   If the database hbtn_0c_0 doesn't exist, your script should not fail
-   You are not allowed to use the SELECT or SHOW statements

`2-remove_database.sql`
```sql
-- Script that deletes the database hbtn_0c_0 in your MySQL server
-- The command DROP DATABASE IF EXISTS prevents errors if the database is already gone

DROP DATABASE IF EXISTS hbtn_0c_0;
```
**Logic**
- **DROP DATABASE**: This is a DDL (Data Definition Language) command. It doesn't just empty the database; it removes the entire structure and all data associated with it from the file system.

- **IF EXISTS**: This is the "safe" way to delete. If you run DROP DATABASE hbtn_0c_0 and the database isn't there, MySQL will throw an error. Adding IF EXISTS turns that error into a simple warning, allowing the script to exit successfully.

- **Permissions**: Since you are working in your local environment, you need sudo or the root user to execute DDL commands like this.
**Try**
1. **Check that the database exists:**
```bash
cat 0-list_databases.sql | sudo mysql -hlocalhost -uroot -p
```

```bash
cat 1-create_database_if_missing.sql | mysql
```
**Output**
```bash
[sudo] password for juliangf94: 
Enter password: 
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
```
2. **Run the deletion script:**
```bash
cat 2-remove_database.sql | sudo mysql -hlocalhost -uroot -p
```
- with the `.my.cnf` file
```bash
cat 2-remove_database.sql | mysql
```
3. **Check the list again to confirm it's gone:**
```bash
cat 0-list_databases.sql | sudo mysql -hlocalhost -uroot -p
```
**Output**
```bas
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

---

##  3. List tables
Write a script that lists all the tables of a database in your MySQL server.
-   The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)
``
```bash
```
`3-list_tables.sql`
```sql
-- Script that lists all tables of a database in your MySQL server
-- The database name will be passed as an argument of the mysql command

SHOW TABLES;

```
**Logic**
- `SHOW TABLES`: This command lists all tables within the currently selected database.

- Context: When you run the command `cat 3-list_tables.sql | mysql ... hbtn_0c_0, the hbtn_0c_0` at the end tells MySQL to "USE" that database before running the script.

- DDL vs DML: This is technically a database administration command, used to explore the schema structure.
**Try**
```bash
cat 3-list_tables.sql | sudo mysql -hlocalhost -uroot -p mysql
```
- **with the `.my.cnf` file**
```bash
cat 3-list_tables.sql | mysql mysql
```
**Output**
```bash
Enter password: 
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
replication_group_configuration_version
replication_group_member_actions
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
```

---

##  4. First table
Write a script that creates a table called `first_table` in the current database in your MySQL server.
-   first_table description:
  +   id INT
  +   name VARCHAR(256)
  +   The database name will be passed as an argument of the mysql command
  +   If the table first_table already exists, your script should not fail
  +   You are not allowed to use the SELECT or SHOW statements
``
```
```
`4-first_table.sql`
```sql
-- Script that creates a table called first_table in the current database
-- first_table description: id INT, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

```
**Logic**
- `CREATE TABLE`: This **DDL** command creates a new table structure.

- `IF NOT EXISTS`: Just like with the database creation, this prevents your script from crashing if you run it twice.

- `id INT`: Defines a column named `id` that stores integers (whole numbers).

- `name VARCHAR(256)`: Defines a column named `name` that stores a variable-length string of up to 256 characters.

- `()`: The column definitions must be wrapped in parentheses and separated by commas.
**Try**
1. **Ensure the database exists first (from Task 1):**
```bash
cat 1-create_database_if_missing.sql | sudo mysql -hlocalhost -uroot -p
```
2. **Run the script to create the table:**
```bash
cat 4-first_table.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
```
```bash
cat 4-first_table.sql | mysql hbtn_0c_0
```
3. **Verify the table was created (using your Task 3 script):**
```bash
cat 3-list_tables.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
```
**Output**
```bash
Enter password: 
Tables_in_hbtn_0c_0
first_table
```
4. **Check the structure of the table (Optional but helpful):**
```bash
echo "DESCRIBE first_table;" | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
```
**Output**
```bash

```
---

##  5. Full description
Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
-   The database name will be passed as an argument of the mysql command
-   You are not allowed to use the DESCRIBE or EXPLAIN statements

`5-full_table.sql`
```sql
-- Script that prints the full description of the table first_table
-- Using SHOW CREATE TABLE instead of DESCRIBE as required

SHOW CREATE TABLE first_table;

```
**Logic**
- `SHOW CREATE TABLE`: This is a powerful command that returns the exact "recipe" of the table. It includes the column names, data types, the storage engine (like `InnoDB`), and the character set.

- Why not `DESCRIBE`?: `DESCRIBE` only gives you a simplified summary (columns, types, nullability). The requirements specifically forbid it to ensure you know how to access the deeper metadata of the database.

- **Database Argument**: You don't need to specify the database inside the script (like `USE hbtn_0c_0;`) because Holberton's requirement states the database name will be passed in the `mysql` command itself.
**Try**
```bash
cat 5-full_table.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$ 
```

---

##  6. List all in table
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
-   All fields should be printed
-   The database name will be passed as an argument of the mysql command

`6-list_values.sql`
```sql
-- Script that lists all rows of the table first_table
-- All fields (id and name) should be printed

SELECT * FROM first_table;

```
**Logic**
- `SELECT`: The primary DML (Data Manipulation Language) command used to query and fetch data from a database.

- `*`: Instructs MySQL to return every column defined in the table schema (in this case, both `id` and `name`).

- FROM `first_table`: Specifies the source table for the query.

- Database Context: Since the database name `hbtn_0c_0` is passed as an argument in the command line, you don't need a `USE` statement inside the script.
**Try**
```bash
cat 6-list_values.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
```

---

##  7. First add
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
- New row:
- id = 89
- name = Best School
- The database name will be passed as an argument of the mysql command
`7-insert_value.sql`
```sql
-- Script that inserts a new row in the table first_table (database hbtn_0c_0)
-- New row: id = 89, name = Best School

INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```
**Try**
```bash
cat 7-insert_value.sql | mysql hbtn_0c_0
```
**Logic**
- `INSERT INTO`: The standard DML command used to add new records to a table.
- `(id, name)`: Explicitly listing the columns is a best practice. It ensures that the values are placed in the correct fields regardless of the table's internal column order.
- `VALUES (89, 'Best School')`:
  + 89: An integer, so it doesn't need quotes.
  + 'Best School': A string, so it must be enclosed in single quotes.
- Database Context: Again, no `USE` statement is needed inside the script because you'll provide the database name in the command line.
**Output**
```bash
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id    name
89    Best School
89    Best School
89    Best School
guillaume@ubuntu:~/$ 
```

---

##  8. Count 89
Write a script that displays the number of records with `id = 89` in the table first_table of the database `hbtn_0c_0` in your MySQL server.
-  The database name will be passed as an argument of the `mysql` command
`8-count_89.sql`
```sql
-- Script that displays the number of records with id = 89 in the table first_table
-- The COUNT function aggregates the total number of matching rows

SELECT COUNT(*) FROM first_table WHERE id = 89;

```
**Logic**
- `SELECT COUNT(*)`: This counts all rows that satisfy the condition. You could also use COUNT(id), but COUNT(*) is the standard way to count records.

- `WHERE id = 89`: This is the filter. Without this clause, the script would return the total number of all rows in the table.

- **Database Context**: As with the previous tasks, do not include a USE statement; the database hbtn_0c_0 is provided as a command-line argument.
**Try**
```bash
cat 8-count_89.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
```

---

##  9. Full creation
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
- `second_table` description:
  + `id` INT
  + `name` VARCHAR(256)
  + `score` INT
- The database name will be passed as an argument to the `mysql` command
- If the table `second_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` and `SHOW` statements
- Your script should create these records:
  + `id` = 1, `name` = "John", `score` = 10
  + `id` = 2, `name` = "Alex", `score` = 3
  + `id` = 3, `name` = "Bob", `score` = 14
  + `id` = 4, `name` = "George", `score` = 8

`9-full_creation.sql`
```sql
-- Script that creates a table second_table and adds multiple rows
-- Table structure: id INT, name VARCHAR(256), score INT

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserting the required records into second_table
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);

```
**Logic**
- `IF NOT EXISTS`: This is a critical guardrail. It prevents the script from crashing if you run it more than once. Since the requirements say "your script should not fail," this is mandatory.

- `VARCHAR(256)`: This defines a variable-length string that can hold up to 256 characters.

- **Multiple Values**: By using commas between the `()` sets after the `VALUES` keyword, you tell MySQL to perform all four insertions in a single transaction. This is a common industry practice to improve performance.

- No `SELECT/SHOW`: The script strictly sticks to creating and inserting, as per your instructions.
**Try**
```bash
cat 9-full_creation.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
```

---

##  10. List by best
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

`10-top_score.sql`
```sql
-- Script that lists all records of the table second_table
-- Display order: score, name
-- Sorting: ordered by score (top first / descending)

SELECT score, name FROM second_table ORDER BY score DESC;

```
**Logic**
- `SELECT score, name`: The requirements specify the order. By listing `score` first, the output columns will be arranged as `score` followed by `name`.
- `ORDER BY score`: This tells MySQL which column to use as the sorting key.
- `DESC`: Short for Descending. Since the task asks for "top first" (highest to lowest), we must use `DESC`. By default, SQL sorts in ascending order (`ASC`), which would put the lowest score first.
- **Database Context**: The database name `hbtn_0c_0` will be passed via the command line, so no `USE` statement is required.
**Try**
```bash
cat 10-top_score.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    name
14    Bob
10    John
8    George
3    Alex
guillaume@ubuntu:~/$ 
```

---

##  11. Select the best
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the mysql command

`11-best_score.sql`
```sql
-- Script that lists all records with a score >= 10 in second_table
-- Records are ordered by score (top first)

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

```
**Logic**
- `WHERE score >= 10`: This is the filtering condition. It tells MySQL to ignore any rows where the score is less than 10 (like Alex and George from your previous task).

- `score, name`: Keeping the specific column order requested by Holberton.

- `ORDER BY score DESC`: Ensuring the highest score (Bob with 14) appears at the top of the list.

- **Comparison Operator (`>=`)**: This includes rows where the score is exactly 10 and anything greater.
**Try**
```bash
cat 11-best_score.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    name
14    Bob
10    John
guillaume@ubuntu:~/$ 
```

---

##  12. Cheating is bad
Write a script that updates the score of `Bob` to `10` in the table `second_table`.
- You are not allowed to use Bob's id value, only the name field
- The database name will be passed as an argument of the mysql command

`12-no_cheating.sql`
```sql
-- Script that updates the score of Bob to 10 in the table second_table
-- Using only the name field to identify the record

UPDATE second_table SET score = 10 WHERE name = 'Bob';

```
**Logic**
- `UPDATE second_table`: Specifies which table contains the data you want to change.

- `SET score = 10`: This is the action. It tells MySQL to overwrite the current value in the score column with the new value, `10`.

- `WHERE name = 'Bob'`: This is the most important part. Without a `WHERE` clause, SQL would update the score to 10 for everyone in the table! This filter ensures only Bob is affected.

- **No ID allowed**: The requirements specifically forbid using `WHERE id = 3`. Using the `name` column follows the task's constraints perfectly.

**Try**
```bash
cat 12-no_cheating.sql | mysql hbtn_0c_0
```
```bash
cat 10-top_score.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    name
10    John
10    Bob
8    George
3    Alex
guillaume@ubuntu:~/$ 
```

---

##  13. Score too low
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- The database name will be passed as an argument of the mysql command
`13-change_class.sql`
```sql
-- Script that removes all records with a score <= 5 in the table second_table
-- Records where score is less than or equal to 5 will be deleted

DELETE FROM second_table WHERE score <= 5;

```
**Logic**
- `DELETE FROM second_table`: This identifies the table where the removal will occur.
- `WHERE score <= 5`: This is the critical filter.
  + **Crucial Note**: If you omit the `WHERE` clause, MySQL will delete all rows in the table.
  + This condition targets anyone with a score of 5, 4, 3, 2, 1, or 0. In your current data, this specifically targets Alex (who has a score of 3).
- **Permanent Action**: Unlike `SELECT`, a `DELETE` command cannot be "undone" easily. In a professional environment, always double-check your `WHERE` clause!
**Try**
```bash
cat 13-change_class.sql | mysql hbtn_0c_0
```
```bash
cat 10-top_score.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    name
10    John
10    Bob
8    George
guillaume@ubuntu:~/$ 
```

---

##  14. Average
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command

`14-average.sql`
```sql
-- Script that computes the score average of all records in the table second_table
-- The result column is renamed to 'average' using an alias

SELECT AVG(score) AS average FROM second_table;

```
**Logic**
- `AVG(score)`: This is a built-in SQL function that sums up all values in the score column and divides that sum by the total number of rows.
- `AS average`: This is called an Alias. By default, MySQL would name the output column `AVG(score)`. The requirements specifically ask for the column to be named `average`.
- **One Row Output**: Aggregate functions like `AVG`, `SUM`, or `MIN/MAX` collapse the entire table's data into a single result row.
- **Database Context**: As before, the database is handled by the command-line argument, so no `USE` statement is needed.
**Try**
```bash
cat 14-average.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
```

---

##  15. Number by score
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result should display:
  + the `score`
  + the number of records for this score with the label `number`
  + The list should be sorted by the number of records (descending)
  + The database name will be passed as an argument to the `mysql` command

`15-groups.sql`
```sql
-- Script that lists the number of records with the same score in second_table
-- Results display the score and the count labeled as 'number'
-- Sorted by the count of records in descending order

SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;

```
**Logic**
- `SELECT score`: Le dice a MySQL: "De cada grupo que encontraste, muéstrame qué valor tienen en la columna score".
  + Ya que se agrupa por `score`, solo se ve un "10" (que representa a John y Bob) y un "8" (que representa a George).
- `COUNT(*) AS number`: Within each group, this counts how many rows exist. We use the alias `AS number` as required by the task.
- `GROUP BY score`: This is the magic part. It tells MySQL to "stack" all rows that have the same value in the `score` column. Instead of seeing three separate rows for John, Bob, and George, you see groups based on their scores (the "10" group and the "8" group).
- `ORDER BY number DESC`: This sorts the final summary so that the score shared by the most people (the highest "number") appears at the top.
- **Logic**: In your current table, John and Bob both have `10`, so the "10" group will show a count of `2`. George is the only one with `8`, so that group shows `1`.

**Try**
```bash
cat 15-groups.sql | mysql hbtn_0c_0
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    number
10    2
8    1
guillaume@ubuntu:~/$ 
```

---

##  16. Say my name
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Don't list rows where the name column does not contain a value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the mysql command
In this example, new data have been added to the table second_table.

`16-no_link.sql`
```sql

```
**Logic**
- WHERE name IS NOT NULL: This is the standard way to check if a field has a value. Using name != NULL will not work in SQL because NULL cannot be compared using standard operators.

- AND name <> '': This is a "safety net." In many environments, a name might not be NULL, but it could be an empty string (just ""). Adding <> (which means "not equal to") ensures those are filtered out too.

- ORDER BY score DESC: Just like in your previous tasks, we want the highest scores at the very top.

- **Column Order**: We select score first, then name, exactly as the output example shows.
**Try**
```bash
mysql -e "INSERT INTO second_table (id, score) VALUES (5, 20);" hbtn_0c_0
```
```bash
cat 16-no_link.sql | mysql hbtn_0c_0
```

**Output**
```bash
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score    name
18    Aria
12    Aria
10    John
10    Bob
guillaume@ubuntu:~/$ 
```


---

```bash
cat 0-list_databases.sql | mysql
cat 1-create_database_if_missing.sql | mysql
cat 2-remove_database.sql | mysql
cat 3-list_tables.sql | mysql mysql
cat 4-first_table.sql | mysql hbtn_0c_0
cat 5-full_table.sql | mysql hbtn_0c_0
cat 6-list_values.sql | mysql hbtn_0c_0
cat 7-insert_value.sql | mysql hbtn_0c_0
cat 8-count_89.sql | mysql hbtn_0c_0
cat 9-full_creation.sql | mysql hbtn_0c_0
cat 10-top_score.sql | mysql hbtn_0c_0
cat 11-best_score.sql | mysql hbtn_0c_0
cat 12-no_cheating.sql | mysql hbtn_0c_0
cat 13-change_class.sql | mysql hbtn_0c_0
cat 14-average.sql | mysql hbtn_0c_0
cat 15-groups.sql | mysql hbtn_0c_0
cat 16-no_link.sql | mysql hbtn_0c_0

```
