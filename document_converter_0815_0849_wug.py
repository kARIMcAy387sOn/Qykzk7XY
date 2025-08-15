# 代码生成时间: 2025-08-15 08:49:45
import pandas as pd

"""
A document converter program using Python and Pandas.
This program is designed to convert documents between different formats.
"""

def convert_document(input_file_path, output_file_path, input_format, output_format):
    """
    Converts a document from one format to another.
    
    Args:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to the output file.
        input_format (str): The format of the input file (e.g., 'csv', 'xlsx', 'json').
        output_format (str): The format of the output file (e.g., 'csv', 'xlsx', 'json').
    
    Raises:
        ValueError: If the input or output format is not supported.
    """
    # Check if the input and output formats are supported
    supported_formats = ['csv', 'xlsx', 'json']
    if input_format not in supported_formats or output_format not in supported_formats:
        raise ValueError("Unsupported input or output format")

    try:
        # Read the input file using Pandas
        data = pd.read_csv(input_file_path) if input_format == 'csv' else \
                  pd.read_excel(input_file_path) if input_format == 'xlsx' else \
                  pd.read_json(input_file_path)
    except Exception as e:
        # Handle any exceptions that occur during file reading
        raise Exception(f"Error reading input file: {str(e)}")

    try:
        # Write the data to the output file using Pandas
        data.to_csv(output_file_path) if output_format == 'csv' else \
         data.to_excel(output_file_path) if output_format == 'xlsx' else \
         data.to_json(output_file_path)
    except Exception as e:
        # Handle any exceptions that occur during file writing
        raise Exception(f"Error writing output file: {str(e)}")

    print("Document conversion successful")


def main():
    """
    The main function of the document converter program.
    It takes command-line arguments for input and output file paths and formats.
    """
    import sys
    
    if len(sys.argv) != 5:
        print("Usage: python document_converter.py input_file_path output_file_path input_format output_format")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    input_format = sys.argv[3]
    output_format = sys.argv[4]
    
    convert_document(input_file_path, output_file_path, input_format, output_format)

if __name__ == "__main__":
    main()