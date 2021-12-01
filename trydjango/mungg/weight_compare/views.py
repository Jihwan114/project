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

        ##STEP0. 로그인 사용자가 선택한 강이지 이름 세션값 가져오기 
        selected_puppy_name = request.session.get('selected_puppy_name')
        print("TEST2")
        print(selected_puppy_name)

        ##STEP1. 선택된 강아지 정보 불러오기
        #선택된 강아지 객체 가져오기 
        selected_puppy_queryset = Puppy.objects.filter(name__contains=selected_puppy_name)
        #From queryset To object
        selected_puppy_object = selected_puppy_queryset[0]

        #STEP1-1.선택된 강아지 출생일 호출(년/월/일)
        #type = datetime.datetime
        selected_puppy_birthday = selected_puppy_object.birth_date
        #tyep = string 
        modified_b_day1 = selected_puppy_birthday.strftime('%Y-%m-%d')

        modified_b_day2 = datetime.datetime.strptime(modified_b_day1,'%Y-%m-%d')
    
        #STEP1-2.선택된 강아지 품종
        selected_puppy_kind = selected_puppy_object.kind
        #특수문자 제거하고 이름만 출력 (type=string)
        modified_p_kind = selected_puppy_kind[2:-3]
        print(modified_p_kind)
    

        #STEP2. 현재 나이 계산
        dog_age_dif=datetime.datetime.now()-modified_b_day2
        print(dog_age_dif)
        dog_age_day=int(dog_age_dif.days)
        print(dog_age_day)


        #STEP2-1. 카테고리 구간 설정
        if dog_age_day>322:
            dog_age='q'
        elif dog_age_day>308:
            dog_age='p'
        elif dog_age_day>280:
            dog_age='o'
        elif dog_age_day>252:
            dog_age='n'
        elif dog_age_day>224:
            dog_age='m'
        elif dog_age_day>196:
            dog_age='i'
        elif dog_age_day>168:
            dog_age='k'
        elif dog_age_day>140:
            dog_age='j'
        elif dog_age_day>112:
            dog_age='i'
        elif dog_age_day>105:
            dog_age='h'
        elif dog_age_day>98:
            dog_age='g'
        elif dog_age_day>91:
            dog_age='f'
        elif dog_age_day>84:
            dog_age='f'
        elif dog_age_day>77:
            dog_age='e'
        elif dog_age_day>70:
            dog_age='d'
        elif dog_age_day>63:
            dog_age='c'
        elif dog_age_day>56:
            dog_age='b'
        else:
            dog_age='a'

    return render(request, 'weight_compare/compare.html')

