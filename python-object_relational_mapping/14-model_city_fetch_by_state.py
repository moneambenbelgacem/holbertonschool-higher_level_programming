#!/usr/bin/python3
"""Fetch Two tables"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State, City) \
                    .filter(State.id == City.state_id)

    for city in cities:
        print("{}: ({}) {}"
              .format(city.State.name, city.City.id, city.City.name))

    session.close()
