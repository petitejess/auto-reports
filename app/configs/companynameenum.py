import json
from enum import Enum

class CompanyName(Enum):
    pass

with open('/workspaces/auto-reports/app/configs/companyconfig.json') as f:
    data = json.load(f)

    for key, value in data['companies'].items():
        setattr(CompanyName, key, (value['code'], value['name']))
