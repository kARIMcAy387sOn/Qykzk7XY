# 代码生成时间: 2025-10-12 22:07:07
import pandas as pd
from cryptography.fernet import Fernet

class DataEncryptionUtility:
    """
    A utility class for encrypting and decrypting data using the cryptography library.
    It uses symmetric encryption to ensure secure data transfer.
    """

    def __init__(self, key=None):
        """
        Initializes the DataEncryptionUtility with a key for encryption.
        If no key is provided, it generates a new one.
        """
        self.key = key or Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """
        Encrypts the provided data.
        
        Parameters:
            data (str): The data to be encrypted.
        
        Returns:
            str: The encrypted data.
        
        Raises:
            ValueError: If the data is not a string.
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        return self.cipher_suite.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the provided encrypted data.
        
        Parameters:
            encrypted_data (str): The data to be decrypted.
        
        Returns:
            str: The decrypted data.
        
        Raises:
            ValueError: If the encrypted data is not a string.
            cryptography.fernet.InvalidToken: If the encrypted data is invalid.
        """
        if not isinstance(encrypted_data, str):
            raise ValueError("Encrypted data must be a string.")
        try:
            return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
        except Exception as e:
            print("An error occurred during decryption: ", e)
            raise

    def save_key(self, file_path):
        """
        Saves the encryption key to a file.
        
        Parameters:
            file_path (str): The path to save the key.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
        except IOError as e:
            print("An error occurred while writing to file: ", e)
            raise

    def load_key(self, file_path):
        """
        Loads the encryption key from a file.
        
        Parameters:
            file_path (str): The path to load the key from.
        
        Raises:
            IOError: If there's an issue reading from the file.
        """
        try:
            with open(file_path, 'rb') as key_file:
                self.key = key_file.read()
            self.cipher_suite = Fernet(self.key)
        except IOError as e:
            print("An error occurred while reading from file: ", e)
            raise

# Example usage
if __name__ == '__main__':
    # Create an instance of the utility with a generated key
    encryption_util = DataEncryptionUtility()

    # Encrypt some data
    data = "Sensitive information"
    encrypted_data = encryption_util.encrypt_data(data)
    print("Encrypted data: ", encrypted_data)

    # Decrypt the data
    decrypted_data = encryption_util.decrypt_data(encrypted_data)
    print("Decrypted data: ", decrypted_data)

    # Save the key to a file
    encryption_util.save_key('encryption_key.key')

    # Load the key from a file (assuming it's the same instance)
    encryption_util.load_key('encryption_key.key')
