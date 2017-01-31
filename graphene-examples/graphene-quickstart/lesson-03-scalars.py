#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/types/scalars/
"""

import datetime

import graphene
from graphene.types import Scalar
from graphql.language import ast


class DateTime(Scalar):
    """DateTime Scalar Description"""

    @staticmethod
    def serialize(dt):
        return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def parse_value(value):
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")


class Person(graphene.ObjectType):
    name = graphene.String()
