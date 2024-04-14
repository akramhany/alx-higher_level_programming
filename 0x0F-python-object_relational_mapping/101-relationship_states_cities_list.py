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
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).order_by(State.id)
    for state in results:
        print(str(state.id) + ': ' + state.name)
        for city in state.cities:
            print('    ' + str(city.id) + ': ' + city.name)
