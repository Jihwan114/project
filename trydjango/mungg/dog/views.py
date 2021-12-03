from django.contrib import auth
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Count
from weight_compare.models import * 
# from accounts.models import *


#########################
# 강아지등록
def dogregister(request):
    if request.method == 'POST':
        name=request.POST['name'],
        kind =request.POST['kind'],
        Primary_weight = request.POST['Primary_weight'],
        print("TEST_PRIMARY")
        print(Primary_weight)
        print(type(Primary_weight))
        name=name[0]
        kind=kind[0]

        #성별 입력에 따른 구분 
        if request.POST['gender'] == "on":
            gender = "Male"
        else: 
            gender = "Female"

        #중성화여부 boolean 값 분류 
        if request.POST['neutralization'] == "on":
            neutralization = True
        else:
            neutralization = False

        #datetimeField type 튜플, 인덱싱 
        birth_date = request.POST['birth_date']
        if type(birth_date) == tuple :
            birth_date = birth_date[0]

        주인아이디 = request.POST['user_id']

        user_id = MyUser.objects.get(user_id=주인아이디)

        #강아지 객체 생성
        puppy = Puppy.create_puppy(
            name=name,
            kind=kind,
            Primary_weight=Primary_weight[0],
            gender=gender,
            neutralization = neutralization,
            birth_date=birth_date,
            #animal_id=animal_id,
            user_id=user_id
            )
        puppy.save()
        #P_COUNT = Puppy.objects.count()


        pweight= IndiWeight.create_weight(    #다영이
            puppy=puppy,
            date=datetime.now().date(),
            weight=float(puppy.Primary_weight),
        )

        return redirect('home')
        
    #강아지 품종별 선택
    kinds = PuppyKind.objects.all().order_by('kind')
    print(kinds)
    context = {'kinds':kinds}

    return render(request, 'dogregister.html', context)
