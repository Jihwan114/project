from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.compare_puppy_weight, name="compare"),
]



