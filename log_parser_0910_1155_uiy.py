# 代码生成时间: 2025-09-10 11:55:19
import pandas as pd
import re
from datetime import datetime

"""
日志文件解析工具

该工具用于解析日志文件，并提取特定格式的日志数据。
它将日志文件读入Pandas DataFrame，并提供数据清洗和转换功能。
"""

class LogParser:
    def __init__(self, filename):
        """
        初始化LogParser对象
        :param filename: 日志文件路径
        """
        self.filename = filename
        self.df = None

    def read_log_file(self):
        """
        读取日志文件
        """
        try:
            with open(self.filename, 'r') as file:
                self.df = file.readlines()
        except FileNotFoundError:
            print(f"错误：文件{self.filename}未找到。")
        except Exception as e:
            print(f"读取文件时发生错误：{e}")

    def parse_log_data(self, pattern):
        """
        解析日志数据
        :param pattern: 日志行的正则表达式
        """
        if self.df is None:
            print("日志文件未读取，请先调用read_log_file方法。")
            return

        try:
            self.df = pd.DataFrame(self.df)
            self.df['parsed'] = self.df[0].apply(lambda x: re.search(pattern, x).groupdict())
        except Exception as e:
            print(f"解析日志时发生错误：{e}")

    def to_datetime(self, date_column, time_column):
        """
        将日期和时间列转换为datetime
        :param date_column: 日期列名
        :param time_column: 时间列名
        """
        if self.df is None or 'parsed' not in self.df.columns:
            print("日志数据未解析，请先调用parse_log_data方法。")
            return

        self.df['datetime'] = pd.to_datetime(self.df[date_column] + ' ' + self.df[time_column])

    def save_to_csv(self, output_filename):
        """
        将解析后的日志数据保存为CSV文件
        :param output_filename: 输出CSV文件名
        """
        if self.df is None or 'datetime' not in self.df.columns:
            print("日志数据未转换为datetime，无法保存。")
            return

        try:
            self.df.to_csv(output_filename, index=False)
            print(f"日志数据已保存为{output_filename}。")
        except Exception as e:
            print(f"保存文件时发生错误：{e}")

# 示例用法
if __name__ == '__main__':
    log_parser = LogParser('example.log')
    log_parser.read_log_file()
    log_parser.parse_log_data(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (.*)')
    log_parser.to_datetime('date', 'time')
    log_parser.save_to_csv('parsed_log.csv')