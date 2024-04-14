#!/usr/bin/python3

"""A script that executes a query using sqlalchemy ORM"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(username, password, db_name)
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    s = State(name='California')
    c = City(name='San Francisco')

    s.cities.append(c)

    session.add(c)
    session.add(s)
    session.commit()
