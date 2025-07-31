# 代码生成时间: 2025-07-31 13:33:38
import psutil
import pandas as pd
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(filename='system_performance_monitor.log', level=logging.INFO, format='%(asctime)s %(message)s')

class SystemPerformanceMonitor:
    """
    A class for monitoring system performance metrics.
    """

    def __init__(self):
        # Initialize the DataFrame to store performance data
        self.performance_data = pd.DataFrame(columns=['timestamp', 'cpu_usage', 'memory_usage', 'disk_usage', 'network_io'])

    def collect_metrics(self):
        """
        Collects system performance metrics.
        """
        try:
            # Collect CPU usage
            cpu_usage = psutil.cpu_percent()

            # Collect memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent

            # Collect disk usage
            disk_usage = psutil.disk_usage('/').percent

            # Collect network I/O
            network_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

            # Append metrics to the DataFrame
            self.performance_data = self.performance_data.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'cpu_usage': cpu_usage,
                'memory_usage': memory_usage,
                'disk_usage': disk_usage,
                'network_io': network_io,
            }, ignore_index=True)

            # Log the successful collection of metrics
            logging.info('Metrics collected successfully')
        except Exception as e:
            # Log any errors that occur during metric collection
            logging.error(f'Error collecting metrics: {e}')

    def save_metrics(self, file_name):
        """
        Saves the collected performance metrics to a CSV file.
        """
        try:
            # Save the DataFrame to a CSV file
            self.performance_data.to_csv(file_name, index=False)
            # Log the successful saving of metrics
            logging.info(f'Metrics saved to {file_name}')
        except Exception as e:
            # Log any errors that occur during file saving
            logging.error(f'Error saving metrics to file: {e}')

    def start_monitoring(self, interval=5):
        """
        Starts the monitoring process with a specified interval.
        """
        while True:
            self.collect_metrics()
            time.sleep(interval)

# Example usage
if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    monitor.start_monitoring(interval=10)  # Adjust interval as needed
