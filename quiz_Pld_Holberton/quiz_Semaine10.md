#   SQL & Databases
## Question 0 — What is a PRIMARY KEY?
**Score: ✅ 1.0**

- [x] A constraint that uniquely identifies each record in a table.
- [x] It should not be NULL.
- [ ] A value that refers to a record in another table.
- [ ] A function that establishes relationships between two tables.

---

## Question 1 — What is DML?
**Score: ✅ 1.0**

- [ ] It is the language to define the structures like schema, database, tables, constraints, etc.
- [x] It is the language used to manage and manipulate data in the database.
- [ ] It is the language that deals with controls, rights, and permissions in the database system.
- [ ] It is a derivate language from SQL.

---

## Question 2 — What is SQL?
**Score: ✅ 1.0**

- [x] It is a standard language for accessing and manipulating databases.
- [ ] It stands for Standard Query Language.
- [ ] It is a collection of rules and guidelines for how to work with databases.
- [ ] It is a universal language that every database uses.

---

## Question 3 — How do you add a new record in the table users?
**Score: ✅ 1.0**

- [ ] INSERT users (id, name, age) VALUES (2, "Betty", 30);
- [ ] INSERT INTO users (id, name) VALUES (2, "Betty", 30);
- [x] INSERT INTO users (id, name, age) VALUES (2, "Betty", 30);
- [ ] INSERT INTO users (id, name, age) VALUES (2, "Betty");

---

## Question 4 — MySQL privileges differ in contexts and levels of operation
**Score: ✅ 1.0**

- [x] True
- [ ] False

---

## Question 5 — What is DDL?
**Score: ✅ 1.0**

- [ ] It is a derivate language from SQL.
- [ ] It is the language that deals with controls, rights, and permissions in the database system.
- [ ] It is the language used to manage and manipulate data in the database.
- [x] It is the language to define the structures like schema, database, tables, constraints, etc.

---

## Question 6 — What is a DBMS?
**Score: ✅ 1.0**

- [x] It is a system software for creating and managing databases.
- [ ] It is a tool to automate database operations.
- [ ] It stands for Database Management Services.
- [ ] It is MySQL's open source code.

---

## Question 7 — How do you list all users in this table?
**Score: ✅ 1.0**

- [x] SELECT * FROM users;
- [ ] SELECT ALL users;
- [ ] FROM users SELECT *;
- [ ] From users SELECT ALL;

---

## Question 8 — Which best describes what is data?
**Score: ✅ 1.0**

- [x] Data is any sequence of one or more symbols, bits of information.
- [ ] Data are numeric values that can be displayed in a graph.
- [ ] Data are paragraphs of information.
- [ ] Data is information about a person or place.

---

## Question 9 — In MySQL, an account is defined in terms of a user name and the client host or hosts from which the user can connect
**Score: ❌ 0.0**

- [x] True
- [ ] False

> ⚠️ **Missed this one.** The statement is **True** — in MySQL, an account is indeed defined by a username AND the host from which the user connects (e.g. `'user'@'localhost'`), and can include a password.

---

## Question 10 — A subquery is a query that is inside another query
**Score: ✅ 1.0**

- [x] True
- [ ] False

---

## Question 11 — What is a JOIN?
**Score: ✅ 1.0**

- [x] It is a clause used to retrieve data from multiple tables.
- [ ] It is a clause used to retrieve data from multiple databases.
- [ ] It is a clause used to create a new table by joining data from multiple tables.
- [ ] It is a clause used to join multiple databases.

---

## Question 12 — How do you change the name of the users record with id = 89 to Holberton?
**Score: ✅ 1.0**

- [x] UPDATE users SET name = "Holberton" WHERE id = 89;
- [ ] CHANGE users SET name = "Holberton" WHERE id = 89;
- [ ] ALTER users SET name = "Holberton" WHERE id = 89;

---

## Question 13 — What is MySQL?
**Score: ✅ 1.0**

- [ ] A database
- [ ] A tool to create data
- [ ] A non relational DBMS
- [x] A relational database management system

---

## Question 14 — Which of the following are valid relationship types in MySQL?
**Score: ✅ 1.0**

- [x] one to one
- [x] one to many
- [x] many to many
- [ ] parent to child
- [ ] not null

---

## Question 15 — What is a database?
**Score: ✅ 1.0**

- [x] It is an organized collection of data, so that it can be easily accessed and managed.
- [ ] It is a software that processes information.
- [ ] It is a tool to store any type of information.
- [ ] It is an unstructured collection of data.

---

## Question 16 — How do you list all users records with age > 21?
**Score: ✅ 1.0**

- [ ] SELECT * FROM users IF age > 21;
- [ ] SELECT * FROM users WHERE age IS UP TO 21;
- [x] SELECT * FROM users WHERE age > 21;
- [ ] SELECT * FROM users WHILE age > 21;

---

## Question 17 — In MySQL, a function is a stored program that you can pass parameters into and then return a value
**Score: ✅ 1.0**

- [x] True
- [ ] False

---

## Question 18 — Which statements are true for SQL constraints?
**Score: ✅ 1.0**

- [x] SQL constraints are used to specify rules for data in a table.
- [x] Constraints can be specified when the table is created.
- [x] Constraints can be specified after the table is created.
- [x] Constraints are used to limit the type of data that can go into a table.
- [x] Constraints ensure the accuracy and reliability of the data in the table.
- [ ] An example of a constraint can be ORDER BY.

---

## Question 19 — What is DCL?
**Score: ✅ 1.0**

- [ ] It is a derivate language from SQL.
- [ ] It is the language to define the structures like schema, database, tables, constraints, etc.
- [x] It is the language that deals with controls, rights, and permissions in the database system.
- [ ] It is the language used to manage and manipulate data in the database.

---

## Question 20 — What is a relational database?
**Score: ✅ 1.0**

- [x] It is a type of database that stores and provides access to data points that are related to one another.
- [ ] It is a type of database that finds any relationship among the data you store in it.
- [ ] It is a type of database that doesn't require the use of SQL, also known as NoSQL.
- [ ] It is a type of database that works just like a married database.

---

## Question 21 — How do you delete the users record with id = 89?
**Score: ❌ 0.0**

- [ ] DELETE users WHERE id = 89;
- [x] DELETE FROM users WHERE id = 89;
- [ ] DELETE ALL users WHERE id == 89;
- [ ] DELETE FROM users WHERE id IS EQUAL TO 89;

> ⚠️ **Missed this one.** The correct answer is `DELETE FROM users WHERE id = 89;` — requires `FROM` keyword and uses `=` not `==`.

---

## Question 22 — Which is a correct example of how to create a database in MySQL?
**Score: ✅ 1.0**

- [x] CREATE DATABASE menagerie;
- [ ] ALTER DATABASE menagerie;
- [ ] creat database menagerie
- [ ] INSERT database menagerie;
