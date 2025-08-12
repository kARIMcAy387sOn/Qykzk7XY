# 代码生成时间: 2025-08-13 03:31:41
import pandas as pd

"""
Theme Switcher Module

This module provides functionality to switch themes within a pandas DataFrame.
It allows users to apply different styles to the DataFrame based on a theme.
"""


class Theme:
    """
    Represents a theme with its associated styles.
    """
    def __init__(self, name, styles):
        self.name = name
        self.styles = styles

    def apply(self, df):
        """
        Apply the theme's styles to the DataFrame.
        """
        return df.style.apply(self.styles, axis=None)


class ThemeSwitcher:
    """
    Manages themes and allows switching between them.
    """
    def __init__(self):
        self.themes = {}
        self.current_theme = None

    def add_theme(self, theme):
        """
        Add a new theme to the switcher.
        """
        if not isinstance(theme, Theme):
            raise ValueError("Only Theme instances can be added.")

        self.themes[theme.name] = theme
        print(f"Theme {theme.name} added successfully.")

    def set_theme(self, theme_name):
        """
        Set the current theme.
        """
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' not found.")

        self.current_theme = self.themes[theme_name]
        print(f"Theme switched to {theme_name}.")

    def apply_theme(self, df):
        "