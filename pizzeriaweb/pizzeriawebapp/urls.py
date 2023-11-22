from django.urls import path
from pizzeriawebapp import views

urlpatterns = [
    path('index/', views.index, name='Home'),
    path('', views.login, name='Login'),
    path('register/', views.register, name='Registro'),
    path('crear_pizza/', views.crear_pizza, name='Crear Pizza'),
    path('menu1/', views.menu1, name='Menu1'),
    path('menu2/', views.menu2, name='Menu2'),
    path('menu3/', views.menu3, name='Menu3'),
    path('menu4/', views.menu4, name='Menu4'),
    path('menu5/', views.menu5, name='Menu5'),
    path('comprobacion/', views.comprobacion, name='Comprobacion'),
    path('borrar_ultima_pizza/', views.borrar_ultima_pizza, name='borrar_ultima_pizza'),
]