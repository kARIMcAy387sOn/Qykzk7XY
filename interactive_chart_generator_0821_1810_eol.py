# 代码生成时间: 2025-08-21 18:10:45
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

"""
Interactive Chart Generator

This is a Python program that generates interactive charts using Pandas and Matplotlib.
It allows users to select data and chart types, and displays the results interactively.
"""

class InteractiveChartGenerator:
    """
    The main class responsible for generating interactive charts.
    """
    def __init__(self, data):
        """
        Initializes the chart generator with a Pandas DataFrame.
        
        Args:
        data (pd.DataFrame): The input data for the chart.
        """
        self.data = data
        self.chart_types = ["line", "bar", "pie"]
        
    def select_data(self):
        """
        Prompts the user to select data columns for the chart.
        Returns two columns (x and y) and a pivot column (optional).
        """
        try:
            x_column = input("Enter the x-axis column name: ")
            y_column = input("Enter the y-axis column name: ")
            pivot_column = input("Enter the pivot column name (optional): ")
            return x_column, y_column, pivot_column
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def select_chart_type(self):
        """
        Prompts the user to select a chart type.
        Returns the selected chart type.
        """
        try:
            print("Available chart types: ", self.chart_types)
            chart_type = input("Enter the desired chart type: ")
            if chart_type not in self.chart_types:
                print("Invalid chart type. Please select from the available options.")
                return self.select_chart_type()
            return chart_type
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def generate_chart(self, x_column, y_column, pivot_column, chart_type):
        """
        Generates the chart based on the provided parameters.
        
        Args:
        x_column (str): The x-axis column name.
        y_column (str): The y-axis column name.
        pivot_column (str): The pivot column name (optional).
        chart_type (str): The selected chart type.
        """
        try:
            if pivot_column:
                data = self.data.pivot_table(index=x_column, columns=pivot_column, values=y_column)
            else:
                data = self.data[[x_column, y_column]]

            fig, ax = plt.subplots()
            
            if chart_type == "line":
                ax.plot(data.iloc[:, 0], data.iloc[:, 1:])
            elif chart_type == "bar":
                ax.bar(data.index, data.iloc[:, 1:].sum(axis=1))
            elif chart_type == "pie":
                ax.pie(data.iloc[:, 1:].sum(axis=0), labels=data.columns[1:], autopct='%1.1f%%')
            else:
                raise ValueError("Unsupported chart type")

            plt.show()
        except Exception as e:
            print(f"Error: {e}")
    
    def run(self):
        """
        Runs the interactive chart generator.
        """
        x_column, y_column, pivot_column = self.select_data()
        chart_type = self.select_chart_type()
        if x_column and y_column and chart_type:
            self.generate_chart(x_column, y_column, pivot_column, chart_type)
        else:
            print("Invalid input. Please run the program again.")

# Example usage
if __name__ == "__main__":
    data = pd.DataFrame({
        "Category": ["A", "B", "C", "A", "B", "C"],
        "Values": [10, 20, 30, 15, 25, 35],
        "Subcategory": ["X", "X", "X", "Y", "Y", "Y"]
    })
    
    generator = InteractiveChartGenerator(data)
    generator.run()