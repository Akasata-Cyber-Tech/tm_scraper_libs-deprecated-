from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from select_table import fetch_all_users
from create_table import create_table 
from table_models import create_attack_table
from table_models import create_suspicious_dns_table
from table_models import create_malware_table
from table_models import drop_attack_table

def create_connection(username, password, host, port, database):
    """
    Create a connection to a PostgreSQL database using SQLAlchemy.
    
    Parameters:
        username (str): PostgreSQL username.
        password (str): PostgreSQL password.
        host (str): PostgreSQL host address.
        port (int): PostgreSQL port number.
        database (str): Name of the PostgreSQL database.

    Returns:
        engine: SQLAlchemy engine object if connection is successful, None otherwise.
    """
    try:
        # Construct the connection URL
        db_url = f'postgresql://{username}:{password}@{host}:{port}/{database}'
        
        # Create the engine
        engine = create_engine(db_url)
        
        # Test the connection
        engine.connect()
        
        print("Connection to the database was successful.")
        return engine
    
    except SQLAlchemyError as e:
        print(f"Connection failed: {e}")
        return None

# Example usage
username = 'tefos'
password = 'TeFoS_S3CURE$$'
host = '10.147.17.166'
port = 5432
database = 'tmdb'

engine = create_connection(username, password, host, port, database)
if engine:
    # drop_attack_table(engine)
    # create_table(engine)
    create_attack_table(engine)
    create_suspicious_dns_table(engine)
    create_malware_table(engine)
    # insert_example_data(engine)
    # fetch_all_users(engine)