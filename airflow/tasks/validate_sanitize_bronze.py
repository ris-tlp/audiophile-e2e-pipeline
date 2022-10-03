from typing import List
from csv import DictReader
from pydantic import ValidationError
from scraper.models import InEarMonitor, Headphone


def read_csv_as_dicts(filename: str) -> List[dict]:
    """
    Returns a list of dictionaries read from specified csv

    Args:
        filename (str): name of file to be read

    Returns:
        List[dict]
    """
    try:
        with open(filename, "r") as file:
            reader = DictReader(file)
            return list(reader)
    except OSError as exception:
        print(f"{filename} - {exception}")


if __name__ == "__main__":
    headphones_file = "/tmp/headphones-bronze.csv"
    iems_file = "/tmp/iems-bronze.csv"

    # Validates all headphones/iems in a list based on the validators
    # defined in the PyDantic models
    iems_list = read_csv_as_dicts(iems_file)

    try:
        iems_list = [InEarMonitor.parse_obj(iem) for iem in iems_list]
    except ValidationError as exception:
        print(f"IEM - {exception}")

    headphones_list = read_csv_as_dicts(headphones_file)

    try:
        headphones_list = [Headphone.parse_obj(headphone) for headphone in headphones_list]
    except ValidationError as exception:
        print(f"Headphone - {exception}")
