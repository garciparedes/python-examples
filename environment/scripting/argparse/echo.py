#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="echo the string you use here")
args = parser.parse_args()

print(args.text)
