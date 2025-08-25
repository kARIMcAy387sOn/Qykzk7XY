# 代码生成时间: 2025-08-26 03:22:59
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import widgets

"""
Interactive Chart Generator

This program allows users to interactively select data from a pandas DataFrame
and generate charts based on their selections.
"""

class InteractiveChartGenerator:
    """Class to generate interactive charts from pandas DataFrame."""

    def __init__(self, dataframe):
        """Initialize the InteractiveChartGenerator with a pandas DataFrame."""
        self.dataframe = dataframe

    def show(self):
        """Display the interactive chart."""
        try:
            fig, ax = plt.subplots()
            # Set up the initial plot with dummy data
            ax.plot(self.dataframe.index, self.dataframe.iloc[:, 0])
            
            # Define the callback function for the slider
            def update(val):
                "Update the plot based on the slider value."
                ax.clear()
                ax.plot(self.dataframe.index, self.dataframe.iloc[:, int(val)])
                plt.draw()
            
            # Create a slider to select the column index
            axcolor = 'lightgoldenrodyellow'
            ax_slider = plt.axes([0.1, 0.01, 0.8, 0.03], facecolor=axcolor)
            slider = widgets Slider(ax=ax_slider, label='Select Column', valmin=0, valmax=len(self.dataframe.columns)-1, valinit=0)
            slider.on_changed(update)
            
            plt.show()
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_data(self, file_path):
        """Load data from a file into the DataFrame."""
        try:
            self.dataframe = pd.read_csv(file_path)
        except Exception as e:
            print(f"Failed to load data: {e}")

# Example usage
if __name__ == '__main__':
    generator = InteractiveChartGenerator(pd.DataFrame())
    file_path = input("Enter the path to the data file: ")
    generator.load_data(file_path)
    generator.show()