#!/usr/bin/python3
"""
Start link class to table in database with sqlalchemy
Script that prints all `City` objects from hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_S = State(name="California")
    new_C = City(name="San Francisco")
    new_S.cities.append(new_C)
    session.add(new_S)
    session.add(new_C)
    session.commit()
    session.close()
