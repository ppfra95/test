from django.shortcuts import render
from django.http import HttpResponse
# from core.models import Customer, Item
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
# from core.forms import Contacto

def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
