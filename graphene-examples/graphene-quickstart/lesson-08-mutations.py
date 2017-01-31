#!/usr/bin/env python3

"""
URL: http://docs.graphene-python.org/en/latest/types/mutations/
"""

import graphene
import utils.json as uj


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class PersonInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()


class CreatePerson(graphene.Mutation):
    class Input:
        person_data = graphene.Argument(PersonInput)

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, args, context, info):
        p_data = args.get('person_data')

        name = p_data.get('name')
        age = p_data.get('age')

        person = Person(name=name, age=age)
        ok = True
        return CreatePerson(person=person, ok=ok)


class LatLngInput(graphene.InputObjectType):
    lat = graphene.Float()
    lng = graphene.Float()


# A location has a latlng associated to it
class LocationInput(graphene.InputObjectType):
    name = graphene.String()
    latlng = graphene.InputField(LatLngInput)


class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()


schema = graphene.Schema(mutation=MyMutations)

query_string = 'mutation myFirstMutation {' \
               '   createPerson(personData: {name:"Peter", age: 24}) {' \
               '       person {' \
               '           name,' \
               '           age' \
               '       }' \
               '       ok' \
               '   }' \
               '}'

result = schema.execute(query_string)

print(uj.dict_to_json(result.data))
