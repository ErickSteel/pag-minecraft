import graphene
from graphene_django import DjangoObjectType
from .models import *

class PruebaType(DjangoObjectType):
    class Meta:
        model = Prueba

class Query(graphene.ObjectType):
    Prueba = graphene.List(PruebaType)

    def resolve_Prueba(self, info, *kwarts):
        return Prueba.objects.all()