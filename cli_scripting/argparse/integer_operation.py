#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Apply operations over numbers')

parser.add_argument('number', type=int, help='number to operate')
parser.add_argument('--other', type=int, help='other to operate')
parser.add_argument('-s', '--square', help='display a square of a given number', action='store_true')
parser.add_argument('-c', '--cube', help='display a cube of a given number', action='store_true')
parser.add_argument('--sum', help='apply sum', action='store_true')

args = parser.parse_args()

number = args.number

if args.square:
    number **= 2

if args.cube:
    number **= 3

if args.other:
    other = args.other
    if args.sum:
        number += other

print(number)
