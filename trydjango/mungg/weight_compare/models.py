from django.db import models

# Create your models here.

class Kindage(models.Model):
    num = models.IntegerField(db_column='Num', blank=True, primary_key=True)  # Field name made lowercase.
    kind = models.TextField(db_column='Kind', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kindage'