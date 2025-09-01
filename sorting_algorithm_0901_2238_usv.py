# 代码生成时间: 2025-09-01 22:38:51
import pandas as pd

"""
Module for sorting algorithms using Python and Pandas.

This module includes functions for various sorting algorithms, such as bubble sort,
selection sort, and insertion sort, using Pandas DataFrames for
demonstration purposes.
"""

# Define a function for Bubble Sort
def bubble_sort(data):
    """Sorts a list of data using the Bubble Sort algorithm.

    Args:
        data (list): The list of data to be sorted.

    Returns:
        list: The sorted list of data.
    """
    n = len(data)
    for i in range(n):
        # Flag to detect any swap
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return data

# Define a function for Selection Sort
def selection_sort(data):
    """Sorts a list of data using the Selection Sort algorithm.

    Args:
        data (list): The list of data to be sorted.

    Returns:
        list: The sorted list of data.
    """
    n = len(data)
    for i in range(n):
        # Find the minimum element in unsorted array
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] > data[j]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# Define a function for Insertion Sort
def insertion_sort(data):
    """Sorts a list of data using the Insertion Sort algorithm.

    Args:
        data (list): The list of data to be sorted.

    Returns:
        list: The sorted list of data.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Example usage with Pandas DataFrame
if __name__ == '__main__':
    # Create a sample DataFrame
    data = {'numbers': [64, 34, 25, 12, 22, 11, 90]}
    df = pd.DataFrame(data)
    print("Original DataFrame:",
          df)

    # Convert DataFrame to list and sort
    sorted_data = bubble_sort(df['numbers'].tolist())
    df_sorted = pd.DataFrame({'sorted_numbers': sorted_data})
    print("Sorted DataFrame using Bubble Sort:",
          df_sorted)

    # Convert DataFrame to list and sort using Selection Sort
    sorted_data = selection_sort(df['numbers'].tolist())
    df_sorted = pd.DataFrame({'sorted_numbers': sorted_data})
    print("Sorted DataFrame using Selection Sort:",
          df_sorted)

    # Convert DataFrame to list and sort using Insertion Sort
    sorted_data = insertion_sort(df['numbers'].tolist())
    df_sorted = pd.DataFrame({'sorted_numbers': sorted_data})
    print("Sorted DataFrame using Insertion Sort:",
          df_sorted)