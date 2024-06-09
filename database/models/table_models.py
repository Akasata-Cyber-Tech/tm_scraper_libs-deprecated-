from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy as db
from db_models import AttackData

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

attack_table = db.Table( 
    'attack_data',
    metadata_obj,
    db.Column('id', db.String, primary_key=True),   
    db.Column('sourceIp', db.String),                     
    db.Column('destinationIp', db.String),                 
    db.Column('rulename', db.String),                 
    db.Column('indicator', db.String),                 
) 

def create_attack_table(engine):
    """
    Create the users table in the database.
    
    Parameters:
        engine: SQLAlchemy engine object.
    """
    # database name 

    # metadata_obj.create_all(engine)
    attack_table.create(engine)
    # profile.drop(engine)
    # Base.metadata.create_all(engine)
    print("Table created successfully.")


def create_suspicious_dns_table(engine):
    # database name 
    suspicious_dns_table = db.Table( 
        'suspicious_dns',                                         
        metadata_obj,                                     
        db.Column('id', db.String, primary_key=True),   
        db.Column('sourceIp', db.String),                     
        db.Column('destinationIp', db.String),                 
        db.Column('rulename', db.String),                 
        db.Column('indicator', db.String),                 
    ) 

    # metadata_obj.create_all(engine)
    suspicious_dns_table.create(engine)
    # profile.drop(engine)
    # Base.metadata.create_all(engine)
    print("Table created successfully.")


def create_malware_table(engine):
    # database name 
    malware_table = db.Table( 
        'malware',                                         
        metadata_obj,                                     
        db.Column('id', db.String, primary_key=True),   
        db.Column('endpointHostname', db.String),                     
        db.Column('endpointIp', db.String),                 
        db.Column('filenames', db.String),                 
    ) 

    # metadata_obj.create_all(engine)
    malware_table.create(engine)
    # profile.drop(engine)
    # Base.metadata.create_all(engine)
    print("Table created successfully.")


def drop_attack_table(engine):
    # database name 
    # metadata_obj.create_all(engine)
    attack_table.drop(engine)
    # profile.drop(engine)
    # Base.metadata.create_all(engine)
    print("Table created successfully.")