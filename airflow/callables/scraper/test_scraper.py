from unittest.mock import NonCallableMock
import pytest
import requests
import unittest
from bs4 import BeautifulSoup


class TestScraper(unittest.TestCase):
    """
    Unittests to test the structure of the webpage being scraped
    """

    def setUp(self):
        headphone_url = "https://crinacle.com/rankings/headphones/"
        iem_url = "https://crinacle.com/rankings/iems/"

        self.headphone_response = requests.get(headphone_url)
        self.headphone_soup = BeautifulSoup(self.headphone_response.text, "html.parser")

        self.iem_response = requests.get(iem_url)
        self.iem_soup = BeautifulSoup(self.iem_response.text, "html.parser")

    def test_iem_response(self):
        """
        Test if IEM url connection is successful
        """
        self.assertEqual(self.headphone_response.status_code, 200)

    def test_headphone_response(self):
        """
        Test if Headphone url connection is successful
        """
        self.assertEqual(self.iem_response.status_code, 200)

    def test_iem_soup(self):
        """
        Test if IEM soup parsed successfully
        """
        self.assertNotEqual(self.iem_soup, None)

    def test_headphone_soup(self):
        """
        Test if Headphone soup parsed successfully
        """
        self.assertNotEqual(self.headphone_soup, None)

    def test_iem_table(self):
        """
        Test if the database table in the IEM url exists
        """
        self.assertGreaterEqual(len(self.iem_soup.find_all("table")), 0)

    def test_headphone_table(self):
        """
        Test if the database table in the Headphone url exists
        """
        self.assertGreaterEqual(len(self.headphone_soup.find_all("table")), 0)

    def test_iem_table_not_empty(self):
        """
        Test if the database table in the IEM url is not empty
        """
        self.assertGreaterEqual(len(self.iem_soup.find_all("tr")), 0)

    def test_headphone_table_not_empty(self):
        """
        Test if the database table in the Headphone url is not empty
        """
        self.assertGreaterEqual(len(self.headphone_soup.find_all("tr")), 0)

    def test_iem_table_header(self):
        """
        Test if the header in the IEM database table exists
        """
        self.assertNotEqual(self.iem_soup.find_all("thead"), None)

    def test_headphone_table_header(self):
        """
        Test if the header in the Headphone database table exists
        """
        self.assertNotEqual(self.headphone_soup.find_all("thead"), None)

    def test_iem_table_body(self):
        """
        Test if the body in the IEM database table exists
        """
        self.assertNotEqual(self.iem_soup.find_all("tbody"), None)

    def test_headphone_table_body(self):
        """
        Test if the body in the Headphone database table exists
        """
        self.assertNotEqual(self.headphone_soup.find_all("tbody"), None)
