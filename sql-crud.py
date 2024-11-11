from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


#create a class-based table for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(string)
    last_name  = Column(string)
    gender = Column(string)
    nationality = Column(string)
    famous_for = Column(string)



# instead of connecting to the database directly, we will ask for a session
# create a new instance of a sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#opens actual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)