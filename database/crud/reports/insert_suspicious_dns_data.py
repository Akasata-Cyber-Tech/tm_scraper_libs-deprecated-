from sqlalchemy import Column, Integer, String
from app.db.base import Base

class insert_attack_data(Base):
    __tablename__ = "attack_data"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

