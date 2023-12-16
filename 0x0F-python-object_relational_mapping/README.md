# 0x0F. Python - Object-relational mapping project:


Description for all the files and directories in this directory
Any file that does't have a description -if there any- is for testing purposes


`0-select_states.py` -> a script that lists all states from the database `hbtn_0e_0_usa`:

The script takes 3 arguments: mysql username, mysql password and database name (no argument validation)
The script connects to a MySQL server running on localhost at port 3306
Results is sorted in ascending order by states.id


`1-filter_states.py` -> a script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`:

The script takes 3 arguments: mysql username, mysql password and database name (no argument validation)
The script connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id


`2-my_filter_states.py` -> a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument.

The script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation)
The script connects to a MySQL server running on localhost at port 3306
Results will be sorted in ascending order by states.id


`3-my_safe_filter_states.py` -> the same as `2-my_filter_states.py` but safe from MySQL injections!


`4-cities_by_state.py` -> a script that lists all cities from the database `hbtn_0e_4_usa`

The script takes 3 arguments: mysql username, mysql password and database name
The script connects to a MySQL server running on localhost at port 3306
Results is sorted in ascending order by cities.id


`5-filter_cities.py` -> a script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`

The script takes 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
The script connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id

