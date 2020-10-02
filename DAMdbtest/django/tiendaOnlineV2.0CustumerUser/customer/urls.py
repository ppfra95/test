from django.urls import path

from . import views

app_name = 'CustomAuth'

urlpatterns = [
    path('login/', views.CustomAuthToken.as_view()),
    path('list/', views.ListCustomer.as_view()),
    path('<pk>/edit/', views.EditCustomer.as_view()),
    path('<pk>/change-password/', views.CustomerChangePassword.as_view()),
    path('create/', views.CreateCustomer.as_view()),
]
