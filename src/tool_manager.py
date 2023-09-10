import json
import pandas as pd

from tools.constant import DATA_LITERAL_STR, FILENAME_JSON_STR, FILEPATH_STR


def load_json_data() -> list:
    """
    Load data from a JSON file and return it as a list.

    Returns:
        list: A list of data loaded from the JSON file.
    """
    with open(FILENAME_JSON_STR, "r") as json_file:
        data = json.load(json_file)
    return data


def change_data_to_idx(data: list) -> list:
    """
    Change the index of each item in the data list.

    Args:
        data (list): The data list to which the index will be changed.

    Returns:
        list: The data list with changed indices.
    """
    for index, item in enumerate(iterable=data, start=1):
        item[DATA_LITERAL_STR] = index - 1
    return data


def extract_data_json(data: list) -> list:
    """
    Extract JSON data from a list of data.

    Args:
        data (list): The data list from which JSON data will be extracted.

    Returns:
        list: A list of JSON data extracted from the input list.
    """
    data_json: list = []
    for item in data:
        json_loads = json.loads(item[DATA_LITERAL_STR])
        key_json = list(json_loads.keys())[0]
        data_json.append(json_loads[key_json])
    return data_json


def create_tables(data: list) -> None:
    """
    Create and save tables in an Excel file from a list of data.

    Args:
        data (list): The data list from which tables will be created.

    Returns:
        None
    """
    table2 = pd.DataFrame(extract_data_json(data=data))
    table1 = pd.DataFrame(change_data_to_idx(data=data))

    with pd.ExcelWriter(FILEPATH_STR, engine="openpyxl") as writer:
        table1.to_excel(writer, sheet_name="table 1", index=False)
        table2.to_excel(writer, sheet_name="table 2", index_label=DATA_LITERAL_STR)
