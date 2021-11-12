from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('map/', views.map, name="map"),
    path('main/', views.map, name="main"),
    
]
