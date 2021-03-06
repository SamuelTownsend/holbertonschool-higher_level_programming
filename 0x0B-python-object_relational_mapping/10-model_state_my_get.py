#!/usr/bin/python3
#!/usr/bin/python3
"""
This script lists the State object from the database and matches  given name with argument
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    dbengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(dbengine)
    dbsess = sessionmaker(bind=dbengine)

    try:
        print(dbsess().query(State).filter(
            State.name == argv[4])[0].id)

    except Exception:
        print("Not found")

    dbsess().close
