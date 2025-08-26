# 代码生成时间: 2025-08-26 18:57:27
import psutil
import pandas as pd

"""
系统性能监控工具
使用PYTHON和PANDAS框架实现系统性能监控，包括CPU、内存、磁盘和网络状态。
"""

class SystemPerformanceMonitor:
    """系统性能监控类"""

    def __init__(self):
        """初始化方法"""
        pass

    def get_cpu_usage(self):
        """获取CPU使用率"""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return cpu_usage
        except Exception as e:
            print(f"Error getting CPU usage: {e}")
            return None

    def get_memory_usage(self):
        """获取内存使用情况"""
        try:
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            return memory_usage
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None

    def get_disk_usage(self):
        """获取磁盘使用情况"""
        try:
            disk_usage = psutil.disk_usage('/')
            disk_usage_percentage = disk_usage.percent
            return disk_usage_percentage
        except Exception as e:
            print(f"Error getting disk usage: {e}")
            return None

    def get_network_usage(self):
        """获取网络使用情况"""
        try:
            network_io = psutil.net_io_counters()
            network_sent = network_io.bytes_sent
            network_recv = network_io.bytes_recv
            return network_sent, network_recv
        except Exception as e:
            print(f"Error getting network usage: {e}")
            return None, None

    def monitor_system_performance(self):
        """监控系统性能"""
        try:
            cpu_usage = self.get_cpu_usage()
            memory_usage = self.get_memory_usage()
            disk_usage = self.get_disk_usage()
            network_sent, network_recv = self.get_network_usage()

            # 创建DataFrame存储系统性能数据
            data = {
                'CPU Usage': [cpu_usage],
                'Memory Usage': [memory_usage],
                'Disk Usage': [disk_usage],
                'Network Sent': [network_sent],
                'Network Received': [network_recv]
            }
            df = pd.DataFrame(data)

            # 打印系统性能数据
            print(df)

            return df
        except Exception as e:
            print(f"Error monitoring system performance: {e}")
            return None

# 示例用法
if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    system_performance_df = monitor.monitor_system_performance()
    if system_performance_df is not None:
        print('System performance data:')
        print(system_performance_df)