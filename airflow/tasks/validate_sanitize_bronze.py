import re
import pandas as pd
from typing import List
from csv import DictReader
from pydantic import ValidationError
from utilities import convert_to_csv
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


def sanitize_data(data: List[dict]) -> List[dict]:
    """
    Performs rudimentary sanitizations on bronze data

    Args:
        data (List[dict]): list of IEMs/Headphones

    Returns:
        List[dict]: Sanitized data
    """
    df = pd.DataFrame(data)

    columns_to_drop = [
        "comments",
        "based_on",
        "note_weight",
        "pricesort",
        "techsort",
        "tonesort",
        "ranksort"
    ]

    df = df.drop(columns_to_drop, axis=1)

    # Some signatures have quotes around them, unneeded
    df["signature"] = df["signature"].str.replace('"', "")

    for index, row in df.iterrows():
        # Replacing discontinued devices with no price with -1
        if re.search("Discont", str(row["price"])):
            row["price"] = -1

        # Replacing ? device prices with -1
        if re.search("\\?", str(row["price"])):
            row["price"] = -1

        # Some prices have models embedded to them, this replaces with only price
        # Ex: 3000(HE1000) gives 3000
        if re.search("[a-zA-Z]", str(row["price"])):
            row["price"] = list(filter(None, re.split(r"(\d+)", str(row["price"]))))[0]

            # Some are still text even after splits and earlier cleanses
            if re.search("[a-zA-Z]", str(row["price"])):
                row["price"] = -1

        # Replace star text rating with number. If no stars, replace with -1
        row["value_rating"] = len(row["value_rating"]) if row["value_rating"] else -1

    return df.to_dict("records")


if __name__ == "__main__":
    headphones_file = "/tmp/headphones-bronze.csv"
    iems_file = "/tmp/iems-bronze.csv"

    iems_list = read_csv_as_dicts(iems_file)
    headphones_list = read_csv_as_dicts(headphones_file)

    # Sanitize both CSV files with similar parameters
    iems_list_sanitized = sanitize_data(iems_list)
    headphones_list_sanitized = sanitize_data(headphones_list)

    # Validates all headphones/iems in a list based on the validators
    # defined in the respective PyDantic models
    try:
        iems_list = [InEarMonitor.parse_obj(iem) for iem in iems_list_sanitized]
    except ValidationError as exception:
        print(f"IEM - {exception}")

    try:
        headphones_list = [
            Headphone.parse_obj(headphone) for headphone in headphones_list_sanitized
        ]
    except ValidationError as exception:
        print(f"Headphone - {exception}")

    convert_to_csv(device_data=iems_list_sanitized, device_type="iems", data_level="silver")
    convert_to_csv(
        device_data=headphones_list_sanitized, device_type="headphones", data_level="silver"
    )
