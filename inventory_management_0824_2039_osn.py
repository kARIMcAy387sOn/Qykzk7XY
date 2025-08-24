# 代码生成时间: 2025-08-24 20:39:40
import pandas as pd

"""
Inventory Management System

This module provides a simple inventory management system using pandas.
It allows adding, updating, deleting, and listing inventory items.
"""

# Define the inventory DataFrame which will store the data
INVENTORY = pd.DataFrame(columns=['ID', 'Name', 'Quantity', 'Price'])


class InventoryManager:
    """
    Inventory management class providing methods to manipulate inventory data.
    """
    def __init__(self):
        """
        Initialize the InventoryManager.
        If an existing inventory CSV file exists, load it.
        """
        try:
            self.inventory_df = pd.read_csv('inventory.csv')
        except FileNotFoundError:
            self.inventory_df = INVENTORY
            print("No existing inventory data found. Starting with an empty inventory.")
        except pd.errors.EmptyDataError:
            self.inventory_df = INVENTORY
            print("Existing inventory data is empty. Starting with an empty inventory.")
        except Exception as e:
            print(f"An error occurred while loading inventory data: {e}")
            self.inventory_df = INVENTORY

    def add_item(self, item_id, name, quantity, price):
        """
        Adds a new item to the inventory.
        """
        new_item = {'ID': item_id, 'Name': name, 'Quantity': quantity, 'Price': price}
        self.inventory_df = pd.concat([self.inventory_df, pd.DataFrame([new_item])])
        self.save_inventory()
        print(f"Item {name} added successfully.")

    def update_item(self, item_id, quantity=None, price=None):
        """
        Updates an existing item in the inventory.
        """
        try:
            row = self.inventory_df[self.inventory_df['ID'] == item_id]
            if quantity is not None:
                row['Quantity'] = quantity
            if price is not None:
                row['Price'] = price
            self.inventory_df = pd.concat([self.inventory_df.drop(self.inventory_df[self.inventory_df['ID'] == item_id].index), row])
            self.save_inventory()
            print(f"Item {item_id} updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating item {item_id}: {e}")

    def delete_item(self, item_id):
        """
        Deletes an item from the inventory.
        """
        try:
            self.inventory_df = self.inventory_df.drop(self.inventory_df[self.inventory_df['ID'] == item_id].index)
            self.save_inventory()
            print(f"Item {item_id} deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting item {item_id}: {e}")

    def list_items(self):
        """
        Lists all items in the inventory.
        """
        print(self.inventory_df)

    def save_inventory(self):
        """
        Saves the current inventory state to a CSV file.
        """
        try:
            self.inventory_df.to_csv('inventory.csv', index=False)
        except Exception as e:
            print(f"An error occurred while saving inventory data: {e}")

# Example usage
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('001', 'Apple', 100, 0.50)
    manager.add_item('002', 'Banana', 150, 0.30)
    manager.update_item('001', quantity=120)
    manager.delete_item('002')
    manager.list_items()