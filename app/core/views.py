from django.http import HttpResponse


def hola(request):
    return HttpResponse("hola, esto es un repaso")

def adios(request):
    return HttpResponse("se acabo el repaso ")

def calEdad(request, anno):
    ededA=18
    periodo=anno-2020
    edadFutura=edadA+periodo
    doc="En el año "+anno+" tendras "+edadFutura+" años"
    return HttpResponse(doc)
