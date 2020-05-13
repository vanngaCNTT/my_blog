  
import graphene
from graphene_django.types import DjangoObjectType
# from graphene import relay, AbstractType, ObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User