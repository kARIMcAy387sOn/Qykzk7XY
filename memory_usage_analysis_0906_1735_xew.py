# 代码生成时间: 2025-09-06 17:35:13
import psutil
import pandas as pd
from datetime import datetime

# 获取系统内存使用情况的函数
def get_memory_usage():
    try:
        # 使用psutil获取内存使用情况
        mem = psutil.virtual_memory()
        return mem.used, mem.percent
    except Exception as e:
        # 错误处理
        print(f"Error retrieving memory usage: {e}")
        return None, None

# 将内存使用情况存储为DataFrame的函数
def store_memory_usage_as_df(start_time):
    memory_usage_records = []
    for _ in range(10):  # 假设我们需要记录10次内存使用情况
        used_memory, percent_used = get_memory_usage()
        if used_memory is not None:
            # 记录时间戳和内存使用情况
            memory_usage_records.append({
                'timestamp': datetime.now(),
                'used_memory': used_memory,
                'percent_used': percent_used
            })

    return pd.DataFrame(memory_usage_records)

# 分析内存使用情况并打印结果的函数
def analyze_memory_usage(df):
    if df.empty:
        print("No memory usage data to analyze.")
        return

    # 打印总的内存使用情况
    print("Total memory usage:
", df)

    # 分析并打印内存使用的趋势
    print("
Memory usage trend:
")
    print(df.describe())

# 主函数，执行内存使用情况分析
def main():
    start_time = datetime.now()
    print("Starting memory usage analysis...")

    # 存储内存使用情况到DataFrame
    df = store_memory_usage_as_df(start_time)

    # 分析内存使用情况
    analyze_memory_usage(df)

    print("Memory usage analysis completed at", datetime.now())

if __name__ == '__main__':
    main()