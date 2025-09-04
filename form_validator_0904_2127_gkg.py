# 代码生成时间: 2025-09-04 21:27:58
import pandas as pd

"""
Form Validator using Python and Pandas.
This module provides a simple form validator for validating form data.
It checks for required fields, data types, and custom validation rules.
"""

class FormValidator:
    def __init__(self, data, schema):
        """
        Initialize the FormValidator with form data and validation schema.
        :param data: DataFrame containing the form data to validate.
        :param schema: Dictionary defining the validation schema.
        """
        self.data = data
        self.schema = schema

    def validate(self):
        """
        Perform the validation of the form data.
        :return: A DataFrame with validation results.
        """
        errors = []
        for column, rules in self.schema.items():
            for rule in rules:
                # Check required fields
                if 'required' in rule and rule['required'] and column not in self.data.columns:
                    errors.append((f"{column} is required but missing"))
                    continue

                # Check data type
                if 'type' in rule and not self._check_type(column, rule['type']):
                    errors.append((f"{column} is of incorrect type. Expected {rule['type']}"))
                    continue

                # Add custom validation rules here
                # For example, checking if a value is in a specific list
                # if 'in' in rule and self.data[column] not in rule['in']:
                #     errors.append((f"{column} is not in the allowed list"))
                #     continue

        # Create a DataFrame with the validation results
        if errors:
            validation_results = pd.DataFrame({"error": errors})
        else:
            validation_results = pd.DataFrame({"status": ["All fields are valid"]}, index=[0])

        return validation_results

    def _check_type(self, column, expected_type):
        """
        Helper function to check if the data in a column matches the expected type.
        :param column: The name of the column to check.
        :param expected_type: The expected data type.
        :return: True if the type matches, False otherwise.
        """
        actual_type = self.data[column].dtype
        if expected_type == 'int':
            return actual_type == 'int64'
        elif expected_type == 'float':
            return actual_type == 'float64'
        elif expected_type == 'str':
            return actual_type == 'object'
        else:
            raise ValueError(f"Unsupported type: {expected_type}")

# Example usage:
if __name__ == '__main__':
    # Sample form data
    form_data = pd.DataFrame({
        'email': ['user@example.com', ''],
        'age': ['25', 'thirty']
    })

    # Validation schema
    validation_schema = {
        'email': [{'required': True, 'type': 'str'}],
        'age': [{'required': True, 'type': 'int'}]
    }

    # Create a FormValidator instance
    validator = FormValidator(form_data, validation_schema)

    # Perform validation
    results = validator.validate()
    print(results)