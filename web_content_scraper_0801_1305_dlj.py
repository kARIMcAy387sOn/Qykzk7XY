# 代码生成时间: 2025-08-01 13:05:45
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

"""
Web Content Scraper

A Python program to scrape web content using the Requests and BeautifulSoup libraries.
It can be used to extract data from HTML pages and store it in a pandas DataFrame.
"""

class WebContentScraper:
    def __init__(self, base_url):
        """
        Initialize the WebContentScraper with a base URL.
        :param base_url: The base URL of the website to scrape.
        """
        self.base_url = base_url

    def get_html(self, url):
        """
        Retrieve the HTML content of a given URL.
        :param url: The URL to retrieve the HTML content from.
        :return: The HTML content as a string.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error retrieving HTML: {e}")
            return None

    def parse_html(self, html):
        "