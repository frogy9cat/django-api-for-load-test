
from rest_framework import serializers
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            "username": {
                "required": True
            },
            "password": {
                "required": True,
                "write_only": True
            },
        }
