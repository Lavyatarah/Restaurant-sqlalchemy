from classes import restaurant, review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.customer import Customer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Define the database file path (assuming it's in the current directory)
database_url = 'sqlite:///database.db'
# Create an SQLAlchemy engine
engine = create_engine(database_url)
# Create the tables in the database if they don't exist
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()
if __name__ == "__main__":
    # Entry point for running the application
    pass