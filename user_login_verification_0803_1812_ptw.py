# 代码生成时间: 2025-08-03 18:12:00
import pandas as pd
from getpass import getpass

"""
用户登录验证系统
"""

class UserLoginSystem:
    def __init__(self):
        # 假设用户数据保存在一个CSV文件中
        self.user_data = pd.read_csv('users.csv')
        """
        用户数据CSV文件的格式：
        username, password
        """

    def verify_user(self, username, password):
        """
        验证用户登录信息
        :param username: 用户名
        :param password: 密码
        :return: 登录成功返回True，否则返回False
        """
        try:
            # 在用户数据中查找匹配的用户名和密码
            user_info = self.user_data[(self.user_data['username'] == username) & (self.user_data['password'] == password)]
            if not user_info.empty:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error verifying user: {e}")
            return False

    def login(self):
        """
        用户登录流程，提示输入用户名和密码
        """
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        
        if self.verify_user(username, password):
            print("Login successful!")
        else:
            print("Invalid username or password.")

# 示例用法
if __name__ == '__main__':
    login_system = UserLoginSystem()
    login_system.login()