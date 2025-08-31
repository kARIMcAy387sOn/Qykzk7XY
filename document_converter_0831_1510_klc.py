# 代码生成时间: 2025-08-31 15:10:25
import pandas as pd

"""
Document Converter
================

This script converts documents from one format to another using the pandas library.
It's designed to be easily understandable, with proper error handling,
comments, and documentation adhering to Python best practices.
"""

class DocumentConverter:
    """
    A class for converting documents from one format to another.
    """

    def __init__(self, input_path, output_path, input_format='csv', output_format='excel'):
        """
        Initialize the DocumentConverter with input and output paths and formats.
        
        :param input_path: Path to the input document.
        :param output_path: Path to the output document.
        :param input_format: Format of the input document (default is CSV).
        :param output_format: Format of the output document (default is Excel).
        """
        self.input_path = input_path
        self.output_path = output_path
        self.input_format = input_format
        self.output_format = output_format

    def convert(self):
        """
        Convert the document from the input format to the output format.
        
        :raises ValueError: If the input or output format is not supported.
        """
        try:
            # Read the input document based on its format
            if self.input_format == 'csv':
                data = pd.read_csv(self.input_path)
            elif self.input_format == 'excel':
                data = pd.read_excel(self.input_path)
            else:
                raise ValueError(f