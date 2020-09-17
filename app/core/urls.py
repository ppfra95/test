from django.urls import path

from . import views

urlpatterns = [
    path('hola/', views.hola, name='hola'),
    path('adios/', views.adios, name='adios'),
    path('edad/<int:anno>', views.adios, name='edadFutura'),
]
