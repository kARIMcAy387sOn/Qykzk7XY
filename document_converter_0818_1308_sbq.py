# 代码生成时间: 2025-08-18 13:08:30
import pandas as pd

"""
文档格式转换器

该程序旨在将不同格式的文档转换成CSV格式以便进一步处理。
支持的文档格式包括Excel和JSON。
"""


class DocumentConverter:
    """文档转换器类"""
    def __init__(self):
        pass

    def convert_excel_to_csv(self, input_file_path, output_file_path):
        """将Excel文档转换为CSV

        Args:
            input_file_path (str): 输入Excel文件路径
            output_file_path (str): 输出CSV文件路径
        """
        try:
            # 读取Excel文件
            df = pd.read_excel(input_file_path)
            # 保存为CSV文件
            df.to_csv(output_file_path, index=False)
            print(f"文件{input_file_path}已成功转换为{output_file_path}")
        except Exception as e:
            print(f"转换Excel文件时发生错误：{e}")

    def convert_json_to_csv(self, input_file_path, output_file_path):
        """将JSON文档转换为CSV

        Args:
            input_file_path (str): 输入JSON文件路径
            output_file_path (str): 输出CSV文件路径
        """
        try:
            # 读取JSON文件
            df = pd.read_json(input_file_path)
            # 保存为CSV文件
            df.to_csv(output_file_path, index=False)
            print(f"文件{input_file_path}已成功转换为{output_file_path}")
        except Exception as e:
            print(f"转换JSON文件时发生错误：{e}")


if __name__ == '__main__':
    # 示例用法
    converter = DocumentConverter()
    input_file_path = 'example.xlsx'
    output_file_path = 'output.csv'
    converter.convert_excel_to_csv(input_file_path, output_file_path)
    
    input_file_path = 'example.json'
    output_file_path = 'output.csv'
    converter.convert_json_to_csv(input_file_path, output_file_path)