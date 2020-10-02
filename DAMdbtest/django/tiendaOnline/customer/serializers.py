from rest_framework import serializers
from rest_framework_mongoengine import serializers as me_serializers
from django.contrib.auth.password_validation import validate_password
from django_mongoengine.mongo_auth.models import User
from core.models import *

__all__ = ['UserListSerializer', 'UserCreateSerializer', 'CustomerCreateSerializer']


class UserListSerializer(me_serializers.DocumentSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserCreateSerializer(me_serializers.DocumentSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'password', 'password2'
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                'Las constraseñas no coinciden', code='password_mismatch'
            )

        validate_password(password)
        return attrs


class CustomerCreateSerializer(me_serializers.DocumentSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    class Meta:
        model = Customer
        fields = (
            'id', 'first_name','last_name', 'age', 'address',
            'email','cell_Phone','password','password2'
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                'Las constraseñas no coinciden', code='password_mismatch'
            )

        validate_password(password)
        return attrs
