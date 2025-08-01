# 代码生成时间: 2025-08-02 01:32:17
# process_manager.py

"""
A simple process manager using Python and Pandas to manage system processes.
This script provides functionalities to retrieve system processes,
filter them based on certain criteria, and display or terminate them.
"""

import psutil
import pandas as pd
from tabulate import tabulate

class ProcessManager:
    def __init__(self):
        """Initialize the ProcessManager class."""
        self.processes = self.get_all_processes()
    
    def get_all_processes(self):
        """Retrieve all running system processes and return as a Pandas DataFrame."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status', 'username', 'memory_info', 'create_time']):
            try:
                process_info = {
                    'PID': proc.info['pid'],
                    'Name': proc.info['name'],
                    'Status': proc.info['status'],
                    'Username': proc.info['username'],
                    'Memory Usage': proc.info['memory_info'].rss,  # in bytes
                    'Create Time': proc.info['create_time']
                }
                processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return pd.DataFrame(processes)
    
    def filter_processes(self, **criteria):
        """Filter processes based on given criteria."""
        filtered_processes = self.processes.copy()
        for key, value in criteria.items():
            filtered_processes = filtered_processes[filtered_processes[key] == value]
        return filtered_processes
    
    def display_processes(self, filtered_processes=None):
        """Display processes in a tabulated format."""
        if filtered_processes is None:
            filtered_processes = self.processes
        print(tabulate(filtered_processes, headers='keys', tablefmt='grid'))
    
    def terminate_process(self, pid):
        """Terminate a process by its PID."""
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait()
            print(f"Process {pid} terminated successfully.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}.")
        except psutil.AccessDenied:
            print(f"Access denied to terminate process {pid}.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage of the ProcessManager class
if __name__ == '__main__':
    pm = ProcessManager()
    print("All Running Processes:")
    pm.display_processes()
    
    # Example filter: show processes with 'python' in the name
    filtered = pm.filter_processes(Name=lambda x: 'python' in x.lower())
    print("
Python Processes:")
    pm.display_processes(filtered)
    
    # Example termination: terminate a process with PID 1234
    # pm.terminate_process(1234)
