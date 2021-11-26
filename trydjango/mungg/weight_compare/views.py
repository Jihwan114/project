from django.shortcuts import render, redirect
from accounts.models import *
from dog.models import *


import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import matplotlib.dates as mdate
import numpy as np
import matplotlib as mpl


# Create your views here.

def compare_puppy_weight(request):

    #사용자가 로그인했는지 확인
    if request.user.is_authenticated:
        now_user_id = request.user.user_id

        #로그인 사용자 강아지 분류
        queryset = Puppy.objects.filter(user_id_id=now_user_id)

        ##STEP1. 선택된 강아지 정보 불러오기
        #선택된 강아지 생년월일
        selected_puppy_birth_date = queryset[0].birth_date
        modified_b_day = selected_puppy_birth_date.strftime('%Y-%m-%d')
        
        print(modified_b_day)
        print(type(modified_b_day))

        a = datetime.datetime.strptime(modified_b_day, '%Y-%m-%d')

        print(a)
        print(type(a))



        #선택된 강아지 품종
        selected_puppy_kind = queryset[0].kind

        #STEP2. 현재 나이 계산
        print(datetime.datetime.now().date())
        print(type(datetime.datetime.now().date()))
        #now_puppy_age = datetime.datetime.now().date() - modified_b_day


        ###########################TEST########
        #강아지 몸무게 리스트
        puppy_weight_list=[]
        #강아지 id 리스트
        puppy_id_list=[]
        #강아지 id와 몸무게 분리하여 리스트에 추가
        for puppy in queryset:
            puppy_weight_list.append(puppy.Primary_weight)
            puppy_id_list.append(puppy.name)

        ######몸무게와 id 데이터 특수문자 제거#########
        puppy_weight_list_modified = []
        puppy_name_list_modified = []
        specialcharacter = "(),\'"
        #몸무게 특수문자 제거
        for j in puppy_weight_list:
            for i in range(len(specialcharacter)):
                j = j.replace(specialcharacter[i],'')
            puppy_weight_list_modified.append(j)

        #이름 특무순자 제거
        for j in puppy_id_list:
            for i in range(len(specialcharacter)):
                j = j.replace(specialcharacter[i],'')
            puppy_name_list_modified.append(j)
        ########################################

        w=puppy_weight_list_modified[0]
        n=puppy_name_list_modified[0]


    return render(request, 'weight_compare/compare.html',
    {'w':w, 'n':n})

