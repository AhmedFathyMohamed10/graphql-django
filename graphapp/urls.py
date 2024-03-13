from django.urls import path
from django.views.decorators import csrf
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('graphql/', csrf.csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
]