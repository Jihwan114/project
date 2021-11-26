from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('home/dogregister/', views.dogregister, name="dogregister"),
]
