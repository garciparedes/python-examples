#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/types/objecttypes/
"""

import graphene


class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)
