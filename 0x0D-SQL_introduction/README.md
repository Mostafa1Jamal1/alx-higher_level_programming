# `0x0D-SQL_introduction` project:


Description for all the files in this directory
Any file that does't have a description is for testing purposes


`0-list_databases.sql` -> a script that lists all databases of your MySQL server.


`1-create_database_if_missing.sql` -> a script that creates the database `hbtn_0c_0` in your MySQL server.
If the database `hbtn_0c_0` already exists, your script should not fail


`2-remove_database.sql` -> a script that deletes the database `hbtn_0c_0` in your MySQL server.
If the database `hbtn_0c_0` doesn’t exist, your script should not fail


`3-list_tables.sql` -> a script that lists all the tables of a database in your MySQL server.
The database name will be passed as argument of `mysql` command


`4-first_table.sql` -> a script that creates a table called `first_table` in the current database in your MySQL server.
- `first_table` description:
	id INT
	name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table `first_table` already exists, your script should not fail


`5-full_table.sql` -> a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command


`6-list_values.sql` -> a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- All fields should be printed
- The database name will be passed as an argument of the mysql command

