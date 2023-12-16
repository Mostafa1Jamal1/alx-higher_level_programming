#!/usr/bin/python3
''' a script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. '''


import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    namematch = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbname, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                WHERE BINARY name = BINARY '{}'\
                ORDER BY id".format(namematch))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
