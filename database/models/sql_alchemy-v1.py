
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: Define the connection URI for your database
db_url = 'postgresql://username:password@localhost:5432/postgres'  # Change this to your PostgreSQL connection string
engine = create_engine(db_url)

# Step 2: Create a new user (PostgreSQL example, optional step)
def create_user(engine, username, password):
    with engine.connect() as connection:
        connection.execute(f"CREATE USER {username} WITH PASSWORD '{password}';")

# Create a new user (run once, then comment out)
# create_user(engine, 'newuser', 'newpassword')

# Step 3: Create a new database
def create_database(engine, database_name):
    with engine.connect() as connection:
        connection.execute(f"CREATE DATABASE {database_name};")

# Create a new database (run once, then comment out)
# create_database(engine, 'newdatabase')

# Step 4: Define a new engine connected to the new database
new_db_url = 'postgresql://newuser:newpassword@localhost:5432/newdatabase'  # Change to the new user and database
new_engine = create_engine(new_db_url)

# Step 5: Define ORM Base and User class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# Step 6: Create the users table in the new database
Base.metadata.create_all(new_engine)

# Step 7: Create a session to interact with the database
Session = sessionmaker(bind=new_engine)
session = Session()

# Step 8: Add a new user to the users table
new_user = User(name='John Doe', email='john.doe@example.com')
session.add(new_user)
session.commit()

print("User added successfully.")
