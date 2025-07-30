# 代码生成时间: 2025-07-31 06:40:08
import pandas as pd
import psutil
import os
from datetime import datetime

"""
Memory Usage Analyzer

This script analyzes the memory usage of a system using the psutil library.
It provides information about memory usage, including the total, used, and free memory,
as well as the memory usage percentage.
"""

def get_memory_usage():
    """
    Retrieves the memory usage information from the system.

    Returns:
        A dictionary containing memory usage information.
    """
    try:
        # Get memory usage statistics
        mem = psutil.virtual_memory()
        
        # Calculate memory usage percentage
        memory_usage_percent = mem.percent
        
        # Create a dictionary to store memory usage information
        memory_info = {
            "Total Memory": f"{mem.total / (1024 ** 3):.2f} GB",
            "Used Memory": f"{mem.used / (1024 ** 3):.2f} GB",
            "Free Memory": f"{mem.free / (1024 ** 3):.2f} GB",
            "Memory Usage Percentage": f"{memory_usage_percent}%",
        }
        
        return memory_info
    
    except Exception as e:
        # Handle any exceptions that occur during memory usage retrieval
        print(f"Error retrieving memory usage: {e}")
        return None


def save_memory_usage_to_csv(memory_info, output_file):
    """
    Saves the memory usage information to a CSV file.

    Args:
        memory_info (dict): A dictionary containing memory usage information.
        output_file (str): The path to the output CSV file.
    """
    try:
        # Create a Pandas DataFrame from the memory usage information
        df = pd.DataFrame([memory_info])
        
        # Save the DataFrame to a CSV file
        df.to_csv(output_file, index=False)
        
        print(f"Memory usage information saved to {output_file}")
    
    except Exception as e:
        # Handle any exceptions that occur during CSV file creation
        print(f"Error saving memory usage to CSV: {e}")


def main():
    """
    The main function that runs the memory usage analyzer.
    """
    # Get the current date and time for the output file name
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the output file path
    output_file = f"memory_usage_{current_datetime}.csv"
    
    # Get the memory usage information
    memory_info = get_memory_usage()
    
    # Check if memory usage information was retrieved successfully
    if memory_info is not None:
        # Save the memory usage information to a CSV file
        save_memory_usage_to_csv(memory_info, output_file)
    
# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()