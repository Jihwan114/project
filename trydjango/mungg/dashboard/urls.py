from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('weight/', views.checktheweight, name="weight"),  
    path('hospital/', views.aroundhospital, name="hospital"),  
    path('tip/', views.well_with_puppy, name="tip"),    
    path('schedule/', views.check_health_schedule, name="schedule"), 
]
