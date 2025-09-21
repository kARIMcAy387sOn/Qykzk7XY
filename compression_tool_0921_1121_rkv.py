# 代码生成时间: 2025-09-21 11:21:08
import os
import zipfile
import tarfile
# TODO: 优化性能
from pathlib import Path

"""
A utility for compressing and decompressing files using Python and pandas.
This tool supports ZIP and TAR archives.

Usage:
- To compress a directory into a ZIP or TAR archive, use the compress method.
- To decompress a ZIP or TAR archive into a directory, use the decompress method.
"""

class CompressionTool:
# TODO: 优化性能
    def __init__(self, archive_type='zip'):
# 扩展功能模块
        """Initialize the CompressionTool with an archive type."""
        self.archive_type = archive_type

    def compress(self, source_folder, output_file):
        """Compress a folder into an archive.
        
        Args:
        - source_folder (str): The path to the folder to compress.
        - output_file (str): The path to the output archive file.
        """
        # Check if the source folder exists
        if not Path(source_folder).is_dir():
            raise FileNotFoundError(f"The source folder '{source_folder}' does not exist.")
        
        # Create the output directory if it does not exist
        output_dir = Path(output_file).parent
# 添加错误处理
        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
        
        if self.archive_type == 'zip':
# TODO: 优化性能
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Walk through the directory and add files to the zip archive
                for root, dirs, files in os.walk(source_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=source_folder)
                        zipf.write(file_path, arcname)
        elif self.archive_type == 'tar':
            with tarfile.open(output_file, 'w:') as tar:
                # Walk through the directory and add files to the tar archive
                for root, dirs, files in os.walk(source_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=source_folder)
                        tar.add(file_path, arcname)
        else:
            raise ValueError("Unsupported archive type. Supported types are 'zip' and 'tar'.")

    def decompress(self, input_file, destination_folder):
        """Decompress an archive into a folder.
        
        Args:
        - input_file (str): The path to the archive file to decompress.
        - destination_folder (str): The path to the destination folder.
        """
# FIXME: 处理边界情况
        # Check if the input file exists
        if not Path(input_file).is_file():
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")
        
        # Create the destination directory if it does not exist
        if not Path(destination_folder).exists():
            Path(destination_folder).mkdir(parents=True)
        
        if self.archive_type == 'zip':
            with zipfile.ZipFile(input_file, 'r') as zipf:
                # Extract all files from the zip archive
                zipf.extractall(destination_folder)
        elif self.archive_type == 'tar':
            with tarfile.open(input_file, 'r:') as tar:
                # Extract all files from the tar archive
                tar.extractall(destination_folder)
        else:
            raise ValueError("Unsupported archive type. Supported types are 'zip' and 'tar'.")

# Example usage:
if __name__ == '__main__':
    tool = CompressionTool(archive_type='zip')
    # Compress a folder
    tool.compress('/path/to/source/folder', '/path/to/output.zip')
    
    # Decompress an archive
    tool.decompress('/path/to/input.zip', '/path/to/destination/folder')