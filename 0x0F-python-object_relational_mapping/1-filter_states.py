#!/usr/bin/python3
''' a script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa '''


import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbname, charset="utf8mb4")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE 'N_%' COLLATE utf8mb4_ja_0900_as_cs\
                ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
