# `0x0E-SQL_more_queries` project:



Description for all the files in this directory
Any file that does't have a description is for testing purposes


`0-privileges.sql` -> a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).


`1-create_user.sql` -> a script that creates the MySQL server user `user_0d_1`.
- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
- If the user `user_0d_1` already exists, your script should not fail


`2-create_read_user.sql` -> a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail


`3-force_name.sql` -> a script that creates the table `force_name` on your MySQL server.
- `force_name` description:
	- `id` INT
	- `name` VARCHAR(256) can’t be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail


`4-never_empty.sql` -> a script that creates the table `id_not_null` on your MySQL server.
- `id_not_null` description:
	- id INT with the default value 1
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table `id_not_null` already exists, your script should not fail


`5-unique_id.sql` -> a script that creates the table `unique_id` on your MySQL server.
- `unique_id` description:
	- id INT with the default value 1 and must be unique
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table `unique_id` already exists, your script should not fail


`6-states.sql` -> a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
- `states` description:
	- id INT unique, auto generated, can’t be null and is a primary key
	- name VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail


`7-cities.sql` ->  a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
- `cities` description:
	- `id` INT unique, auto generated, can’t be null and is a primary key
	- `state_id` INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
	- `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `cities` already exists, your script should not fail

