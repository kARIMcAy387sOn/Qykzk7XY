# 代码生成时间: 2025-10-11 23:12:24
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

"""
A Python program to create a disease prediction model using pandas and scikit-learn.
This program assumes a dataset with features that predict the presence or absence of a disease.
"""

# Define the function to load and preprocess the dataset
def load_and_preprocess_data(file_path):
    # Load the dataset into a pandas DataFrame
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
    # Handle missing values if any
    if data.isnull().values.any():
        data = data.dropna()
    
    # Separate the features and the target variable
    X = data.drop('target_column', axis=1)
    y = data['target_column']
    
    # Return the preprocessed data
    return X, y

# Define the function to train the model
def train_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Return the trained model
    return model

# Define the function to predict and evaluate the model
def predict_and_evaluate(model, X_test, y_test):
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    # Return the accuracy
    return accuracy

# Define the main function to run the program
def main():
    # Specify the file path of the dataset
    file_path = 'disease_data.csv'
    
    # Load and preprocess the data
    X, y = load_and_preprocess_data(file_path)
    if X is None or y is None:
        print('Failed to load or preprocess data.')
        return
    
    # Train the model
    model = train_model(X, y)
    
    # Split the data into test set for evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Evaluate the model
    accuracy = predict_and_evaluate(model, X_test, y_test)
    
    # Print the accuracy of the model
    print(f"Model Accuracy: {accuracy:.2f}")

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()