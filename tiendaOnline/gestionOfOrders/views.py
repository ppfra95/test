from django.shortcuts import render
from django.http import HttpResponse
from core.models import Customers
from django.contrib.auth import authenticate

def index(request):
  newChoice = Customers(Name="First",Last_Name="Test",Address="test#1",Email="test@123.com",Cell_Phone="1234567890")
  newChoice.save()
  return HttpResponse("Test")
