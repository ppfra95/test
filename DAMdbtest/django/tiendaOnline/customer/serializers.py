from rest_framework import serializers
from rest_framework_mongoengine import serializers as me_serializers
from django.contrib.auth.password_validation import validate_password
from core.models import *

__all__ = ['CustomerListSerializer', 'CustomerCreateSerializer']


class CustomerListSerializer(me_serializers.DocumentSerializer):

    class Meta:
        model = Customer
        fields = (
            'id', 'first_name','last_name', 'age', 'address',
            'email','cell_Phone','password'
        )


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
