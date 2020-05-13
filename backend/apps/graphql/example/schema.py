import graphene
from graphene import relay, AbstractType, ObjectType
from .types import UserType
from .models import Example
from django.contrib.auth.models import User
import json

class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)
    # users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get("id")
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

