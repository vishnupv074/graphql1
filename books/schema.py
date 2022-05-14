from dataclasses import fields
import imp
from pyexpat import model
import graphene
from graphene_django import DjangoObjectType  # Formating the django object to a format that can be used by the graph QL
from .models import Books


class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):

    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Books.objects.all()

schema = graphene.Schema(query=Query)
