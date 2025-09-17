# 代码生成时间: 2025-09-17 16:02:40
import pandas as pd
from sqlalchemy import create_engine

"""
Database Migration Tool

This tool is designed to migrate data from one database to another using pandas and sqlalchemy.
It provides a simple and efficient way to transfer data between different database systems.
"""

class DatabaseMigrationTool:
    def __init__(self, source_db, target_db):
        """
        Initializes the DatabaseMigrationTool with source and target database connections.

        Args:
        source_db (str): The connection string for the source database.
        target_db (str): The connection string for the target database.
        """
        self.source_db = source_db
        self.target_db = target_db
        self.source_engine = create_engine(source_db)
        self.target_engine = create_engine(target_db)

    def migrate_table(self, table_name):
        """
        Migrates a single table from the source database to the target database.

        Args:
        table_name (str): The name of the table to migrate.
        """
        try:
            # Read data from the source table
            data = pd.read_sql_table(table_name, self.source_engine)

            # Write data to the target table, replacing existing data
            data.to_sql(table_name, self.target_engine, if_exists='replace', index=False)

            print(f"Successfully migrated {table_name} from {self.source_db} to {self.target_db}")

        except Exception as e:
            # Handle any errors that occur during the migration process
            print(f"Error migrating {table_name}: {str(e)}")

    def migrate_all_tables(self):
        """
        Migrates all tables from the source database to the target database.
        """
        try:
            # Get a list of tables in the source database
            tables = pd.read_sql("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'", self.source_engine)

            # Migrate each table individually
            for i, row in tables.iterrows():
                self.migrate_table(row['table_name'])

            print("Successfully migrated all tables")

        except Exception as e:
            # Handle any errors that occur during the migration process
            print(f"Error migrating all tables: {str(e)}")

# Example usage
if __name__ == '__main__':
    # Define the connection strings for the source and target databases
    source_db = 'postgresql://user:password@host:port/dbname'
    target_db = 'mysql://user:password@host:port/dbname'

    # Create an instance of the DatabaseMigrationTool
    migration_tool = DatabaseMigrationTool(source_db, target_db)

    # Migrate a specific table
    #migration_tool.migrate_table('my_table')

    # Migrate all tables
    migration_tool.migrate_all_tables()