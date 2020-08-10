#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    """ Function body """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
