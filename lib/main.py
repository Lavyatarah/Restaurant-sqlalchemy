from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.customer import Customer
from classes.review import Review
from classes .Restaurant import Restaurant
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Define the database file path (assuming it's in the current directory)
# database_url = 'sqlite:///database.db'
# Create an SQLAlchemy engine
engine = create_engine(database.db)
# Create the tables in the database if they don't exist
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine, autoflush=False) 
session = Session()

if __name__ == "__main__":
    pass 
 