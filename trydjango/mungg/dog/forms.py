from django.forms import ModelForm
from .models import *

class DogForm(ModelForm):
    class Meta:
        model = Puppy
        fields = ['name', 'kind','Primary_weight','gender','neutralization','birth_date']

# form = DogForm()
                                      