#!/usr/bin/python3
"""
Lists states with 'a' in their name from the hbtn_0e_6_usa database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()