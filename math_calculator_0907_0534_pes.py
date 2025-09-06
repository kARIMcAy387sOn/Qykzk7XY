# 代码生成时间: 2025-09-07 05:34:41
import pandas as pd

"""
数学计算工具集
提供基本的数学运算功能，包括加法、减法、乘法和除法。
"""

class MathCalculator:
    """数学计算工具集类"""

    def __init__(self):
        """初始化方法，无需参数"""
        pass

    def add(self, a, b):
        """加法运算

        Args:
            a (int or float): 第一个数
            b (int or float): 第二个数

        Returns:
            float: 两个数的和

        Raises:
            TypeError: 如果输入不是数字类型
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both inputs must be numerical values")
        return a + b

    def subtract(self, a, b):
        """减法运算

        Args:
            a (int or float): 第一个数
            b (int or float): 第二个数

        Returns:
            float: 两个数的差

        Raises:
            TypeError: 如果输入不是数字类型
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both inputs must be numerical values")
        return a - b

    def multiply(self, a, b):
        """乘法运算

        Args:
            a (int or float): 第一个数
            b (int or float): 第二个数

        Returns:
            float: 两个数的积

        Raises:
            TypeError: 如果输入不是数字类型
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both inputs must be numerical values")
        return a * b

    def divide(self, a, b):
        """除法运算

        Args:
            a (int or float): 被除数
            b (int or float): 除数

        Returns:
            float: 两个数的商

        Raises:
            TypeError: 如果输入不是数字类型
            ZeroDivisionError: 如果除数为零
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both inputs must be numerical values")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

# 示例用法
if __name__ == '__main__':
    calculator = MathCalculator()
    print("5 + 3 =", calculator.add(5, 3))
    print("5 - 3 =", calculator.subtract(5, 3))
    print("5 * 3 =", calculator.multiply(5, 3))
    try:
        print("5 / 0 =", calculator.divide(5, 0))
    except ZeroDivisionError as e:
        print("Error:", e)