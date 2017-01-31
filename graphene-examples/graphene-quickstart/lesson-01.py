#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/quickstart/
"""

import graphene
import utils.json as uj


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'World'


schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')

print(uj.dict_to_json(result.data))
