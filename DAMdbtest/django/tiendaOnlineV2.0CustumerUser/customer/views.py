from core.models import *
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django_mongoengine.mongo_auth.models import User as MongoUser, AbstractUser

from .serializers import *
from core.forms import *

Customer = get_user_model()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.upsert_one(user=user)

        if not token.key:
            token.key = token.generate_key()
            token.save()
        return Response({
            'token': token.key,
            'id': str(user.pk),
            'username': user.username,
            'email': user.email
        })


class ListCustomer(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class CreateCustomer(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerCreateSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def perform_create(self, serializer):
        data = serializer.data
        password = data['password']

        try:
            del(data['password2'])
        except Exception:
            pass

        instance = Customer(**data)
        instance.set_password(password)
        instance.save()
        return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = CustomerListSerializer(instance)
        return Response(instance_serializer.data)


class EditCustomer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class CustomerChangePassword(APIView):

    def post(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Exception:
            return Response(status=404)

        form = ChangePasswordForm(request.data)

        if form.is_valid():
            password = form.cleaned_data['password']
            customer.set_password(password)
            customer.save()
            return Response({'status': 'OK'}, status=200)

        for key in form.errors:
            form.errors[key] = ' '.join(form.errors[key])

        return Response(form.errors, status=401)
