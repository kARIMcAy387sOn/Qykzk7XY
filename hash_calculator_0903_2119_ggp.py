# 代码生成时间: 2025-09-03 21:19:17
import pandas as pd
import hashlib
from typing import Any, List

"""
哈希值计算工具

该程序使用Pandas框架和Python标准库中的hashlib模块来计算哈希值。
它提供了一个函数来计算给定值的哈希值，并支持多种哈希算法。
"""

def calculate_hash(value: Any, algorithm: str) -> str:
    """
    计算给定值的哈希值

    参数:
    value (Any): 要计算哈希值的值
    algorithm (str): 哈希算法名称，例如 'md5', 'sha256' 等

    返回:
    str: 计算得到的哈希值

    异常:
    ValueError: 如果指定的哈希算法不受支持
    """
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    # 使用hashlib模块计算哈希值
    hash_object = hashlib.new(algorithm)
    hash_object.update(str(value).encode('utf-8'))
    return hash_object.hexdigest()


def main():
    """
    主函数
    """
    # 示例用法
    test_values = [123, 'hello', [1, 2, 3]]
    algorithms = ['md5', 'sha256', 'sha1']

    for value in test_values:
        for algorithm in algorithms:
            try:
                hash_value = calculate_hash(value, algorithm)
                print(f"{value} ({algorithm}): {hash_value}")
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    main()