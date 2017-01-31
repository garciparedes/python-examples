import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'World'


schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')
print(result.data['hello'])
