import graphene
from apps.aplicaciones import schema

class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
		