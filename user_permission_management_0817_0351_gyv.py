# 代码生成时间: 2025-08-17 03:51:01
import pandas as pd

"""
用户权限管理系统
"""

class UserPermission:
    """
    用户权限管理类
    """
    def __init__(self):
        """
        初始化方法
        """
        self.users = []  # 存储用户信息
        self.permissions = []  # 存储权限信息

    def add_user(self, username, password):
        """
        添加用户
        :param username: 用户名
        :param password: 密码
        """
        for user in self.users:
            if user['username'] == username:
                raise ValueError("用户已存在")
        self.users.append({'username': username, 'password': password, 'permissions': []})

    def add_permission(self, permission_name):
        """
        添加权限
        :param permission_name: 权限名称
        """
        for permission in self.permissions:
            if permission['name'] == permission_name:
                raise ValueError("权限已存在")
        self.permissions.append({'name': permission_name})

    def assign_permission(self, username, permission_name):
        """
        为用户分配权限
        :param username: 用户名
        :param permission_name: 权限名称
        """
        user = self.get_user(username)
        permission = self.get_permission(permission_name)
        if user and permission:
            user['permissions'].append(permission['name'])
        else:
            raise ValueError("用户或权限不存在")

    def remove_permission(self, username, permission_name):
        """
        移除用户的权限
        :param username: 用户名
        :param permission_name: 权限名称
        """
        user = self.get_user(username)
        if user:
            if permission_name in user['permissions']:
                user['permissions'].remove(permission_name)
            else:
                raise ValueError("权限不存在")
        else:
            raise ValueError("用户不存在\)

    def get_user(self, username):
        """
        根据用户名获取用户信息
        :param username: 用户名
        :return: 用户信息
        """
        for user in self.users:
            if user['username'] == username:
                return user
        return None

    def get_permission(self, permission_name):
        """
        根据权限名称获取权限信息
        :param permission_name: 权限名称
        :return: 权限信息
        """
        for permission in self.permissions:
            if permission['name'] == permission_name:
                return permission
        return None

    def list_users(self):
        """
        列出所有用户
        """
        return pd.DataFrame(self.users)

    def list_permissions(self):
        """
        列出所有权限
        """
        return pd.DataFrame(self.permissions)

# 示例用法
if __name__ == '__main__':
    permission_manager = UserPermission()
    permission_manager.add_user('admin', 'password123')
    permission_manager.add_user('user1', 'password1')
    permission_manager.add_permission('read')
    permission_manager.add_permission('write')
    permission_manager.assign_permission('admin', 'read')
    permission_manager.assign_permission('admin', 'write')
    print(permission_manager.list_users())
    print(permission_manager.list_permissions())