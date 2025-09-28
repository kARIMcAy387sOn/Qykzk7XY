# 代码生成时间: 2025-09-28 20:03:58
import pandas as pd
import numpy as np
from scipy.integrate import quad

"""
数值积分计算器

该程序使用Python和Pandas框架实现数值积分计算器功能。
它支持使用scipy库的quad函数进行数值积分。
"""


class NumericalIntegrationCalculator:
    def __init__(self, function, a, b):
        """
        构造函数
        
        参数:
        function (callable): 要积分的函数，接受一个参数
        a (float): 积分下限
        b (float): 积分上限
        """
        self.function = function
        self.a = a
        self.b = b

    def integrate(self):
        """
        执行数值积分
        
        返回:
        float: 积分结果
        """
        try:
            # 使用scipy库的quad函数进行数值积分
            result, error = quad(self.function, self.a, self.b)
            if error > 1e-6:
                raise ValueError("积分结果误差过大")
            return result
        except Exception as e:
            # 处理积分过程中出现的异常
            print(f"积分过程中出现异常: {e}")
            return None

    def get_integral_result(self):
        """
        获取积分结果
        
        返回:
        float: 积分结果
        """
        result = self.integrate()
        if result is not None:
            print(f"积分结果: {result}")
        else:
            print("积分失败")
        return result

# 示例用法
if __name__ == "__main__":
    # 定义要积分的函数
    def example_function(x):
        return x**2
    
    # 创建数值积分计算器实例
    calculator = NumericalIntegrationCalculator(example_function, 0, 1)
    
    # 执行积分并获取结果
    result = calculator.get_integral_result()
