from django.http import HttpResponse
# from django.template import Template, Context
# from django.template.loader import get_template
from django.template import Template
from django.shortcuts import render

def hola(request):
    persona={"Name":"Juan",
        "Lastname":"Perez",
        "Hobbies":["leer","jugar","musica"]
        }
    # doc_externo=get_template("plantilla1.html")
    # doc=doc_externo.render(persona)
    # return HttpResponse(doc)
    return render(request, "plantilla1.html", persona)

def adios(request):
    return render(request, "plantilla2.html")

def calEdad(request, anno, edadA):
    edadA=18
    periodo=anno-2020
    edadF=edadA+periodo
    return HttpResponse("En el año %s tendras %s años" %(anno, edadF))
