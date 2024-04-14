import json
from enum import Enum

from configs.dirconfigenum import DirPath

class CompanyName(Enum):
    pass


with open(DirPath.COMPANY.value) as f:
    data = json.load(f)

    for key, value in data["companies"].items():
        setattr(CompanyName, key, (value["code"], value["name"]))
