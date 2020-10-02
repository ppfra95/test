from rest_framework import serializers
from rest_framework_mongoengine import serializers as me_serializers
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django_mongoengine.mongo_auth.models import User

from core.models import *

__all__ = ['CustomerListSerializer', 'CustomerCreateSerializer']


class CustomerListSerializer(me_serializers.DocumentSerializer):

    class Meta:
        model = Customer
        fields = (
            'id', 'first_name','last_name', 'age', 'address',
            'email','cell_Phone','password'
        )
#
#     class Meta:
#         model = Customer
#         fields = (
#             'id','first_name','last_name', 'age', 'address',
#             'email','cell_Phone','password','password2'
#         )


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
        fields = ('email', 'password','password2')

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        data = self.data
        password = data['password']

        try:
            del(data['password2'])
        except Exception:
            pass

        # instance = Customer(**data)
        # instance.set_password(password)
        # instance.save()
        # return instance
        return  Customer().objects.create_user(**data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')

            if password != password2:
                raise serializers.ValidationError(
                    'Las constraseñas no coinciden', code='password_mismatch'
                )

            validate_password(password)
            return attrs


# class AuthTokenSerializer(me_serializers.DocumentSerializer):
#     """Serializer for the user authentication object"""
#     email = serializers.CharField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         trim_whitespace=False
#     )
#
#     class Meta:
#         model = Customer
#         fields = ('email', 'password')
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data, context={'request': request}
#         )
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.is_valid(raise_exception=True))
#         user = serializer.validated_data['user']
#         token = Token.objects.upsert_one(user=user)
#
#         if not token.key:
#             token.key = token.generate_key()
#             token.save()
#         return Response({
#             'token': token.key,
#             'id': str(user.pk),
#             'username': user.username,
#             'email': user.email
#         })
#
#     def validate(self, attrs):
#         """Validate and authenticate the user"""
#         email = attrs.get('email')
#         password = attrs.get('password')
#
#         try:
#             user = Customer.objects.get(username=email)
#             if user.check_password(password):
#                 # user.backend = 'django_mongoengine.mongo_auth.backends.MongoEngineBackend'
#                 # user = authenticate(
#                 #     request=self.context.get('request'),
#                 #     username=email,
#                 #     password=password
#                 # )
#                 # if not user:
#                 #     msg = _('Unable to authenticate with provided credentials')
#                 #     raise serializers.ValidationError(msg, code='authorization')
#                 # user = authenticate(username=email, password=password)
#                 attrs['user'] = user
#                 return attrs
#             else:
#                 msg = _('Unable to authenticate with provided credentials222')
#                 raise serializers.ValidationError(msg, code='authorization')
#         except User.DoesNotExist:
#             msg = _('Unable to authenticate with provided credentials')
#             raise serializers.ValidationError(msg, code='authorization')
