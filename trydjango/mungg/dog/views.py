from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from accounts.models import *

# Create your views here.

#강아지메인홈
def home(request):
    return render(request, 'doghome.html')



# 강아지등록
def dogregister(request):
    if request.method == 'POST':
        # dog = Puppy.objects.create_user(
        name=request.POST['name'],
        kind =request.POST['kind'],
        Primary_weight = request.POST['Primary_weight'],
        gender = request.POST['gender'],
        neutralization = request.POST['neutralization'],
        birth_date = request.POST['birth_date'],
        user_id = MyUser.objects.get('user_id')
                                        
        dog = Puppy(
            name=name,
            kind=kind,
            Primary_weight=Primary_weight,
            gender=gender,
            neutralization = neutralization,
            birth_date=birth_date,
            user_id=user_id
            )
        dog.save()
        # auth.login(request, user)
        return redirect('doghome')
    return render(request, 'dogregister.html')