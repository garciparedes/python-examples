#!/usr/bin/env python

__author__ = "Sergio Garcia Prado"
__license__ = "MPL-2.0"
__version__ = "1.0.0"
__maintainer__ = "Sergio Garcia Prado"
__email__ = "sergio@garciparedes.me"

import json


def dict_to_json(dict_data):
    return json.dumps(dict_data, indent=2, sort_keys=True)
