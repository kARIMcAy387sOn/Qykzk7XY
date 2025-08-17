# 代码生成时间: 2025-08-18 04:42:58
import hashlib
import pandas as pd
from typing import Any, Union


def calculate_hash(data: Union[str, bytes, pd.DataFrame], algorithm: str = 'sha256') -> Union[str, pd.DataFrame]:
    '''
    Calculate the hash value of the input data using the specified algorithm.

    Parameters:
    data (Union[str, bytes, pd.DataFrame]): The input data to calculate hash for.
    algorithm (str): The hash algorithm to use (default is 'sha256').

    Returns:
    Union[str, pd.DataFrame]: The hash value of the input data as a string or a DataFrame with hash values.
    '''

    # Check if the algorithm is supported
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Supported algorithms are: {hashlib.algorithms_available}")

    # Calculate hash for string or bytes data
    if isinstance(data, (str, bytes)):
        hash_object = hashlib.new(algorithm)
        hash_object.update(data.encode() if isinstance(data, str) else data)
        return hash_object.hexdigest()

    # Calculate hash for pandas DataFrame
    elif isinstance(data, pd.DataFrame):
        result_df = pd.DataFrame(index=data.index)
        for column in data.columns:
            result_df[column] = data[column].apply(lambda x: calculate_hash(x, algorithm))
        return result_df

    else:
        raise TypeError("Unsupported data type. Data must be str, bytes, or pd.DataFrame.")


# Example usage
if __name__ == '__main__':
    data_str = "Hello, World!"
    data_bytes = b"Hello, World!"
    data_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

    print("Hash of string: ", calculate_hash(data_str))
    print("Hash of bytes: ", calculate_hash(data_bytes))
    print("Hash of DataFrame: ", calculate_hash(data_df))
