from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, renderers
from .serializers import UserSerializer, GroupSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    renderer_classes = [ renderers.JSONOpenAPIRenderer ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ permissions.IsAuthenticated ]