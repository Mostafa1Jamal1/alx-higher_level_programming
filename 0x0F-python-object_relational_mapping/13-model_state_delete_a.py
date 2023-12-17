#!/usr/bin/python3
''' a script that deletes all State objects
with a name containing the letter a
from the database hbtn_0e_6_usa '''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username, password, dbname),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    session.query(State).filter(State.name.like("%a%")).delete()
    session.commit()
    session.close()
