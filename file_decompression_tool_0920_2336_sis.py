# 代码生成时间: 2025-09-20 23:36:16
import os
import zipfile
import tarfile
import gzip
from pathlib import Path

# 定义一个压缩文件解压工具类
class DecompressionTool:
    """
    该类提供了压缩文件的解压功能，支持zip、tar.gz和gzip格式。
    """

    def __init__(self, file_path):
        """
        初始化函数，设置需要解压的文件路径
        :param file_path: 文件路径
        """
        self.file_path = file_path

    def unzip(self):
        """
        unzip文件
        """
        try:
            # 使用zipfile模块解压zip文件
            with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(self.file_path))
            print("Unzipped successfully")
        except zipfile.BadZipFile:
            print("Not a zip file or it is corrupted")

    def untar(self):
        """
        untar文件
        """
        try:
            # 使用tarfile模块解压tar.gz文件
            with tarfile.open(self.file_path, 'r:gz') as tar_ref:
                tar_ref.extractall(os.path.dirname(self.file_path))
            print("Untarred successfully")
        except (tarfile.TarError, AttributeError):
            print("Not a tar file or it is corrupted")

    def ungzip(self):
        """
        ungzip文件
        """
        try:
            # 使用gzip模块解压gzip文件
            with gzip.open(self.file_path, 'rb') as gzip_ref:
                with open(self.file_path[:-3], 'wb') as out_file:
                    out_file.write(gzip_ref.read())
            print("Ungziped successfully")
        except OSError:
            print("Not a gzip file or it is corrupted")

    def decompress(self):
        """
        根据文件扩展名自动选择解压方式
        """
        # 根据文件扩展名确定解压方式
        if self.file_path.endswith('.zip'):
            self.unzip()
        elif self.file_path.endswith('.tar.gz') or self.file_path.endswith('.tgz'):
            self.untar()
        elif self.file_path.endswith('.gz'):
            self.ungzip()
        else:
            print("Unsupported file type")

# 主函数
if __name__ == '__main__':
    file_path = input("Enter the path of the compressed file: ")
    try:
        # 检查文件是否存在
        Path(file_path).is_file()
        tool = DecompressionTool(file_path)
        tool.decompress()
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")
