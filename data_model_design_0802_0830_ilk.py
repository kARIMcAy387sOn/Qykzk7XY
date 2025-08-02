# 代码生成时间: 2025-08-02 08:30:51
import pandas as pd

"""
Data Model Design using Python and Pandas.
This program demonstrates the creation of a data model with error handling,
comments, and follows best practices for maintainability and scalability.
"""

# Define a DataFrame to hold our data model
class DataModel:
    def __init__(self, data):
        """Initialize the DataModel with a DataFrame."""
        try:
            # Attempt to create a DataFrame from the provided data
            self.df = pd.DataFrame(data)
        except ValueError as e:
            # Handle the case where data is not in the correct format
            print(f"Error creating DataFrame: {e}")
            raise
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise

    def add_column(self, column_name, data):
        """Add a new column to the DataFrame."""
        try:
            self.df[column_name] = data
        except Exception as e:
            print(f"Error adding column '{column_name}': {e}")
            raise

    def remove_column(self, column_name):
        """Remove a column from the DataFrame."""
        try:
            if column_name in self.df.columns:
                del self.df[column_name]
            else:
                print(f"Column '{column_name}' not found.")
        except Exception as e:
            print(f"Error removing column '{column_name}': {e}")
            raise

    def update_data(self, column_name, data):
        """Update the data in a specified column."""
        try:
            if column_name in self.df.columns:
                self.df[column_name] = data
            else:
                print(f"Column '{column_name}' not found.")
        except Exception as e:
            print(f"Error updating data in column '{column_name}': {e}")
            raise

    def display_data(self):
        """Display the current state of the DataFrame."""
        print(self.df)

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
    }

    # Create a DataModel instance
    model = DataModel(data)

    # Display initial data
    model.display_data()

    # Add a new column
    model.add_column("Gender", ["Female", "Male", "Male"])
    model.display_data()

    # Update data in a column
    model.update_data("Age", [26, 31, 36])
    model.display_data()

    # Remove a column
    model.remove_column("Gender")
    model.display_data()