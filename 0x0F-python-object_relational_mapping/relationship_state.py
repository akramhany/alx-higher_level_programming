#!/usr/bin/python3

"""Contains the state class that represents a table"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mmetadata = MetaData()
Base = declarative_base(metadata=mmetadata)


class State(Base):
    """State class that represents a table"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')
