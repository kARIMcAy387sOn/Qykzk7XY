# 代码生成时间: 2025-08-25 08:54:07
import pandas as pd

"""
User Authentication module

This module provides a simple user authentication system using pandas dataframe to store user credentials.
"""

class UserAuthentication:
    """
    Class responsible for user authentication.

    Attributes:
        users_df (pd.DataFrame): A pandas dataframe to store user credentials.
    """
    def __init__(self):
        # Initialize an empty dataframe to store users
        self.users_df = pd.DataFrame(columns=['username', 'password'])

    def register_user(self, username, password):
        """
        Registers a new user with the given username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users_df['username'].values:
            raise ValueError("Username already exists.")

        # Create a new row with the provided credentials and append to the dataframe
        new_user = pd.DataFrame([(username, password)], columns=['username', 'password'])
        self.users_df = pd.concat([self.users_df, new_user], ignore_index=True)

    def authenticate_user(self, username, password):
        """
        Authenticates a user with the given username and password.

        Args:
            username (str): The username to authenticate.
            password (str): The password to authenticate.

        Returns:
            bool: True if the user is authenticated, False otherwise.
        """
        # Check if the username and password match an existing user in the dataframe
        auth_result = self.users_df.loc[(self.users_df['username'] == username) & (self.users_df['password'] == password)]
        return len(auth_result) > 0

# Example usage
if __name__ == '__main__':
    # Create an instance of the UserAuthentication class
    auth_system = UserAuthentication()

    # Register some users
    try:
        auth_system.register_user('user1', 'password1')
        auth_system.register_user('user2', 'password2')
    except ValueError as e:
        print(e)

    # Authenticate a user
    user_authenticated = auth_system.authenticate_user('user1', 'password1')
    print(f'User Authenticated: {user_authenticated}')
