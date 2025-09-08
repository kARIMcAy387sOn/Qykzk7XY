# 代码生成时间: 2025-09-09 05:02:10
import pandas as pd

"""
Text File Analyzer

This program reads a text file, analyzes its content, and provides basic statistics.
"""

class TextFileAnalyzer:
    def __init__(self, file_path):
        """Initialize the analyzer with a file path."""
        self.file_path = file_path
        self.data = None

    def read_file(self):
        """Read the text file into memory."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = file.read()
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def analyze(self):
        """Analyze the text file content and return a pandas DataFrame with basic statistics."""
        if self.data is None:
            print("Error: File has not been read. Please call read_file() first.")
            return None

        # Split the text into words
        words = self.data.split()

        # Create a DataFrame with word counts
        word_counts = pd.DataFrame(list(map(lambda x: [x, words.count(x)], set(words))), columns=['Word', 'Count'])

        # Sort the DataFrame by word counts in descending order
        word_counts = word_counts.sort_values(by='Count', ascending=False).reset_index(drop=True)

        return word_counts

    def display_analysis(self):
        """Display the analysis results."""
        analysis_results = self.analyze()
        if analysis_results is not None:
            print(analysis_results)

# Example usage
if __name__ == '__main__':
    file_path = 'example.txt'
    analyzer = TextFileAnalyzer(file_path)
    analyzer.read_file()
    analyzer.display_analysis()