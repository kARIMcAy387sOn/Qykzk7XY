# 代码生成时间: 2025-08-20 10:27:34
import pandas as pd

"""
Shopping Cart Implementation using Python and Pandas.
This module provides a simple shopping cart functionality allowing users to
add, remove, and view items in their cart.
"""


class ShoppingCart:
    def __init__(self):
        """Initialize the shopping cart with an empty DataFrame."""
        self.cart = pd.DataFrame(columns=['Product', 'Quantity', 'Price'])

    def add_item(self, product, quantity, price):
        """Add an item to the shopping cart."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        self.cart = self.cart.append(
            {'Product': product, 'Quantity': quantity, 'Price': price},
            ignore_index=True
        )

    def remove_item(self, product):
        """Remove an item from the shopping cart."""
        self.cart = self.cart[self.cart['Product'] != product]
        
    def view_cart(self):
        """View the current items in the shopping cart."""
        return self.cart

    def calculate_total(self):
        "