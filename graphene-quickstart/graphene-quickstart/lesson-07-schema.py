#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/types/schema/
"""

import graphene


class Person(graphene.ObjectType):
    last_name = graphene.String()
    other_name = graphene.String(name='_other_Name')
