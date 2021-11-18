from django.urls import path
from . import views

urlpatterns = [
    path('weight_compare/', views.weight_compare, name="weight_compare"),
]
