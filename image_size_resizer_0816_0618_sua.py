# 代码生成时间: 2025-08-16 06:18:41
import os
import sys
from PIL import Image
import pandas as pd

"""
图片尺寸批量调整器
"""

class ImageResizer:
    def __init__(self, input_folder, output_folder, target_size):
        """
        初始化图片尺寸批量调整器
        :param input_folder: 输入文件夹路径
        :param output_folder: 输出文件夹路径
        :param target_size: 目标尺寸 (宽, 高)
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.target_size = target_size

    def resize_images(self):
        """
        批量调整图片尺寸
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        files = os.listdir(self.input_folder)
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                try:
                    input_path = os.path.join(self.input_folder, file)
                    output_path = os.path.join(self.output_folder, file)
                    self._resize_image(input_path, output_path)
                except Exception as e:
                    print(f"Error resizing {file}: {e}")
            else:
                print(f"Skipping non-image file {file}")

    def _resize_image(self, input_path, output_path):
        """
        调整单个图片尺寸
        :param input_path: 输入图片路径
        :param output_path: 输出图片路径
        """
        with Image.open(input_path) as img:
            img = img.resize(self.target_size, Image.ANTIALIAS)
            img.save(output_path)

    def generate_report(self):
        """
        生成调整尺寸报告
        """
        report = []
        files = os.listdir(self.input_folder)
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                input_path = os.path.join(self.input_folder, file)
                with Image.open(input_path) as img:
                    original_size = img.size
                output_path = os.path.join(self.output_folder, file)
                with Image.open(output_path) as img:
                    resized_size = img.size
                report.append({
                    'File': file,
                    'Original Size': f"{original_size[0]}x{original_size[1]}",
                    'Resized Size': f"{resized_size[0]}x{resized_size[1]}"
                })
        df = pd.DataFrame(report)
        df.to_csv('resize_report.csv', index=False)


if __name__ == '__main__':
    # 输入和输出文件夹路径
    input_folder = 'input_images'
    output_folder = 'resized_images'
    # 目标尺寸 (宽, 高)
    target_size = (800, 600)
    
    try:
        resizer = ImageResizer(input_folder, output_folder, target_size)
        resizer.resize_images()
        resizer.generate_report()
        print('Image resizing completed successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')