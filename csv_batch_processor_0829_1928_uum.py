# 代码生成时间: 2025-08-29 19:28:53
import pandas as pd
import os
import glob

"""
CSV文件批量处理器

该程序用于处理指定目录下的所有CSV文件
"""

def process_csv_file(file_path):
    """处理单个CSV文件"""
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        # 这里可以添加所需的数据处理逻辑
        print(f"Processing {file_path}
{df.head()}
")
    except Exception as e:
        # 错误处理
        print(f"Error processing file {file_path}: {str(e)}")

def process_csv_files(directory):
    """处理指定目录下的所有CSV文件"""
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    if not csv_files:
        print(f"No CSV files found in {directory}.")
        return
    
    for file in csv_files:
        process_csv_file(file)

if __name__ == '__main__':
    # 使用示例
    # 替换为你的CSV文件目录
    directory = './csv_files'
    process_csv_files(directory)