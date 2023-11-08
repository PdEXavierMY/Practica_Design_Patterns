from django.urls import path
from pizzeriawebapp import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='Registro'),
    path('crear_pizza/', views.crear_pizza, name='Crear Pizza'),
]