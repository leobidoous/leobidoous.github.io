from rest_framework import serializers
from user.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'cpf', 'genre', 'email', 'telephone', 'birth', 'date_joined', 'last_update']

