#!/usr/bin/python3
"""
Finds a state by name from the hbtn_0e_6_usa database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, state_name_search = sys.argv[1:5]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name_search).first()
        print(f"{state.id}" if state else "Not found")

        session.close()
