# 代码生成时间: 2025-08-09 07:32:22
import os
import zipfile
import tarfile
from pathlib import Path

"""
A utility script for decompressing files using Python's zipfile and tarfile libraries.
This script can handle .zip and .tar.gz files.
"""

class FileDecompressor:
    def __init__(self, source_file: str, destination_folder: str):
        """
        Initialize the FileDecompressor with the source file and destination folder.
        :param source_file: The path to the file to be decompressed.
        :param destination_folder: The path to the folder where the decompressed files will be placed.
        ensure it exists before initializing this class.
        """
        self.source_file = source_file
        self.destination_folder = destination_folder

    def decompress(self):
        """
        Decompress the file to the specified destination folder.
        """
        if not os.path.exists(self.source_file):
            raise FileNotFoundError(f"The source file {self.source_file} does not exist.")
        
        if not os.path.exists(self.destination_folder):
            raise FileNotFoundError(f"The destination folder {self.destination_folder} does not exist.")
        
        if self.source_file.endswith('.zip'):
            self._decompress_zip()
        elif self.source_file.endswith('.tar.gz') or self.source_file.endswith('.tgz'):
            self._decompress_tar_gz()
        else:
            raise ValueError(f"Unsupported file format: {self.source_file}")
        
    def _decompress_zip(self):
        """
        Decompress a .zip file.
        """
        with zipfile.ZipFile(self.source_file, 'r') as zip_ref:
            zip_ref.extractall(self.destination_folder)
            print(f"Decompressed {self.source_file} to {self.destination_folder}")
        
    def _decompress_tar_gz(self):
        """
        Decompress a .tar.gz file.
        """
        with tarfile.open(self.source_file, 'r:gz') as tar_ref:
            tar_ref.extractall(self.destination_folder)
            print(f"Decompressed {self.source_file} to {self.destination_folder}")

# Example usage
if __name__ == '__main__':
    src_file_path = 'path_to_your_file.zip'
    dst_folder_path = 'path_to_your_destination_folder'
    try:
        decompressor = FileDecompressor(src_file_path, dst_folder_path)
        decompressor.decompress()
    except Exception as e:
        print(f"An error occurred: {e}")