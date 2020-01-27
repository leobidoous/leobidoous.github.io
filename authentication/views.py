from rest_framework import viewsets
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from user.serializers import UserSerializer


class AuthLoginViewSet(JSONWebTokenAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = JSONWebTokenSerializer

