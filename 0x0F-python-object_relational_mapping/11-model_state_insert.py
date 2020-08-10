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
    new = State(name='Louisiana')
    session.add(new)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(state.id)
    session.commit()
    session.close()