#!/usr/bin/python3
"""
Start link class to table in database with sqlalchemy
Script that prints all `City` objects from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state, cities in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print(f"{state.name}: ({cities.id}) {cities.name}")
    session.close()
