from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .scema import sc



urlpatterns = [
   path("graphqp/",GraphQLView.as_view(graphiql=True,schema=sc))
]
