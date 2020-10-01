from django.urls import path
from customers import views

urlpatterns = [
    path('', views.customer_list),
    path('create/', views.CreateUser.as_view()),
    # path('login/<email>/<password>/', views.customerLogIn),
    # path('login/', views.customerLogIn),
    # path('customers/<int:pk>', views.customer_detail),
    # path('customers/age/(<int:age>', views.customer_list_age),
]
