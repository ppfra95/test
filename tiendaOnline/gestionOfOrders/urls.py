from django.urls import path

from . import views

urlpatterns = [
    path('hola/', views.index, name='hola'),
    path('busquedaPrd/', views.busquedaPrd),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto),
]
