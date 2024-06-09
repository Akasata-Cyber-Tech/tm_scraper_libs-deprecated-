from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

def insert_example_data(engine):
    """
    Insert example data into the users table.
    
    Parameters:
        engine: SQLAlchemy engine object.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Example data
    example_users = [
        User(name='John Doe', email='john.doe@example.com'),
        User(name='Jane Smith', email='jane.smith@example.com')
    ]
    
    # Insert data
    session.add_all(example_users)
    session.commit()
    print("Example data inserted successfully.")
