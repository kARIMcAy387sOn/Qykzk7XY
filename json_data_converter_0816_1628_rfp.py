# 代码生成时间: 2025-08-16 16:28:07
import pandas as pd
import json

"""
JSON数据格式转换器

该程序可以将JSON数据转换为Pandas DataFrame，并支持将DataFrame转换回JSON格式。
提供错误处理和文档注释，遵循PYTHON最佳实践。
"""

def json_to_dataframe(json_data):
    """
    将JSON数据转换为Pandas DataFrame
    
    参数:
    json_data (str): JSON格式的字符串
    
    返回:
    pd.DataFrame: DataFrame对象
    
    异常:
    ValueError: 当JSON数据无效时抛出
    """
    try:
        data = json.loads(json_data)
        return pd.DataFrame(data)
    except json.JSONDecodeError as e:
        raise ValueError("无效的JSON数据") from e


def dataframe_to_json(dataframe, orient='records'):
    """
    将Pandas DataFrame转换为JSON格式字符串
    
    参数:
    dataframe (pd.DataFrame): DataFrame对象
    orient (str): JSON输出格式，可选值包括'records', 'split', 'index'等，默认为'records'
    
    返回:
    str: JSON格式的字符串
    """
    try:
        return dataframe.to_json(orient=orient)
    except Exception as e:
        raise ValueError("DataFrame转换为JSON失败