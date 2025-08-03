# 代码生成时间: 2025-08-04 04:11:27
import psutil
import pandas as pd
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(filename='system_performance.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

"""
系统性能监控工具

该程序使用psutil库监控系统性能，包括CPU和内存使用情况，并将结果存储在DataFrame中。

Attributes:
    None

Methods:
    get_system_performance_data(): 获取系统性能数据
    save_data_to_csv(data): 将数据保存到CSV文件
    monitor_performance(interval): 监控系统性能
"""

class SystemPerformanceMonitor:
    def __init__(self):
        """初始化监控工具"""
        self.cpu_usage = []
        self.memory_usage = []

    def get_system_performance_data(self):
        """获取系统性能数据
        
        Returns:
            tuple: 包含CPU使用率和内存使用率的元组
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            return cpu_usage, memory_usage
        except Exception as e:
            logging.error(f'获取系统性能数据失败: {e}')
            return None, None

    def save_data_to_csv(self, data):
        """将数据保存到CSV文件
        
        Args:
            data (dict): 包含CPU和内存使用率的数据字典
        """
        try:
            df = pd.DataFrame(data, index=[0])
            df.to_csv('system_performance.csv', index=False)
        except Exception as e:
            logging.error(f'保存数据到CSV失败: {e}')

    def monitor_performance(self, interval):
        "