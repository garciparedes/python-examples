#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/execution/middleware/
"""

import graphene
import utils.json as uj


class AuthorizationMiddleware(object):
    def resolve(self, next, root, args, context, info):
        if info.field_name == 'user':
            return None
        return next(root, args, context, info)


class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, args, context, info):
        return context.get('name')


schema = graphene.Schema(Query)
result = schema.execute('{ name }', context_value={'name': 'Syrus'}, middleware=[AuthorizationMiddleware()])

print(uj.dict_to_json(result.data))
