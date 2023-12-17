#!/usr/bin/python3
''' a script that prints the first State object
from the database hbtn_0e_6_usa '''

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           username, password, dbname), pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    query = session.query(State).order_by(State.id)

    try:
        first_State = query.first()
        print("{}: {}".format(first_State.id, first_State.name))
    except Exception:
        print("Nothing")
