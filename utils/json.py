#!/usr/bin/env python

import json


def dict_to_json(dict):
    return json.dumps(dict, indent=2, sort_keys=True)
