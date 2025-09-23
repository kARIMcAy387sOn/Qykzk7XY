# 代码生成时间: 2025-09-24 01:02:31
import pandas as pd
import numpy as np
import random

"""
Random Number Generator Program

This program generates random numbers using the numpy and random libraries.
It demonstrates the use of pandas for dataframe creation and manipulation.
"""

def generate_random_numbers(n, lower_bound, upper_bound):
    """
    Generate 'n' random numbers within the specified range.
    
    Args:
    n (int): The number of random numbers to generate.
    lower_bound (int): The lower bound of the range.
    upper_bound (int): The upper bound of the range.    
    
    Returns:
    pd.DataFrame: A dataframe containing the generated random numbers.
    
    Raises:
    ValueError: If 'n' is less than 1 or if the lower bound is greater than the upper bound.
    """
    if n < 1:
        raise ValueError("The number of random numbers must be at least 1.")
    if lower_bound > upper_bound:
        raise ValueError("The lower bound must be less than or equal to the upper bound.")

    # Generate 'n' random numbers within the specified range
    random_numbers = np.random.randint(lower_bound, upper_bound + 1, size=n)
    
    # Create a pandas dataframe to store the random numbers
    df = pd.DataFrame(random_numbers, columns=['Random_Numbers'])
    
    return df


# Example usage
if __name__ == '__main__':
    try:
        n = 10  # Number of random numbers to generate
        lower_bound = 1  # Lower bound of the range
        upper_bound = 100  # Upper bound of the range
        
        df = generate_random_numbers(n, lower_bound, upper_bound)
        print("Generated Random Numbers:")
        print(df)
    except ValueError as e:
        print(f"Error: {e}")