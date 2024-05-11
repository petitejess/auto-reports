from os import path
import sys
import json


def get_basedir():
    if getattr(sys, "frozen", False):
        basedir = path.dirname(sys.executable)
    else:
        basedir = path.dirname(path.dirname(path.dirname(__file__)))

    return basedir


def concat_base_dir(add_on_dir):
    return get_basedir() + add_on_dir


def get_appconfig():
    return path.join(get_basedir(), "app/configs/dirconfig.json")


def read_config(file_path):
        with open(file_path, "r") as file:
            config = json.load(file)
        return config
