#!/usr/bin/python3
"""
a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    states = session().query(State).filter(State.name == argv[4]).all()
    if states:
        for state in states:
            if state.name == argv[4]:
                print("{}".format(state.id))
    else:
        print("Not found")
    session().close()
