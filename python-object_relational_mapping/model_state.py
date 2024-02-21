#!/usr/bin/python3
"""
Defines a State model with SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class State(Base):
    """
    Defines the class State that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://<username>:<password>@localhost:3306/<dbname>', pool_pre_ping=True)

Base.metadata.create_all(engine)
