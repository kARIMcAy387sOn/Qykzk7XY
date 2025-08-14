# 代码生成时间: 2025-08-14 22:32:43
import os
import glob
from PIL import Image
import pandas as pd

"""
Image Resizer: A program to batch adjust image dimensions.

This program takes a folder path, resizes all images within to a
specified width and height, and saves them in a new folder.

Attributes:
    target_width (int): The desired width for resized images.
    target_height (int): The desired height for resized images.
    folder_path (str): The path to the folder containing images to resize.
    output_folder (str): The path to the folder where resized images will be saved.
"""

class ImageResizer:
    def __init__(self, folder_path, output_folder, target_width, target_height):
        """Initialize the ImageResizer class."""
        self.folder_path = folder_path
        self.output_folder = output_folder
        self.target_width = target_width
        self.target_height = target_height
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    def resize_images(self):
        """Resize images in the specified folder."""
        # Check if the output folder exists, create it if not
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Find all image files in the specified folder
        image_files = glob.glob(os.path.join(self.folder_path, '*'))
        resized_images = []

        for file_path in image_files:
            # Check if the file is an image
            if os.path.splitext(file_path)[1].lower() in self.image_extensions:
                try:
                    # Open and resize the image
                    with Image.open(file_path) as img:
                        resized_img = img.resize((self.target_width, self.target_height))
                        # Save the resized image to the output folder
                        output_path = os.path.join(
                            self.output_folder,
                            os.path.basename(file_path)
                        )
                        resized_img.save(output_path)
                        resized_images.append(output_path)
                except Exception as e:
                    print(f"Error resizing {file_path}: {e}")

        return resized_images

    def create_report(self, resized_images):
        """Create a report of resized images."""
        df = pd.DataFrame(resized_images, columns=['Resized Images'])
        report_path = os.path.join(self.output_folder, 'resize_report.csv')
        df.to_csv(report_path, index=False)
        return report_path

# Example usage:
if __name__ == '__main__':
    folder_path = 'path_to_your_folder'  # Replace with your folder path
    output_folder = 'path_to_output_folder'  # Replace with your output folder path
    target_width = 800  # Replace with your desired width
    target_height = 600  # Replace with your desired height

    resizer = ImageResizer(folder_path, output_folder, target_width, target_height)
    resized_images = resizer.resize_images()
    report_path = resizer.create_report(resized_images)
    print(f"Resized images have been saved to {report_path}")