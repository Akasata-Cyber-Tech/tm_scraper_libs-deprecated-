from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example usage
username = 'tefos'
password = 'TeFoS_S3CURE$$'
host = '10.147.17.166'
port = 5432
database = 'tmdb'

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
