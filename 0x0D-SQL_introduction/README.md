# SQL Introduction

This repository contains a series of SQL scripts aimed at introducing various fundamental SQL operations. These scripts are designed to be executed on a MySQL server.

## Resources

Read or watch:
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
- [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [Installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
  
### Learning Objectives

By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of google**:
- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- What `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE`, or `DELETE` data
- What `subqueries` are and how to use them
- How to use MySQL functions

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
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
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
In the container, credentials are `root/root`


## Tasks Overview

### 0. List Databases
- **Script:** [0-list_databases.sql](0x0D-SQL_introduction/0-list_databases.sql)
- **Description:** This script lists all databases currently present on the MySQL server.

### 1. Create a Database
- **Script:** [1-create_database_if_missing.sql](0x0D-SQL_introduction/1-create_database_if_missing.sql)
- **Description:** This script creates a database named `hbtn_0c_0` if it does not already exist. It ensures that the database is created only if it's missing, without causing an error if it already exists.

### 2. Delete a Database
- **Script:** [2-remove_database.sql](0x0D-SQL_introduction/2-remove_database.sql)
- **Description:** This script deletes the database named `hbtn_0c_0` from the MySQL server, if it exists. It ensures that the script doesn't fail if the database doesn't exist.

### 3. List Tables
- **Script:** [3-list_tables.sql](0x0D-SQL_introduction/3-list_tables.sql)
- **Description:** This script lists all tables within a specified database. The database name is passed as an argument to the script.

### 4. First Table
- **Script:** [4-first_table.sql](0x0D-SQL_introduction/4-first_table.sql)
- **Description:** This script creates a new table named `first_table` in the current database. The table has two columns: `id` of type INT and `name` of type VARCHAR(256).

### 5. Full Description
- **Script:** [5-full_table.sql](0x0D-SQL_introduction/5-full_table.sql)
- **Description:** This script retrieves and prints the complete description of the `first_table`, including its structure, such as column names, data types, and any constraints.

### 6. List All in Table
- **Script:** [6-list_values.sql](0x0D-SQL_introduction/6-list_values.sql)
- **Description:** This script lists all rows present in the `first_table`, displaying all fields.

### 7. First Add
- **Script:** [7-insert_value.sql](0x0D-SQL_introduction/7-insert_value.sql)
- **Description:** This script inserts a new row into the `first_table` with predefined values: `id = 89` and `name = Best School`.

### 8. Count 89
- **Script:** [8-count_89.sql](0x0D-SQL_introduction/8-count_89.sql)
- **Description:** This script counts and displays the number of records with `id = 89` in the `first_table`.

### 9. Full Creation
- **Script:** [9-full_creation.sql](0x0D-SQL_introduction/9-full_creation.sql)
- **Description:** This script creates a new table named `second_table` in the specified database and inserts multiple rows with predefined values into it.

### 10. List by Best
- **Script:** [10-top_score.sql](0x0D-SQL_introduction/10-top_score.sql)
- **Description:** This script lists all records from `second_table`, ordered by their score in descending order.

### 11. Select the Best
- **Script:** [11-best_score.sql](0x0D-SQL_introduction/11-best_score.sql)
- **Description:** This script lists records from `second_table` with a score greater than or equal to 10, ordered by score in descending order.

### 12. Cheating is Bad
- **Script:** [12-no_cheating.sql](0x0D-SQL_introduction/12-no_cheating.sql)
- **Description:** This script updates the score of the record with the name 'Bob' to 10 in `second_table`, without directly using the id value.

### 13. Score Too Low
- **Script:** [13-change_class.sql](0x0D-SQL_introduction/13-change_class.sql)
- **Description:** This script removes all records from `second_table` with a score less than or equal to 5.

### 14. Average
- **Script:** [14-average.sql](0x0D-SQL_introduction/14-average.sql)
- **Description:** This script computes and displays the average score of all records in `second_table`.

### 15. Number by Score
- **Script:** [15-groups.sql](0x0D-SQL_introduction/15-groups.sql)
- **Description:** This script lists the number of records with the same score in `second_table`, sorted by the number of records in descending order.

### 16. Say My Name
- **Script:** [16-no_link.sql](0x0D-SQL_introduction/16-no_link.sql)
- **Description:** This script lists all records from `second_table` excluding rows where the name field is empty, sorted by score in descending order.

### 17. Go to UTF8
- **Script:** [100-move_to_utf8.sql](0x0D-SQL_introduction/100-move_to_utf8.sql)
- **Description:** This script converts the database `hbtn_0c_0`, the table `first_table`, and the field `name` to UTF8 encoding.

### 18. Temperatures #0
- **Script:** [101-avg_temperatures.sql](0x0D-SQL_introduction/101-avg_temperatures.sql)
- **Description:** This script imports the table dump from [temperatures.sql](temperatures.sql) into the `hbtn_0c_0` database. The script then  calculates and displays the average temperature (in Fahrenheit) by city, ordered by temperature in descending order.

### 19. Temperatures #1
- **Script:** [102-top_city.sql](0x0D-SQL_introduction/102-top_city.sql)
- **Description:** This script imports the table dump from [temperatures.sql](temperatures.sql) into the `hbtn_0c_0` database. The table dump contains temperature data for various cities during July and August. The script then retrieves and displays the top 3 cities' temperatures, ordered by temperature in descending order.

### 20. Temperatures #2
- **Script:** [103-max_state.sql](0x0D-SQL_introduction/103-max_state.sql)
- **Description:** This script imports the table dump from [temperatures.sql](temperatures.sql) into the `hbtn_0c_0` database. The script then retrieves and displays the maximum temperature of each state, ordered by state name.


## Author

Peter Opoku-Mensah(https://github.com/deezyfg)