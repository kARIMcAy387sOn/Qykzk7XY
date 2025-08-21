# 代码生成时间: 2025-08-21 11:44:05
import pandas as pd
import os
import glob

"""
CSV文件批量处理器

该程序用于批量处理指定目录下的所有CSV文件。
"""

class CSVBatchProcessor:
    def __init__(self, directory):
        """
        初始化CSV批量处理器
        :param directory: 要处理的CSV文件所在的目录
        """
        self.directory = directory
        
    def process_files(self):
        """
        处理目录下的所有CSV文件
        """
        try:
            # 使用glob模块查找目录下所有CSV文件
            csv_files = glob.glob(os.path.join(self.directory, '*.csv'))

            # 遍历所有找到的CSV文件
            for file_path in csv_files:
                print(f"处理文件: {file_path}")
                self.process_file(file_path)

        except Exception as e:
            # 处理可能出现的异常
            print(f"处理CSV文件时出现错误: {str(e)}")

    def process_file(self, file_path):
        """
        处理单个CSV文件
        :param file_path: CSV文件的路径
        """
        try:
            # 使用PANDAS读取CSV文件
            df = pd.read_csv(file_path)

            # 打印DataFrame的基本信息
            print(df.info())

            # 执行一些数据处理操作
            # 例如：计算每列的平均值
            mean_values = df.mean()
            print(mean_values)

            # 可以根据需要添加更多的数据处理逻辑

        except pd.errors.EmptyDataError:
            # 处理空文件的情况
            print(f"文件 {file_path} 是空的，跳过处理")
        except pd.errors.ParserError:
            # 处理解析错误的情况
            print(f"文件 {file_path} 解析错误，跳过处理")
        except Exception as e:
            # 处理其他可能的异常
            print(f"处理文件 {file_path} 时出现错误: {str(e)}")

if __name__ == '__main__':
    # 指定要处理的CSV文件所在的目录
    directory = 'path/to/your/csv/directory'

    # 创建CSV批量处理器实例
    processor = CSVBatchProcessor(directory)

    # 开始处理文件
    processor.process_files()