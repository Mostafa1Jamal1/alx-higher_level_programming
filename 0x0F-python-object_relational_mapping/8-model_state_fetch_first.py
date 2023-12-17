#!/usr/bin/python3
''' a script that prints the first State object from the database hbtn_0e_6_usa '''

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
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    row = session.query(State)[0]
    print("{}: {}".format(row.id, row.name))
    
