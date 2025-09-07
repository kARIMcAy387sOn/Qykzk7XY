# 代码生成时间: 2025-09-07 16:22:11
import pandas as pd
import json
import os

"""
Config Manager is a tool to manage configuration files using Python and Pandas.
It provides a simple way to read, write, and update configuration settings.
"""

class ConfigManager:
    """
    A class to manage configuration files.
    """
    def __init__(self, filepath, format_type='json'):
        self.filepath = filepath
        self.format_type = format_type
        self.config_data = self._load_config()

    def _load_config(self):
        """
        Loads the configuration data from the file.
        Returns a dictionary of configuration settings.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Config file not found at {self.filepath}")
        
        if self.format_type == 'json':
            with open(self.filepath, 'r') as file:
                return json.load(file)
        elif self.format_type == 'csv':
            return pd.read_csv(self.filepath).to_dict()
        else:
            raise ValueError(f"Unsupported format type: {self.format_type}")

    def save_config(self, data):
        """
        Saves the configuration data to the file.
        """
        if self.format_type == 'json':
            with open(self.filepath, 'w') as file:
                json.dump(data, file, indent=4)
        elif self.format_type == 'csv':
            pd.DataFrame(data).to_csv(self.filepath, index=False)
        else:
            raise ValueError(f"Unsupported format type: {self.format_type}")

    def update_config(self, key, value):
        """
        Updates a configuration setting.
        """
        self.config_data[key] = value
        self.save_config(self.config_data)

    def get_config(self, key):
        """
        Retrieves a configuration setting.
        """
        return self.config_data.get(key)

    def list_configs(self):
        """
        Lists all configuration settings.
        """
        return self.config_data.keys()

# Example usage
if __name__ == '__main__':
    config_filepath = 'config.json'
    config_manager = ConfigManager(config_filepath)
    try:
        print(config_manager.get_config('database_url'))
        config_manager.update_config('database_url', 'new_database_url')
    except FileNotFoundError:
        print(f"Error: Config file {config_filepath} not found.")
    except ValueError as e:
        print(f"Error: {e}")
