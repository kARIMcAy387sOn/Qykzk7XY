# 代码生成时间: 2025-10-11 01:59:24
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.exceptions import NotFittedError

# Function to load data from a CSV file
def load_data(filepath):
    """
    Load dataset from a CSV file.
    
    Parameters:
        filepath (str): The path to the CSV file.
    
    Returns:
        DataFrame: A pandas DataFrame containing the dataset.
    """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in CSV file.")
        return None
    except pd.errors.ParserError:
        print("Error parsing CSV file.")
        return None

# Function to perform standard scaling
def scale_data(data):
    """
    Scale the data using StandardScaler.
    
    Parameters:
        data (DataFrame): The dataset to scale.
    
    Returns:
        DataFrame: The scaled dataset.
    """
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

# Function to perform K-Means clustering
def perform_kmeans(data, n_clusters):
    """
    Perform K-Means clustering on the dataset.
    
    Parameters:
        data (DataFrame): The dataset to perform clustering on.
        n_clusters (int): The number of clusters to form.
    
    Returns:
        DataFrame: A DataFrame with cluster labels added as a new column.
    "