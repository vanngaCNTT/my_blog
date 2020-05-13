from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(jb4jmong9bk_h_n*e=0&41#1(6=uzug@r&)=^92u($n^gjvzx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'graphene_django',
    'backend.apps.graphql.example',
]
# from backend.apps.graphql.example.schema
GRAPHENE = {
    'SCHEMA': 'backend.apps.graphql.schema.schema',
}