# 代码生成时间: 2025-08-17 16:25:58
@Author: Your Name
@Date: YYYY-MM-DD
@Version: 1.0
*/

import pandas as pd
import psutil
import os
import gc

"""
Function to calculate memory usage of a dataset.

Parameters:
    filepath (str): The filepath to the dataset.

Returns:
    None. Prints the memory usage statistics.
"""
def analyze_memory_usage(filepath):
    # Initialize the memory usage
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss
    
    try:
        # Load the dataset
        df = pd.read_csv(filepath)
        print('Memory usage before loading the dataset (in bytes): {}'.format(mem_before))
        
        # Calculate the memory usage of the DataFrame
        df_info = df.info(memory_usage='deep')
        print(df_info)
        
        # Calculate the memory usage after loading the dataset
        mem_after = process.memory_info().rss
        print('Memory usage after loading the dataset (in bytes): {}'.format(mem_after))
        
        # Calculate the difference in memory usage
        mem_diff = mem_after - mem_before
        print('Difference in memory usage (in bytes): {}'.format(mem_diff))
        
    except Exception as e:
        # Handle exceptions
        print('Error loading the dataset: {}'.format(str(e)))
        
    finally:
        # Clean up memory
        del df
        gc.collect()
        process = psutil.Process(os.getpid())
        mem_after_cleanup = process.memory_info().rss
        print('Memory usage after cleaning up (in bytes): {}'.format(mem_after_cleanup))

if __name__ == '__main__':
    # Main function
    filepath = 'your_dataset.csv'  # Replace with your dataset filepath
    analyze_memory_usage(filepath)