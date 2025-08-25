# 代码生成时间: 2025-08-25 18:43:32
import pandas as pd

# 定义数据分析器类
class DataAnalysisProcessor:
    """
    用于加载数据、执行统计分析以及输出结果的工具类。
    """

    def __init__(self, file_path: str):
        """
        初始化数据分析器，加载指定路径的数据文件。
        
        参数:
        file_path -- CSV文件的路径。
        """
        self.file_path = file_path
        self.data_frame = None
        self._load_data()

    def _load_data(self):
        """
        私有方法，用于加载CSV文件。
        """
        try:
            self.data_frame = pd.read_csv(self.file_path)
            print("数据加载成功。")
        except Exception as e:
            print(f"数据加载失败：{e}")

    def calculate_statistics(self):
        """
        计算并返回数据的描述性统计信息。
        """
        if not self.data_frame:
            print("数据未加载，请先加载数据。")
            return {}
        
        return self.data_frame.describe()

    def get_correlation_matrix(self):
        """
        获取并返回数据的相关性矩阵。
        """
        if not self.data_frame:
            print("数据未加载，请先加载数据。")
            return None
        
        return self.data_frame.corr()

    def save_statistics_to_csv(self, output_file: str):
        """
        将描述性统计信息保存到CSV文件。
        
        参数:
        output_file -- 输出CSV文件的路径。
        """
        statistics = self.calculate_statistics()
        if not statistics.empty:
            statistics.to_csv(output_file)
            print(f"统计信息已保存到：{output_file}")
        else:
            print("统计信息为空，无法保存。")

# 示例用法
if __name__ == '__main__':
    file_path = 'data.csv'  # 假设有一个名为data.csv的数据文件
    output_file = 'statistics.csv'  # 输出文件的路径
    
    processor = DataAnalysisProcessor(file_path)
    correlation_matrix = processor.get_correlation_matrix()
    print(correlation_matrix)
    processor.save_statistics_to_csv(output_file)