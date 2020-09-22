from django.shortcuts import render
from django.http import HttpResponse
from core.models import Customer, Item
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from core.forms import Contacto

def index(request):
  newChoice = Customer(name="First",last_Name="Test",address="test#1",email="test@123.com",cell_Phone="1234567890")
  newChoice.save()
  newChoice2 = Item(name="First",seccion="Test",cost="100.00")
  newChoice2.save()
  return HttpResponse("Test")

def busquedaPrd(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        mensaje="Articulo Buscado: %r" %request.GET['prd']
        producto=request.GET["prd"]
        if len(producto)>30:
            mensaje="texto demasiado largo max = 30 caracteres"
        else:
            articulos=Item.objects(name__icontains=producto)
            return render(request, "resultados.html", {"articulos":articulos,"query":producto})
    else:
        mensaje="no has introducido nada"

    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":
        f=Contacto(request.POST)
        if f.is_valid():
            inf=f.cleaned_data
            send_mail(inf['subject'], inf['message']+" "+inf.get('email'), '',[settings.SERVER_EMAIL])
            return render(request,"test.html")
    else:
        f=Contacto()
    return render(request,'contacto.html',{"form":f})
