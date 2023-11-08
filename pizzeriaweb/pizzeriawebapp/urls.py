from django.urls import path
from pizzeriawebapp import views

urlpatterns = [
    path('', views.index, name='Home'),
]