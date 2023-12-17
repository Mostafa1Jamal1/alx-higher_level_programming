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



`model_state.py` -> a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:
State class:
	inherits from `Base`
	links to the MySQL table `states`
	class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
The script connects to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be imported before calling `Base.metadata.create_all(engine)`


`7-model_state_fetch_all.py` -> a script that lists `all State` objects from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
The script connects to a MySQL server running on localhost at port 3306
Results will be sorted in ascending order by `states.id`


`8-model_state_fetch_first.py` -> a script that prints the first State object from the database `hbtn_0e_6_usa`


`9-model_state_filter_a.py` -> a script that lists all State objects that contain the letter a from the database `hbtn_0e_6_usa`



`10-model_state_my_get.py` -> a script that prints the State object with the name passed as argument from the database `hbtn_0e_6_usa`



`11-model_state_insert.py`-> a script that adds the State object “Louisiana” to the database `hbtn_0e_6_usa`

