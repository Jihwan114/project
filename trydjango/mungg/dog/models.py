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

#모든강아지 품종,평균몸무게 table
class puppy_kind(models.Model):
    kind = models.TextField(blank=True, null=False, primary_key=True)
    section = models.TextField(blank=True, null=True)
    label_3 = models.TextField(db_column='LABEL-3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    label_4 = models.TextField(db_column='LABEL-4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smallavg_kg_field = models.IntegerField(db_column='smallavg(kg)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bigavg_kg_field = models.IntegerField(db_column='bigavg(kg)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'puppy_kind'
