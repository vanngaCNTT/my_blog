from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(jb4jmong9bk_h_n*e=0&41#1(6=uzug@r&)=^92u($n^gjvzx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    # Disable browsable API renderer
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONOpenAPIRenderer',
    # )
}