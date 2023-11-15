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


