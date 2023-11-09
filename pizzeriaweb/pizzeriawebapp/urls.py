from django.urls import path
from pizzeriawebapp import views

urlpatterns = [
    path('index/', views.index, name='Home'),
    path('', views.login, name='Login'),
    path('register/', views.register, name='Registro'),
    path('crear_pizza/', views.crear_pizza, name='Crear Pizza'),
]