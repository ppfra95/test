from django.shortcuts import render
from django.http import HttpResponse
from core.models import Clientes
from django.contrib.auth import authenticate

def index(request):
  newChoice = clientes(nombre="First test")
  newChoice.save()
  return HttpResponse("Test")

user = authenticate(username='Jose', password='9809028JXV')
assert isinstance(user, mongoengine.django.auth.User)
