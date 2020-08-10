#!/usr/bin/python3
""" All states via SQLAlchemy """
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

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
