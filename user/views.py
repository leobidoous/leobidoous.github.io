from rest_framework import viewsets
from .models import UserModel
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
