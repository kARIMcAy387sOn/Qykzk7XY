# 代码生成时间: 2025-08-29 23:30:23
import pandas as pd

class MathCalculator:
    """Class to handle basic mathematical operations."""

    def __init__(self):
        pass

    def add(self, x, y):
        """Add two numbers.

        Parameters:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        try:
            return x + y
        except TypeError:
            print("Error: Both inputs must be numeric.")
            raise

    def subtract(self, x, y):
        """Subtract two numbers.

        Parameters:
            x (float): The first number (minuend).
            y (float): The second number (subtrahend).

        Returns:
            float: The difference of the two numbers.
        """
        try:
            return x - y
        except TypeError:
            print("Error: Both inputs must be numeric.")
            raise

    def multiply(self, x, y):
        """Multiply two numbers.

        Parameters:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        try:
            return x * y
        except TypeError:
            print("Error: Both inputs must be numeric.")
            raise

    def divide(self, x, y):
        """Divide two numbers.

        Parameters:
            x (float): The numerator.
            y (float): The denominator.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        try:
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return x / y
        except TypeError:
            print("Error: Both inputs must be numeric.")
            raise
        except ZeroDivisionError as e:
            print(e)
            raise

# Example usage:
if __name__ == '__main__':
    calc = MathCalculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    try:
        print("Division by zero: ", calc.divide(10, 0))
    except ZeroDivisionError:
        print("Caught division by zero error.")
