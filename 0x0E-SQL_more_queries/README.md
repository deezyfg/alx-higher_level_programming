# SQL - More Queries

This repository contains a series of SQL scripts aimed at introducing various fundamental SQL operations. These scripts are designed to be executed on a MySQL server.

## Resources

**Read or watch:**
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
- [MySQL constraints](https://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

Extra resources around relational database model design:

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)
  
### Learning Objectives

By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of google**:
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL

**In the container, credentials are** `root/root`

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are** `root/root`

### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks Overview

### 0. My privileges!
- **Script:** [0-privileges.sql](0x0E-SQL_more_queries/0-privileges.sql)
- **Description:** This script lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server (in `localhost`).

### 1. Root user
- **Script:** [1-create_user.sql](0x0E-SQL_more_queries/1-create_user.sql)
- **Description:** This script creates the MySQL server user `user_0d_1` with all privileges. The password for `user_0d_1` is set to `user_0d_1_pwd`. If the user `user_0d_1` already exists, the script will not fail.

### 2. Read User
- **Script:** [2-create_read_user.sql](0x0E-SQL_more_queries/2-create_read_user.sql)
- **Description:** This script creates the database `hbtn_0d_2` and the user `user_0d_2`. `user_0d_2` is granted only SELECT privilege in the database `hbtn_0d_2`. The password for `user_0d_2` is set to `user_0d_2_pwd`. If the database `hbtn_0d_2` or the user `user_0d_2` already exists, the script will not fail.

### 3. Always a name
- **Script:** [3-force_name.sql](0x0E-SQL_more_queries/3-force_name.sql)
- **Description:** This script creates the table `force_name` on the MySQL server. The table contains two columns: `id` of type INT (auto-generated and cannot be null) and `name` of type VARCHAR(256) (cannot be null). The database name is passed as an argument of the mysql command. If the table `force_name` already exists, the script will not fail.

### 4. ID can't be null
- **Script:** [4-never_empty.sql](0x0E-SQL_more_queries/4-never_empty.sql)
- **Description:** This script creates the table `id_not_null` on the MySQL server. The table contains two columns: `id` of type INT with default value 1 and `name` of type VARCHAR(256). The database name is passed as an argument of the mysql command. If the table `id_not_null` already exists, the script will not fail.

### 5. Unique ID
- **Script:** [5-unique_id.sql](0x0E-SQL_more_queries/5-unique_id.sql)
- **Description:** This script creates the table `unique_id` on the MySQL server. The table contains two columns: `id` of type INT with default value 1 (must be unique) and `name` of type VARCHAR(256). The database name is passed as an argument of the mysql command. If the table `unique_id` already exists, the script will not fail.

### 6. States table
- **Script:** [6-states.sql](0x0E-SQL_more_queries/6-states.sql)
- **Description:** This script creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on the MySQL server. The table contains two columns: `id` of type INT (auto-generated and cannot be null, primary key) and `name` of type VARCHAR(256) (cannot be null). If the database `hbtn_0d_usa` or the table `states` already exists, the script will not fail.

### 7. Cities table
- **Script:** [7-cities.sql](0x0E-SQL_more_queries/7-cities.sql)
- **Description:** This script creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on the MySQL server. The table contains three columns: `id` of type INT (auto-generated and cannot be null, primary key), `state_id` of type INT (cannot be null, foreign key referencing `id` of the `states` table), and `name` of type VARCHAR(256) (cannot be null). If the database `hbtn_0d_usa` or the table `cities` already exists, the script will not fail.

### 8. Cities of California
- **Script:** 8-cities_of_california_subquery.sql
- **Description:** This script lists all the cities of California that can be found in the database `hbtn_0d_usa`. The `states` table contains only one record where `name = California` (but the `id` can be different). Results are sorted in ascending order by `cities.id`. You are not allowed to use the `JOIN` keyword. The database name will be passed as an argument of the `mysql` command.

### 9. Cities by States
- **Script:** 9-cities_by_state_join.sql
- **Description:** This script lists all cities contained in the database `hbtn_0d_usa`. Each record displays `cities.id, cities.name, and states.name`. Results are sorted in ascending order by `cities.id`. You are allowed to use only one `SELECT` statement. The database name will be passed as an argument of the `mysql` command.

### 10. Genre ID by show
- **Script:** 10-genre_id_by_show.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Each record displays `tv_shows.title` - `tv_show_genres.genre_id`. Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 11. Genre ID for all shows
- **Script:** 11-genre_id_all_shows.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all shows contained in the database `hbtn_0d_tvshows`. Each record displays `tv_shows.title` - `tv_show_genres.genre_id`. Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. If a show doesn’t have a genre, `NULL` is displayed. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 12. No genre
- **Script:** 12-no_genre.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all shows contained in `hbtn_0d_tvshows` without a genre linked. Each record displays `tv_shows.title` - `tv_show_genres.genre_id`. Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 13. Number of shows by genre
- **Script:** 13-count_shows_by_genre.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. Each record displays `<TV Show genre> - <Number of shows linked to this genre>`. The first column is called `genre` and the second column is called `number_of_shows`. Don’t display a genre that doesn’t have any shows linked. Results are sorted in descending order by the number of shows linked. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 14. My genres
- **Script:** 14-my_genres.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`. The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different). Each record displays `tv_genres.name`. Results are sorted in ascending order by the genre name. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql command.

### 15. Only Comedy
- **Script:** 15-comedy_only.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all Comedy shows in the database `hbtn_0d_tvshows`. The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different). Each record displays `tv_shows.title`. Results are sorted in ascending order by the show title. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 16. List shows and genres
- **Script:** 16-shows_by_genre.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. If a show doesn’t have a genre, NULL is displayed in the genre column. Each record displays `tv_shows.title` - `tv_genres.name`. Results are sorted in ascending order by the show title and genre name. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 17. Not my genre
- **Script:** 100-not_my_genres.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`. The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different). Each record displays `tv_genres.name`. Results are sorted in ascending order by the genre name. A maximum of two `SELECT` statements are allowed. The database name will be passed as an argument of the `mysql` command.

### 18. No Comedy tonight!
- **Script:** 101-not_a_comedy.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) into your MySQL server. This script lists all shows without the genre Comedy in the database `hbtn_0d_tvshows`. The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different). Each record displays `tv_shows.title`. Results are sorted in ascending order by the show title. A maximum of two `SELECT` statements are allowed. The database name will be passed as an argument of the `mysql` command.

### 19. Rotten tomatoes
- **Script:** 102-rating_shows.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows_rate.sql](hbtn_0d_tvshows_rate.sql) into your MySQL server. This script lists all shows from `hbtn_0d_tvshows_rate` by their rating. Each record displays `tv_shows.title` - `rating sum`. Results are sorted in descending order by the rating. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

### 20. Best genre
- **Script:** 103-rating_genres.sql
- **Description:** Imports the database dump from [hbtn_0d_tvshows_rate.sql](hbtn_0d_tvshows_rate.sql) into your MySQL server. This script lists all genres in the database `hbtn_0d_tvshows_rate` by their rating. Each record displays `tv_genres.name` - `rating sum`. Results are sorted in descending order by their rating. Only one `SELECT` statement is allowed. The database name will be passed as an argument of the `mysql` command.

## Author

[Peter Opoku-Mensah](https://github.com/deezyfg)