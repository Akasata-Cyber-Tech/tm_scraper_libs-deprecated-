from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class AttackData(Base):
    __tablename__ = 'attack_data'
    id = Column(Integer, primary_key=True)
    sourceIp = Column(String, nullable=False)
    destinationIp = Column(String, nullable=False)
    rulename = Column(String, nullable=False)
    indicators = Column(String, nullable=False)