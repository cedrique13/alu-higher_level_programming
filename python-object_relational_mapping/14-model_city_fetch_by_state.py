#!/usr/bin/python3
"""Prints all City objects from the database, grouped by State."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Get credentials
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Setup engine and session
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their corresponding state
    results = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print in the specified format
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

