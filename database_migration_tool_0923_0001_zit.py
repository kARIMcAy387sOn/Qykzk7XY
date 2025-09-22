# 代码生成时间: 2025-09-23 00:01:14
import pandas as pd
from sqlalchemy import create_engine

"""
Database Migration Tool using Python and Pandas.
This tool migrates data from an existing database to a new database.
"""

# Function to create a database engine
def create_database_engine(db_url):
    """
    Create a database engine using SQLAlchemy.
    
    Args:
        db_url (str): The URL of the database.
    
    Returns:
        engine: The database engine.
    """
    try:
        engine = create_engine(db_url)
        return engine
    except Exception as e:
        print(f"Error creating database engine: {e}")
        raise

# Function to read data from a database table
def read_data_from_table(engine, table_name):
    """
    Read data from a database table using Pandas.
    
    Args:
        engine (object): The database engine.
        table_name (str): The name of the table.
    
    Returns:
        df (DataFrame): The DataFrame containing the table data.
    """
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        print(f"Error reading data from table {table_name}: {e}")
        raise

# Function to write data to a database table
def write_data_to_table(engine, df, table_name):
    """
    Write data to a database table using Pandas.
    
    Args:
        engine (object): The database engine.
        df (DataFrame): The DataFrame containing the data to write.
        table_name (str): The name of the table.
    """
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error writing data to table {table_name}: {e}")
        raise

# Function to migrate data from one database to another
def migrate_data(source_db_url, target_db_url, table_name):
    """
    Migrate data from one database to another.
    
    Args:
        source_db_url (str): The URL of the source database.
        target_db_url (str): The URL of the target database.
        table_name (str): The name of the table to migrate.
    """
    try:
        # Create database engines for source and target databases
        source_engine = create_database_engine(source_db_url)
        target_engine = create_database_engine(target_db_url)
        
        # Read data from the source database table
        df = read_data_from_table(source_engine, table_name)
        
        # Write data to the target database table
        write_data_to_table(target_engine, df, table_name)
        print(f"Data migration from {source_db_url} to {target_db_url} for table {table_name} completed successfully.")
    except Exception as e:
        print(f"Error migrating data: {e}")
        raise

# Example usage
if __name__ == '__main__':
    source_db_url = "postgresql://user:password@host:port/dbname"
    target_db_url = "postgresql://user:password@host:port/dbname"
    table_name = "my_table"
    migrate_data(source_db_url, target_db_url, table_name)