#!/usr/bin/env python

"""
URL: http://docs.graphene-python.org/en/latest/execution/#context
"""

import graphene
import utils.json as uj


class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, args, context, info):
        return context.get('name')


schema = graphene.Schema(Query)
result = schema.execute('{ name }', context_value={'name': 'Syrus'})

print(uj.dict_to_json(result.data))
