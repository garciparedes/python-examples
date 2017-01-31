#!/usr/bin/env python

"""
URL: http://docs.graphene-python.org/en/latest/types/mutations/
"""

import graphene
import utils.json as uj


class CreatePerson(graphene.Mutation):
    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, args, context, info):
        person = Person(name=args.get('name'))
        ok = True
        return CreatePerson(person=person, ok=ok)


class Person(graphene.ObjectType):
    name = graphene.String()


class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()


schema = graphene.Schema(mutation=MyMutations)

query_string = 'mutation myFirstMutation {' \
               '   createPerson(name:"Peter") {' \
               '       person {' \
               '           name' \
               '       }' \
               '       ok' \
               '   }' \
               '}'

result = schema.execute(query_string)

print(uj.dict_to_json(result.data))


