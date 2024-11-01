<div align="center">
<br>

![Introduction.png](README-image/introduction.png)

</div>


<p align="center">
<img src="https://img.shields.io/badge/-SQL-yellow">
<img src="https://img.shields.io/badge/-Linux-lightgrey">
<img src="https://img.shields.io/badge/-WSL-brown">
<img src="https://img.shields.io/badge/-Ubuntu%2020.04.4%20LTS-orange">
<img src="https://img.shields.io/badge/-JetBrains-blue">
<img src="https://img.shields.io/badge/-Holberton%20School-red">
<img src="https://img.shields.io/badge/License-not%20specified-brightgreen">
</p>


<h1 align="center"> SQL - Introduction </h1>


<h3 align="center">
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#eye-about">About</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#hammer_and_wrench-tasks">Tasks</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#memo-learning-objectives">Learning Objectives</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#computer-requirements">Requirements</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#keyboard-more-info">More Info</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#mag_right-resources">Resources</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#bust_in_silhouette-authors">Authors</a> •
<a href="https://github.com/RazikaBengana/holbertonschool-higher_level_programming/tree/main/SQL_introduction#octocat-license">License</a>
</h3>

---

<!-- ------------------------------------------------------------------------------------------------- -->

<br>
<br>

## :eye: About

<br>

<div align="center">

**`SQL - introduction`** project covers fundamental SQL concepts and operations.
<br>
The programs demonstrate essential database management tasks, including creating and listing databases, creating tables, inserting data, and performing basic queries.
<br>
They progress from simple operations like showing databases to more complex tasks such as calculating averages and joining tables, providing a comprehensive introduction to SQL for beginners.
<br>
<br>
This project has been created by **[Holberton School](https://www.holbertonschool.com/about-holberton)** to enable every student to understand how SQL language works.

</div>

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :hammer_and_wrench: Tasks

<br>

**`0. List databases`**

**`1. Create a database`**

**`2. Delete a database`**

**`3. List tables`**

**`4. First table`**

**`5. Full description`**

**`6. List all in table`**

**`7. First add`**

**`8. Count 89`**

**`9. Full creation`**

**`10. List by best`**

**`11. Select the best`**

**`12. Cheating is bad`**

**`13. Score too low`**

**`14. Average`**

**`15. Number by score`**

**`16. Say my name`**

**`17. Go to UTF8`**

**`18. Temperatures #0`**

**`19. Temperatures #1`**

**`20. Temperatures #2`**

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :memo: Learning Objectives

<br>

**_You are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:_**

<br>

```diff

General

+ What’s a database

+ What’s a relational database

+ What does SQL stand for

+ What’s MySQL

+ How to create a database in MySQL

+ What does DDL and DML stand for

+ How to CREATE or ALTER a table

+ How to SELECT data from a table

+ How to INSERT, UPDATE or DELETE data

+ What are subqueries

+ How to use MySQL functions

```

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :computer: Requirements

<br>

```diff

General

+ Allowed editors: vi, vim, emacs

+ All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)

+ All your files should end with a new line

+ All your SQL queries should have a comment just before (i.e. syntax above)

+ All your files should start by a comment describing the task

+ All SQL keywords should be in uppercase (SELECT, WHERE…)

+ A README.md file, at the root of the folder of the project, is mandatory

+ The length of your files will be tested using wc

```

<br>

**_Why all your files should end with a new line? See [HERE](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789)_**

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :keyboard: More Info

<br>

### Comments for your SQL file:

<br>

```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

<br>
<br>

### Install MySQL 8.0 on Ubuntu 20.04 LTS:

<br>

```yaml
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

<br>
<br>

### Connect to your MySQL server:

<br>

```sql
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

<br>
<br>

### Use the sandbox to run MySQL:

<br>

- In the container, credentials are `root/root`

  - Ask for container `Ubuntu 20.04`
  - Connect via SSH
  - OR connect via the Web terminal
  - In the container, you should start MySQL before playing with it:

<br>

```yaml
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

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :mag_right: Resources

<br>

**_Do you need some help?_**

<br>

**Concepts:**

* [Databases](https://drive.google.com/file/d/1-uWmKnCp1m0VAWhyHVWvkV8etRBHV8tt/view?usp=sharing)

<br>

**Read or watch:**

* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)

* [Install MySQL (MySQL Server)](https://www.youtube.com/watch?v=9h3ctGFTz9w)

* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)

* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)

* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)

* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)

* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :bust_in_silhouette: Authors

<br>

<img src="https://img.shields.io/badge/Razika%20Bengana-darkblue" alt="Razika Bengana" width="120">

<br>
<br>

<!-- ------------------------------------------------------------------------------------------------- -->

## :octocat: License

<br>

```SQL - introduction``` _project has no license specified._

<br>
<br>

---

<p align="center"><br>2022</p>