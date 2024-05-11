import json
from enum import Enum

from app.utils.dirutil import concat_base_dir, get_appconfig

class TopPath(Enum):
    pass

class EndPath(Enum):
    pass

class Filename(Enum):
    pass


with open(get_appconfig()) as f:
    data = json.load(f)

    for key, value in data["toppath"].items():
        setattr(TopPath, key, value)
    
    for key, value in data["endpath"].items():
        setattr(EndPath, key, value)
    
    for key, value in data["filename"].items():
        setattr(Filename, key, value)


class DirPath(Enum):
    COMPANY = concat_base_dir(TopPath.configs + Filename.company)
    INCONF = concat_base_dir(TopPath.configs + Filename.inconf)
    ORDERLOOKUP = concat_base_dir(TopPath.configs + Filename.orderlookup)
    EOMSLOOKUP = concat_base_dir(TopPath.configs + Filename.eomslookup)

    IN_ORDER = concat_base_dir(TopPath.inputs + EndPath.orders + Filename.myob)
    IN_EOMS = concat_base_dir(TopPath.inputs + EndPath.eoms + Filename.myob)

    out_basedir = "./"
    OUT_ORDER_ARCHIVE = out_basedir + EndPath.orders + TopPath.archive
    OUT_EOMS_ARCHIVE = out_basedir + EndPath.eoms + TopPath.archive
    OUT_ORDER = out_basedir + TopPath.outputs + EndPath.orders
    OUT_EOMS = out_basedir + TopPath.outputs + EndPath.eoms
