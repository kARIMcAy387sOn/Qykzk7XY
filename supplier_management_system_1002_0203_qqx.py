# 代码生成时间: 2025-10-02 02:03:10
import pandas as pd
from datetime import datetime

# SupplierManagementSystem class
class SupplierManagementSystem:
    """
    A class to manage supplier data using Pandas DataFrame.
    This system allows adding, updating, and displaying supplier information.
    """

    def __init__(self):
        # Initialize an empty DataFrame to store supplier data
        self.suppliers = pd.DataFrame(columns=["ID", "Name", "Address", "Contact", "Phone", "Email"])

    def add_supplier(self, supplier_id, name, address, contact, phone, email):
        """
        Add a new supplier to the system.
        
        Args:
            supplier_id (int): Unique supplier ID.
            name (str): Name of the supplier.
            address (str): Address of the supplier.
            contact (str): Contact person's name.
            phone (str): Contact person's phone number.
            email (str): Contact person's email address.
        """
        try:
            # Check for duplicate supplier ID
            if self.suppliers[self.suppliers['ID'] == supplier_id].empty:
                self.suppliers = self.suppliers.append(
                    {
                        "ID": supplier_id,
                        "Name": name,
                        "Address": address,
                        "Contact": contact,
                        "Phone": phone,
                        "Email": email
                    },
                    ignore_index=True
                )
                print(f"Supplier {name} added successfully.")
            else:
                print(f"Error: Supplier ID {supplier_id} already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_supplier(self, supplier_id, name=None, address=None, contact=None, phone=None, email=None):
        """
        Update an existing supplier's information.
        
        Args:
            supplier_id (int): Unique supplier ID.
            name (str, optional): New name of the supplier.
            address (str, optional): New address of the supplier.
            contact (str, optional): New contact person's name.
            phone (str, optional): New contact person's phone number.
            email (str, optional): New contact person's email address.
        """
        try:
            # Find the supplier by ID
            supplier = self.suppliers[self.suppliers['ID'] == supplier_id]
            if not supplier.empty:
                # Update fields if new values are provided
                if name:
                    supplier['Name'] = name
                if address:
                    supplier['Address'] = address
                if contact:
                    supplier['Contact'] = contact
                if phone:
                    supplier['Phone'] = phone
                if email:
                    supplier['Email'] = email

                # Update the DataFrame
                self.suppliers.update(supplier)
                print(f"Supplier {supplier_id} updated successfully.")
            else:
                print(f"Error: Supplier ID {supplier_id} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_suppliers(self):
        """
        Display all suppliers in the system.
        """
        if not self.suppliers.empty:
            print(self.suppliers)
        else:
            print("No suppliers found.")

# Example usage
if __name__ == "__main__":
    system = SupplierManagementSystem()
    # Add suppliers
    system.add_supplier(1, "Supplier A", "123 Street", "John Doe", "1234567890", "john@example.com")
    system.add_supplier(2, "Supplier B", "456 Avenue", "Jane Doe", "0987654321", "jane@example.com")
    # Update supplier
    system.update_supplier(1, address="789 Boulevard")
    # Display suppliers
    system.display_suppliers()