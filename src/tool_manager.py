import json
import pandas as pd

from tools.constant import DATA_LITERAL_STR, FILENAME_JSON_STR, FILEPATH_STR


def load_json_data() -> list:
    with open(FILENAME_JSON_STR, "r") as json_file:
        data = json.load(json_file)
    return data


def change_data_to_idx(data: list) -> list:
    for index, item in enumerate(iterable=data, start=1):
        item[DATA_LITERAL_STR] = index - 1
    return data


def extract_data_json(data: list) -> list:
    data_json: list = []
    for item in data:
        json_loads = json.loads(item[DATA_LITERAL_STR])
        key_json = list(json_loads.keys())[0]
        data_json.append(json_loads[key_json])
    return data_json


def create_tables(data: list) -> None:
    table2 = pd.DataFrame(extract_data_json(data=data))
    table1 = pd.DataFrame(change_data_to_idx(data=data))

    with pd.ExcelWriter(FILEPATH_STR, engine="openpyxl") as writer:
        table1.to_excel(writer, sheet_name="table 1", index=False)
        table2.to_excel(writer, sheet_name="table 2", index_label=DATA_LITERAL_STR)
