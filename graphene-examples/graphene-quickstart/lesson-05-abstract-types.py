#!/usr/bin/env python

"""
URL: http://docs.graphene-python.org/en/latest/types/abstracttypes/
"""

import graphene


class UserFields(graphene.AbstractType):
    name = graphene.String()


class User(graphene.ObjectType, UserFields):
    pass


class UserInput(graphene.InputObjectType, UserFields):
    pass
