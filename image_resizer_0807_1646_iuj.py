# 代码生成时间: 2025-08-07 16:46:13
import os
import glob
from PIL import Image
import pandas as pd

"""
Image Resizer: A program to batch resize images using Python and Pandas.

This script finds all image files in a specified directory,
resizes them to a given size, and saves them in a new directory.
# NOTE: 重要实现细节
"""

class ImageResizer:
    def __init__(self, input_directory, output_directory, size):
# 优化算法效率
        """
# 改进用户体验
        Initialize the ImageResizer with input and output directories and target size.
        
        Args:
        input_directory (str): Directory containing the original images.
# 改进用户体验
        output_directory (str): Directory to save the resized images.
        size (tuple): Target size as a tuple (width, height).
        """
        self.input_directory = input_directory
        self.output_directory = output_directory
# 改进用户体验
        self.size = size

    def resize_images(self):
# NOTE: 重要实现细节
        """
# 增强安全性
        Resize all images in the input directory and save them to the output directory.
        """
        # Check if output directory exists, if not, create it
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        # Create a list to store the details of the processed images
        resized_images = []
# NOTE: 重要实现细节

        # Iterate over all image files in the input directory
        for file in glob.glob(os.path.join(self.input_directory, "*.*")):
            try:
                with Image.open(file) as img:
                    # Resize the image
# 增强安全性
                    resized_img = img.resize(self.size)
                    
                    # Generate the output filename
                    filename = os.path.basename(file)
                    output_file = os.path.join(self.output_directory, filename)
                    
                    # Save the resized image
                    resized_img.save(output_file)
                    
                    # Store the details of the processed image
                    resized_images.append({
                        "filename": filename,
                        "original_size": img.size,
                        "resized_size": resized_img.size
                    })
            except Exception as e:
# 添加错误处理
                print(f"Error resizing {file}: {e}")

        # Save the details of the resized images to a CSV file
        self.save_resized_images_details(resized_images)

    def save_resized_images_details(self, resized_images):
        """
        Save the details of the resized images to a CSV file.
        """
        df = pd.DataFrame(resized_images)
        df.to_csv(os.path.join(self.output_directory, "resized_images_details.csv"), index=False)

# Example usage:
if __name__ == "__main__":
# 扩展功能模块
    resizer = ImageResizer(
        input_directory="path/to/input/directory",
        output_directory="path/to/output/directory",
# NOTE: 重要实现细节
        size=(800, 600)  # Resize to 800x600
    )
    resizer.resize_images()
# FIXME: 处理边界情况
