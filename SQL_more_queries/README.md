# 🗄️ SQL - More Queries

## 📝 Project Overview
This project focuses on advanced SQL querying techniques using **MySQL**. Throughout these tasks, I explored complex database relationships, including **One-to-Many** and **Many-to-Many** associations, as well as the implementation of constraints, joins, and subqueries.

The project utilizes the `hbtn_0d_tvshows` database, which simulates a TV show management system with titles, genres, and their respective links.

## 🚀 Key Learning Objectives
- How to create and manage users and privileges in MySQL.
- Difference between `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN`.
- How to handle **Many-to-Many** relationships using junction tables.
- Using `GROUP BY` and aggregate functions like `COUNT()`.
- Managing `NULL` values in joined result sets.

## 📂 Database Structure
The project mainly works with three tables:
1. **`tv_shows`**: Contains the title and ID of each show.
2. **`tv_genres`**: Contains the names of different genres.
3. **`tv_show_genres`**: A junction table linking shows to their genres (Many-to-Many).



## 🛠️ Requirements
- All files are executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**.
- Scripts are designed to be run as: 
  `cat <file.sql> | mysql -hlocalhost -uroot -p <database_name>`

## 📋 Task Summary

| Task | File | Description |
| :--- | :--- | :--- |
| **10** | `10-genre_id_by_show.sql` | Lists all shows that have at least one genre linked. |
| **11** | `11-genre_id_all_shows.sql` | Lists all shows, displaying `NULL` for those without a genre. |
| **12** | `12-no_genre.sql` | Lists only shows without a genre linked. |
| **13** | `13-count_shows_by_genre.sql` | Counts the number of shows linked to each genre. |
| **14** | `14-my_genres.sql` | Lists all genres of the show "Dexter". |
| **15** | `15-comedy_only.sql` | Lists all shows categorized under the "Comedy" genre. |
| **16** | `16-shows_by_genre.sql` | Lists all shows and all genres linked to them (including `NULL`). |

## 👤 Author
- **Julian Gonzalez** - [GitHub Profile](https://github.com/your_username_here)
- Student at **Holberton School, Rennes**.
