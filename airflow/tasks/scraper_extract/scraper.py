import re
import csv
import pprint
import pathlib
import logging
import requests
from bs4 import BeautifulSoup

script_path = pathlib.Path(__file__).parent.resolve()

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open("logs.log", "w"):
    pass


class Scraper:
    """
    Encapsulates all the logic for the web scraper.
    """

    def __init__(self) -> None:
        self.base_url = "https://crinacle.com/rankings/"

    def clean_headers(self, headers: list) -> list:
        """
        Formats the table headers in snake case, code friendly format

        Args:
            headers (list): Contains the unformatted dirty table headers

        Returns:
            list: Returns properly formatted table headers
        """
        clean_headers = []

        for header in headers:
            # Remove unnecessary terms
            if "(" in header or "/" in header:
                header = header.split(" ")[0]

            # Rename header for conformity between both IEMS and headphones
            if "Setup" == header:
                header = "driver_type"

            # Convert to snake_case
            clean_headers.append(
                re.sub(r"(?<=[a-z])(?=[A-Z])|[^a-zA-Z]", " ", header).replace(" ", "_").lower()
            )

        return clean_headers

    def scrape(self, device_type: str) -> list:
        """
        Scrapes Crinacle's databases containing technical information about Headphones and IEMs.

        Args:
            device_type (str): specifies the device type and url to be scraped.
        """
        url = self.base_url + device_type
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            logging.log(e)

        # Find all tables within page, in this case, the only one
        data_table = soup.findChildren("table")[0]

        # Get all the headers for the table
        thead = data_table.find_all("thead", recursive=False)
        headers = thead[0].findChildren("th")
        headers = [cell.text for cell in headers]
        headers = self.clean_headers(headers)

        # Get all rows within the table (excluding links)
        tbody = data_table.find_all("tbody", recursive=False)
        rows = tbody[0].find_all("tr", recursive=False)

        device_data = []

        for row in rows:
            row_data = {}
            for i, cell in enumerate(row.find_all("td", recursive=False)):
                row_data[headers[i]] = cell.get_text()
            device_data.append(row_data)

        # device_data = self.convert_to_model(device_data=device_data, device_type=device_type)
        return device_data

    def convert_to_csv(self, device_data: list, device_type: str, data_level: str) -> None:
        """
        Converts a list of dictionaries to a csv file

        Args:
            device_data (list[dict]): List of dictionaries containing each device
            device_type (str): String specifiying the type of device: headphones or iems
            data_level (str): Signifies the level of data, ie, gold, bronze, silver
        """
        with open(f"/tmp/{device_type}-{data_level}.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=device_data[0].keys())
            writer.writeheader()
            writer.writerows(device_data)


if __name__ == "__main__":
    scraper = Scraper()
    headphones = scraper.scrape(device_type="headphones")
    iems = scraper.scrape(device_type="iems")

    scraper.convert_to_csv(device_data=headphones, device_type="headphones", data_level="bronze")
    scraper.convert_to_csv(device_data=iems, device_type="iems", data_level="bronze")
