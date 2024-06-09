from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy as db

Base = declarative_base()
metadata_obj = db.MetaData() 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class AttackData(Base):
    __tablename__ = 'attack_data'
    id = Column(Integer, primary_key=True)
    sourceIp = Column(String, nullable=False)
    destinationIp = Column(String, nullable=False)
    rulename = Column(String, nullable=False)
    indicators = Column(String, nullable=False)


def create_table(engine):
    """
    Create the users table in the database.
    
    Parameters:
        engine: SQLAlchemy engine object.
    """
    # database name 
    profile = db.Table( 
        'profile',                                         
        metadata_obj,                                     
        db.Column('email', db.String, primary_key=True),   
        db.Column('name', db.String),                     
        db.Column('contact', db.Integer),                 
    ) 

    # metadata_obj.create_all(engine)
    profile.create(engine)
    # profile.drop(engine)
    # Base.metadata.create_all(engine)
    print("Table created successfully.")