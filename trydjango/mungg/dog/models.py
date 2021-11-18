from django.db import models
from .models import *
from accounts.models import MyUser
from django.conf import settings
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class Puppy(models.Model):
    #이름
    name = models.CharField(max_length=200, null=True)
    #품종
    kind = models.CharField(max_length=200, null=True)
    Primary_weight = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    #중성화유무
    neutralization = models.BooleanField(default=True)
    birth_date = models.DateTimeField (default=now, editable=True)
    #동물ID
    animal_id = models.CharField(max_length=200, primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def create_puppy(name, kind, Primary_weight, gender, neutralization, birth_date, animal_id, user_id):
        if not name:
            raise ValueError('name is required.')
        
        puppy = Puppy(
            name=name,
            kind=kind,
            Primary_weight=Primary_weight,
            gender=gender,
            neutralization=neutralization,
            birth_date=birth_date,
            animal_id=animal_id,
            user_id=user_id
        )
        puppy.save()
        
        return puppy


