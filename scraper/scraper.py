import logging
import requests
from bs4 import BeautifulSoup
from models import Headphone, InEarMonitor

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open("logs.log", "w"):
    pass


device_type = ["iems", "headphones"]

for device in device_type:
    url = f"https://crinacle.com/rankings/{device}/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.log(e)

    # Find all tables within page, in this case, the only one
    iem_table = soup.findChildren("table")[0]

    # Get all the headers for the table
    thead = iem_table.find_all("thead", recursive=False)
    headers = thead[0].findChildren("th")
    headers = [cell.text for cell in headers]

    # Get all rows within the table (excluding links)
    tbody = iem_table.find_all("tbody", recursive=False)
    rows = tbody[0].find_all("tr", recursive=False)

    device_data = []

    for row in rows:
        row_data = {}
        for i, cell in enumerate(row.find_all("td", recursive=False)):
            row_data[headers[i]] = cell.get_text()
        device_data.append(row_data)

    if device == "headphones":
        headphone = Headphone(device_data[0])
        print(headphone)
    else:
        iem = InEarMonitor(device_data[0])
        print(iem)
