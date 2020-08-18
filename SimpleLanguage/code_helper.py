import json
from glob import glob
from typing import List


def foundDatabasesList(basePath: str) -> List[str]:
    if basePath[-1] != "\\" and basePath[-1] != "/":
        basePath = basePath + "/"
    return glob(basePath + ".*", recursive=False)


def LoadDatabaseList(databasesList: List[str]) -> dict:
    data = {}

    for element in databasesList:
        name = element.split("\\")[-1].split(".")[0]

        with open(element, "r") as read_file:
            data[name] = json.load(read_file)

    return data


def foundSystemLanguage():
    pass
    # TODO: foundSystemLanguage, Scheduled with low priority
