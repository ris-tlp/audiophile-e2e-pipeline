import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open("logs.log", "w"):
    pass


url = "https://crinacle.com/rankings/iems/"
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
except requests.exceptions.RequestException as e:
    logging.log(e)

# Find all tables within page, in this case, the only one
iem_table = soup.findChildren("table")[0]

# Get all the headers for the table
thead = iem_table.find_all("thead", recursive=False)
header = thead[0].findChildren("th")
for cell in header:
    print(cell.text)

# Get all rows within the table (excluding links)
tbody = iem_table.find_all("tbody", recursive=False)
rows = tbody[0].find_all("tr", recursive=False)

for row in rows:
    for cell in row:
        print(cell.text)
    break
