# 代码生成时间: 2025-10-07 23:15:44
import pandas as pd

"""
A simple decentralized application using Python and Pandas framework.
This app simulates a basic decentralized ledger with user transactions.
"""

# Define a class to represent a transaction
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.amount}"

# Define a class to represent the decentralized ledger
class DecentralizedLedger:
    def __init__(self):
        self.ledger = []

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the ledger.
        :param transaction: An instance of the Transaction class.
        """
        try:
            if transaction.sender == transaction.receiver:
                raise ValueError("Sender and receiver cannot be the same.")
            if transaction.amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.ledger.append(transaction)
        except ValueError as err:
            print(f"Error: {err}")

    def get_ledger(self):
        """
        Returns a DataFrame with all transactions in the ledger.
        """
        transactions_data = [
            {
                "sender": tx.sender,
                "receiver": tx.receiver,
                "amount": tx.amount
            } for tx in self.ledger
        ]
        return pd.DataFrame(transactions_data)

    def display_ledger(self):
        """
        Displays the ledger in a human-readable format.
        """
        ledger_df = self.get_ledger()
        print(ledger_df)

# Create an instance of the decentralized ledger
ledger = DecentralizedLedger()

# Test the decentralized ledger with some transactions
try:
    ledger.add_transaction(Transaction("Alice", "Bob", 100))
    ledger.add_transaction(Transaction("Bob", "Charlie", 50))
    ledger.add_transaction(Transaction("Charlie", "Alice", 75))
except ValueError as err:
    print(f"Error adding transaction: {err}")

# Display the ledger
ledger.display_ledger()