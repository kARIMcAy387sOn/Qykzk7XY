# 代码生成时间: 2025-10-13 20:22:58
import pandas as pd
import requests
from datetime import datetime

"""
Blockchain Explorer

This program is designed to act as a blockchain explorer, allowing users to query
blockchain data and retrieve information about blocks and transactions.

Attributes:
    None

Methods:
    fetch_blockchain_data: Fetches blockchain data from a public API.
    display_block_info: Displays information about a specific block.
    display_transaction_info: Displays information about a specific transaction.

Example:
    >>> explorer = BlockchainExplorer()
    >>> explorer.display_block_info(123456)
    >>> explorer.display_transaction_info('your-transaction-hash')
"""

class BlockchainExplorer:
    def __init__(self):
        """
        Initializes the BlockchainExplorer class.
        """
        self.base_url = "https://blockchain.info/"
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key

    def fetch_blockchain_data(self, endpoint, params=None):
        """
        Fetches blockchain data from a public API.

        Args:
            endpoint (str): The endpoint to query (e.g., "block/", "transaction/").
            params (dict): Query parameters (e.g., block height, transaction hash).

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.RequestException: If the API request fails.
        """
        try:
            if params is None:
                params = {}
            response = requests.get(self.base_url + endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def display_block_info(self, block_height):
        """
        Displays information about a specific block.

        Args:
            block_height (int): The height of the block to retrieve.
        """
        params = {"format": "json", "height": block_height}
        data = self.fetch_blockchain_data("block/", params)
        if data is not None:
            print("Block Information:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print("Failed to retrieve block information.")

    def display_transaction_info(self, transaction_hash):
        """
        Displays information about a specific transaction.

        Args:
            transaction_hash (str): The hash of the transaction to retrieve.
        """
        params = {"format": "json", "txindex": 0}
        data = self.fetch_blockchain_data(f"rawtx/{transaction_hash}", params)
        if data is not None:
            print("Transaction Information:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print("Failed to retrieve transaction information.")

if __name__ == "__main__":
    explorer = BlockchainExplorer()
    while True:
        try:
            user_input = input("Enter a block height or transaction hash to retrieve (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            elif user_input.isdigit():
                explorer.display_block_info(int(user_input))
            else:
                explorer.display_transaction_info(user_input)
        except Exception as e:
            print(f"Error: {e}")