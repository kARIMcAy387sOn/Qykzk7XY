# 代码生成时间: 2025-09-14 03:21:05
import hashlib\
import pandas as pd\
\
"""
哈希值计算工具
"""\
\
class HashCalculator:
    """
    用于计算文件内容的哈希值的工具类
    """\
    def __init__(self):
        pass

    def calculate_hash(self, file_path):
        """
        计算给定文件的哈希值
        
        参数：
        file_path (str): 文件的路径
        
        返回：
        str: 文件的哈希值
        
        异常：
        FileNotFoundError: 文件不存在时抛出
        IOError: 文件读取错误时抛出
        """
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                return self._get_hash(content)
        except FileNotFoundError:
            raise FileNotFoundError(f"文件 {file_path} 不存在")
        except IOError as e:
            raise IOError(f"文件 {file_path} 读取错误: {e}")

    def calculate_dataframe_hash(self, df):
        """
        计算Pandas DataFrame的哈希值
        
        参数：
        df (pd.DataFrame): 要计算哈希值的DataFrame
        
        返回：
        str: DataFrame的哈希值
        """
        # 将DataFrame转换为字符串
        df_str = df.to_string()
        # 计算哈希值
        return self._get_hash(df_str.encode())

    def _get_hash(self, content):
        "