# 代码生成时间: 2025-08-11 08:03:45
import pandas as pd

"""
用户权限管理系统

该系统使用Pandas库管理用户权限数据。
提供添加、删除、更新和查询用户权限的功能。
"""

class UserPermissionManager:
    """用户权限管理类"""
    def __init__(self):
        # 初始化权限数据框架
        self.permissions = pd.DataFrame(columns=['username', 'role', 'permissions'])

    def add_user(self, username, role, permissions):
        """添加用户权限"""
        try:
            # 检查用户是否已存在
            if self.check_user_exists(username):
                raise ValueError(f"用户 {username} 已存在。")
            # 添加用户权限数据
            self.permissions = self.permissions.append(
                {'username': username, 'role': role, 'permissions': permissions}, ignore_index=True
            )
            return f"用户 {username} 添加成功。"
        except Exception as e:
            return str(e)

    def delete_user(self, username):
        """删除用户权限"""
        try:
            # 删除用户权限数据
            self.permissions = self.permissions[self.permissions['username'] != username]
            return f"用户 {username} 删除成功。"
        except Exception as e:
            return str(e)

    def update_user(self, username, role=None, permissions=None):
        """更新用户权限"""
        try:
            # 检查用户是否存在
            if not self.check_user_exists(username):
                raise ValueError(f"用户 {username} 不存在。")
            # 更新用户权限数据
            if role:
                self.permissions.loc[self.permissions['username'] == username, 'role'] = role
            if permissions:
                self.permissions.loc[self.permissions['username'] == username, 'permissions'] = permissions
            return f"用户 {username} 更新成功。"
        except Exception as e:
            return str(e)

    def query_user(self, username):
        """查询用户权限"""
        try:
            # 查询用户权限数据
            user_data = self.permissions[self.permissions['username'] == username]
            if user_data.empty:
                return f"用户 {username} 不存在。"
            return user_data.to_dict(orient='records')
        except Exception as e:
            return str(e)

    def check_user_exists(self, username):
        """检查用户是否存在"""
        return (self.permissions['username'] == username).any()

    def show_permissions(self):
        """显示所有用户权限"""
        return self.permissions.to_dict(orient='records')

# 示例用法
if __name__ == '__main__':
    manager = UserPermissionManager()
    print(manager.add_user('alice', 'admin', ['read', 'write', 'delete']))
    print(manager.add_user('bob', 'user', ['read']))
    print(manager.update_user('alice', permissions=['read', 'write']))
    print(manager.query_user('alice'))
    print(manager.delete_user('bob'))
    print(manager.show_permissions())