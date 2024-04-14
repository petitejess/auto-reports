import json
from enum import Enum

class BaseDirPath(Enum):
    pass

with open('/workspaces/auto-reports/app/configs/dirconfig.json') as f:
    data = json.load(f)

    for key, value in data["dirpath"].items():
        setattr(BaseDirPath, key, value)

class DirPath(Enum):
    config_basedir = BaseDirPath.base + BaseDirPath.config["dir"]
    COMPANY = config_basedir + BaseDirPath.config["company"]
    ORDER_FILE = config_basedir + BaseDirPath.config["order_file"]
    ORDER_LOOKUP = config_basedir + BaseDirPath.config["order_lookup"]

    in_basedir = BaseDirPath.base + BaseDirPath.input["dir"]
    IN_MYOB = in_basedir + BaseDirPath.input["myob"]

    out_basedir = "./" +BaseDirPath.output["dir"]
    OUT_ARCHIVE = out_basedir + BaseDirPath.output["archivedir"]
    OUT_ORDER = out_basedir + BaseDirPath.output["orderdir"]
    OUT_EOMS = out_basedir + BaseDirPath.output["eomsdir"]
