# 代码生成时间: 2025-08-24 00:23:40
import os
# FIXME: 处理边界情况
import glob
# 改进用户体验
from PIL import Image
import pandas as pd

"""
图片尺寸批量调整器

功能：
- 读取指定文件夹中的所有图片
# 扩展功能模块
- 将图片调整为指定的尺寸
- 保存调整后的图片到指定文件夹

作者：Your Name
# 扩展功能模块
日期：2023-01-01
# TODO: 优化性能
"""

def adjust_image_size(image_path, output_path, new_width, new_height):
    """调整图片尺寸"""
# 扩展功能模块
    try:
        with Image.open(image_path) as img:
# 改进用户体验
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            resized_img.save(os.path.join(output_path, os.path.basename(image_path)))
# NOTE: 重要实现细节
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def batch_adjust_image_sizes(input_folder, output_folder, new_width, new_height):
    """批量调整图片尺寸"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_paths = glob.glob(os.path.join(input_folder, "*.*"))
    for image_path in image_paths:
        adjust_image_size(image_path, output_folder, new_width, new_height)
# 扩展功能模块

def main():
    # 输入参数
    input_folder = "input_images"
    output_folder = "output_images"
    new_width = 800
    new_height = 600

    # 执行批量调整
    batch_adjust_image_sizes(input_folder, output_folder, new_width, new_height)

if __name__ == "__main__":
    main()