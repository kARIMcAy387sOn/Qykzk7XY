# 代码生成时间: 2025-08-08 02:01:44
import pandas as pd
import numpy as np

"""
A module to generate random numbers using pandas and numpy.

This module contains a function to generate random numbers within a specified range.
It includes error handling to ensure the inputs are valid and the function is robust.
"""

def generate_random_numbers(min_value, max_value, count):
    """
    Generates a specified number of random numbers within a given range.
    
    Args:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.
    count (int): The number of random numbers to generate.
    
    Returns:
    pd.DataFrame: A DataFrame containing the generated random numbers.
    
    Raises:
    ValueError: If min_value is greater than max_value or if count is not a positive integer.
    """
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("count must be a positive integer")
    
    # Generate random numbers using numpy
    random_numbers = np.random.randint(min_value, max_value + 1, count)
    
    # Create a DataFrame to store the random numbers
    df = pd.DataFrame(random_numbers, columns=['Random Numbers'])
    
    return df

# Example usage
if __name__ == '__main__':
    try:
        min_val = 1
        max_val = 100
        num_numbers = 10
        result = generate_random_numbers(min_val, max_val, num_numbers)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")