# 代码生成时间: 2025-09-01 10:55:20
import psutil
import pandas as pd

"""
memory_usage_analysis.py

A Python script to analyze memory usage using the psutil library and pandas framework.
"""

class MemoryAnalyzer:
    def __init__(self):
        """Initialize the MemoryAnalyzer class."""
        self.mem = psutil.virtual_memory()

    def get_memory_stats(self):
        """Get the current memory statistics."""
        return {
            'total': self.mem.total / (1024 ** 3), # Total memory in GB
            'available': self.mem.available / (1024 ** 3), # Available memory in GB
            'used': (self.mem.total - self.mem.available) / (1024 ** 3), # Used memory in GB
            'percentage': self.mem.percent, # Memory usage percentage
        }

    def analyze_memory(self):
        """Analyze the memory usage and generate a report."""
        try:
            memory_stats = self.get_memory_stats()
            df = pd.DataFrame(memory_stats, index=[0])
            print(df)
        except Exception as e:
            print(f"An error occurred: {e}")

    def to_dataframe(self):
        """Convert memory statistics to a pandas DataFrame."""
        try:
            memory_stats = self.get_memory_stats()
            return pd.DataFrame(memory_stats, index=[0])
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == '__main__':
    analyzer = MemoryAnalyzer()
    analyzer.analyze_memory()
    df = analyzer.to_dataframe()
    if df is not None:
        df.to_csv('memory_usage.csv')
        print("Memory usage report generated successfully.")
    else:
        print("Failed to generate memory usage report.")