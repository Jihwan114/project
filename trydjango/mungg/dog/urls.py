from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('dogregister/', views.dogregister, name="dogregister"),
]
