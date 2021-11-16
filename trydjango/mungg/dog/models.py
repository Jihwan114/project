from django.db import models
from .models import *
from accounts.models import MyUser

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
    birth_date = models.DateTimeField (auto_now_add=False)
    #동물ID
    animal_id = models.CharField(max_length=200, primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete = models.PROTECT)

    def __str__(self):
        return self.name
