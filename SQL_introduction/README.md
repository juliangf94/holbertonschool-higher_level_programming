# SQL - Introduction

## Description
This project marks the beginning of my journey into Relational Databases using **MySQL**. I practiced essential SQL commands (DDL and DML) to create databases, manage tables, and manipulate data. 

The tasks cover everything from basic server exploration to advanced data filtering and aggregation.

## Learning Objectives
* How to create a database and a table.
* How to insert, update, and delete records.
* How to filter data using `WHERE`, `ORDER BY`, and `GROUP BY`.
* How to use aggregate functions like `COUNT` and `AVG`.
* Understanding `NULL` values and how to filter them.

## Requirements
* **OS:** Ubuntu 22.04 LTS
* **MySQL Server:** version 8.0
* **Style:** All SQL keywords should be in uppercase (e.g., `SELECT`, `FROM`).
* All files must end with a new line.

## Project Structure

| Task | File | Description |
| :--- | :--- | :--- |
| 0 | `0-list_databases.sql` | Lists all databases on the MySQL server. |
| 1 | `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0`. |
| 2 | `2-remove_database.sql` | Deletes the database `hbtn_0c_0`. |
| 3 | `3-list_tables.sql` | Lists all tables in a specific database. |
| 4 | `4-first_table.sql` | Creates `first_table` with `id` and `name`. |
| 5 | `5-full_table.sql` | Prints the full description of `first_table`. |
| 6 | `6-list_values.sql` | Lists all rows of `first_table`. |
| 7 | `7-insert_value.sql` | Inserts a specific row into `first_table`. |
| 8 | `8-count_89.sql` | Counts records with `id = 89`. |
| 9 | `9-full_creation.sql` | Creates `second_table` and populates multiple rows. |
| 10 | `10-top_score.sql` | Lists records ordered by top scores. |
| 11 | `11-best_score.sql` | Lists records with a score >= 10. |
| 12 | `12-no_cheating.sql` | Updates Bob's score to 10. |
| 13 | `13-change_class.sql` | Removes records with a score <= 5. |
| 14 | `14-average.sql` | Computes the average score of all records. |
| 15 | `15-groups.sql` | Lists the number of records with the same score. |
| 16 | `16-no_link.sql` | Lists records with a name, ordered by score. |

## How to Run
To execute a script against your local MySQL server, use the following command:

```bash
cat <script_name.sql> | mysql -hlocalhost -uroot -p <database_name>
