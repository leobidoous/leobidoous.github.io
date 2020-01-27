from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ['name', 'cpf', 'genre', 'email', 'telephone', 'birth', 'date_joined', 'dt_update']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
