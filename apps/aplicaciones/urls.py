from . import views
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	#path("", GraphQLView.as_view(graphiql=True)),
	path('', csrf_exempt(GraphQLView.as_view(graphiql=True)))
    #path('', views.indice, name='indice'),
]