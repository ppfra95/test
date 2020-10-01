from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets

from django.contrib.auth import authenticate
from core.models import Customer
from customers.serializers import CustomerSerializer


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def customerLogIn(request, email, password):
    if request.method == 'GET':
        customer = Customer.objects.filter(email=email)
        user = Customer.objects.get(email=email)
        print(user.check_password(password))
        print(user)
        # user = authenticate(username=email, password=password)
        # if user is not None:
        #     print(user)
        # else:
        #     print("no jalo")
        # print(user)
        print(customer)
        customers_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
