from django.shortcuts import render
from django.http import HttpResponse
# from core.models import Customer, Item
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings

from core.models import Service

# Create your views here.
def service(request):
    services=Service.objects.all()
    return render(request, 'service/core.html',{"services":services})
