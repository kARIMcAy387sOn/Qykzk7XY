# 代码生成时间: 2025-09-03 01:09:14
import psutil
import time
import pandas as pd

"""
系统性能监控工具

这个程序使用psutil库来监控系统性能，包括CPU, 内存和磁盘使用情况。
它将收集的性能数据存储在Pandas DataFrame中，并可以选择性地保存为CSV文件。
"""

class SystemPerformanceMonitor:
    def __init__(self):
        """初始化性能监控工具"""
        self.data = []

    def collect_data(self, interval=1, duration=60):
        """
        收集系统性能数据
        :param interval: 收集数据的时间间隔，单位秒
        :param duration: 收集数据的总时长，单位秒
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            swap_memory = psutil.swap_memory()
            disk_usage = psutil.disk_usage('/')
            self.data.append({
                'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                'CPU Usage': cpu_usage,
                'Memory Used': memory.used / memory.total * 100,
                'Memory Total': memory.total,
                'Swap Memory Used': swap_memory.used / swap_memory.total * 100,
                'Disk Used': disk_usage.used / disk_usage.total * 100,
                'Disk Total': disk_usage.total
            })
            time.sleep(interval)

    def save_data(self, file_path='system_performance.csv'):
        """
        将收集的数据保存为CSV文件
        :param file_path: 文件保存路径
        """
        try:
            df = pd.DataFrame(self.data)
            df.to_csv(file_path, index=False)
            print(f'数据已保存到{file_path}')
        except Exception as e:
            print(f'保存数据时发生错误: {e}')

    def display_data(self):
        """显示收集的数据"""
        df = pd.DataFrame(self.data)
        print(df)

# 示例用法
if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    monitor.collect_data(interval=5, duration=60)  # 每5秒收集一次数据，共收集60秒
    monitor.display_data()  # 显示收集的数据
    monitor.save_data()  # 保存数据到CSV文件