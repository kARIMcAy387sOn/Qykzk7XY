# 代码生成时间: 2025-08-02 12:51:25
import pandas as pd
import os
from typing import List

"""
CSV文件批量处理器

该程序旨在读取指定文件夹下的所有CSV文件，并执行一些基本操作。
支持的操作包括：
- 读取CSV文件
- 显示基本信息
- 保存CSV文件
"""

class CSVBatchProcessor:
    def __init__(self, directory: str):
        """
        初始化CSV处理器
        :param directory: CSV文件所在的目录路径
        """
        self.directory = directory

    def read_csv_files(self) -> List[pd.DataFrame]:
        """
        读取目录下的所有CSV文件
        :return: 包含所有CSV文件数据的DataFrame列表
        """
        csv_files = [f for f in os.listdir(self.directory) if f.endswith('.csv')]
        dataframes = []
        for file in csv_files:
            try:
                file_path = os.path.join(self.directory, file)
                df = pd.read_csv(file_path)
                dataframes.append(df)
                print(f'成功读取文件：{file}')
            except Exception as e:
                print(f'读取文件{file}时出错：{e}')
        return dataframes

    def display_info(self, dataframes: List[pd.DataFrame]):
        """
        显示所有DataFrame的基本信息
        :param dataframes: DataFrame列表
        """
        for i, df in enumerate(dataframes):
            print(f'文件 {i+1} 信息：')
            print(df.info())

    def save_csv_files(self, dataframes: List[pd.DataFrame]):
        """
        保存所有DataFrame到CSV文件
        :param dataframes: DataFrame列表
        """
        for i, df in enumerate(dataframes):
            try:
                file_path = os.path.join(self.directory, f'output_file_{i+1}.csv')
                df.to_csv(file_path, index=False)
                print(f'文件 {i+1} 已保存：{file_path}')
            except Exception as e:
                print(f'保存文件 {i+1} 时出错：{e}')

    def process_files(self):
        """
        处理目录下的所有CSV文件
        """
        dataframes = self.read_csv_files()
        self.display_info(dataframes)
        self.save_csv_files(dataframes)

# 示例用法
if __name__ == '__main__':
    directory = 'path/to/your/csv/files'  # 指定CSV文件所在的目录
    processor = CSVBatchProcessor(directory)
    processor.process_files()