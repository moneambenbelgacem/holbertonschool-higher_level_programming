#!/usr/bin/python3
"""Select State by name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana")\
        .one()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
