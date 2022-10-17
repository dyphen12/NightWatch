# read json document named settings.json

import json
import os
import sys

def read_settings():
    # read the settings file
    path = os.path.join(os.path.dirname(__file__), "settings.json")
    with open(path, "r") as f:
        settings = json.load(f)
    return settings

def write_settings(settings):
    # write the settings file
    path = os.path.join(os.path.dirname(__file__), "settings.json")
    with open(path, "w") as f:
        json.dump(settings, f, indent=4)

