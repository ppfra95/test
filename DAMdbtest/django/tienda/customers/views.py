# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework import viewsets
#
# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from core.models import Customer
# from customers.serializers import CustomerSerializer
#

# @csrf_exempt
# def customer_list(request):
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         customers_serializer = CustomerSerializer(customers, many=True)
#         return JsonResponse(customers_serializer.data, safe=False)
#         # In order to serialize objects, we must set 'safe=False'
#
#     elif request.method == 'POST':
#         customer_data = JSONParser().parse(request)
#         customer_serializer = CustomerSerializer(data=customer_data)
#         if customer_serializer.is_valid():
#             customer_serializer.save()
#             return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         Customer.objects.all().delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#
# # @csrf_exempt
# # def customerLogIn(request, email, password):
#     # if request.method == 'GET':
#     #     customer = Customer.objects.get(email=email)
#     #     print(customer.check_password("password"))
#     #
#     #     # print(customer)
#     #     customers_serializer = CustomerSerializer(customer)
#     #     # print(customer.email)
#     #     return JsonResponse(customers_serializer.data)

# from .models import Token
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from core.models import Customer as MongoUser

from .serializers import *
from .forms import *

Customer = get_user_model()


# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data, context={'request': request}
#         )
#         serializer.is_valid(raise_exception=True)
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
# class ListUsers(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserListSerializer
#     model = serializer_class.Meta.model
#     queryset = model.objects.all()


class CreateUser(generics.CreateAPIView):
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

        instance = MongoUser(**data)
        instance.set_password(password)
        instance.save()
        return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = CustomerListSerializer(instance)
        return Response(instance_serializer.data)


# class EditUser(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserListSerializer
#     model = serializer_class.Meta.model
#     queryset = model.objects.all()

#
# class UserChangePassword(APIView):
#
#     def post(self, request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except Exception:
#             return Response(status=404)
#
#         form = ChangePasswordForm(request.data)
#
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#             return Response({'status': 'OK'}, status=200)
#
#         for key in form.errors:
#             form.errors[key] = ' '.join(form.errors[key])
#
#         return Response(form.errors, status=401)
