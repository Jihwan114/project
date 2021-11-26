import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from accounts.models import *
from dog.models import *
from django.db.models import Count
from django.contrib import messages
import datetime

# Create your views here.

# Home 화면 구성 및 유저 수 최신화 
def home(request):
    #메인화면 상단에 유저 숫자 나타내기 
    countingUser = MyUser.objects.count()

    #강아지 객체 수 생성
    countingPuppy = Puppy.objects.count()
    

    #홈 화면 오른쪽 사용자 이름 표시
    #step1. 로그인 했는지 확인 
    if request.user.is_authenticated:
        now_user_id = request.user.user_id
        

        #####################################
        ###홈 화면 오른쪽 강아지 선택 이름 생성 과정###
        #step1.로그인한 유저의 강아지 객체 불러오기 

        queryset = Puppy.objects.filter(user_id_id=now_user_id)

        #step2.강아지 객체에서 name 불러와서 리스트 만들기 
        puppy_name_list = []
        for obj in queryset:
            puppy_name_list.append(obj.name)
            
        #step3.불러온 강아지 이름들 특수문자 제거 
        puppy_name_list_modified = []
        specialcharacter = "(),\'"
        for j in puppy_name_list:
            for i in range(len(specialcharacter)):
                j = j.replace(specialcharacter[i],'')
            puppy_name_list_modified.append(j)
        #####################################



    #회원인지 물어보는 팝업 
    if request.user.is_authenticated:
        return render(request, 'dashboard/home.html',
                            {'countingUser':countingUser, 
                    'countingPuppy':countingPuppy, 
                    'puppy_name_list_modified':puppy_name_list_modified,
                    'now_user_id':now_user_id}
                    )
    else:
        # messages.info(request, '멍바디에 회원가입 하시겠습니까?')
        return render(request, 'dashboard/home.html', 
                    {'countingUser':countingUser, 
                    'countingPuppy':countingPuppy, 
                    # 'puppy_name_list_modified':puppy_name_list_modified,
                    # 'now_user_id':now_user_id},
                    }
                    )


#강아지 몸무게 입력받기 
def checktheweight(request):
    if request.method == 'POST':
        puppy_weight = request.POST.get('fname')
        print(puppy_weight)
        
    return render(request, 'dashboard/강아지몸무게.html')

#근처 동물 병원
def aroundhospital(request):
    return render(request, 'dashboard/주변동물병원.html')

#강아지 키우는 방법
def well_with_puppy(request):
    return render(request, 'dashboard/생활팁.html')


def check_health_schedule(request):
    return render(request, 'dashboard/건강검진일정.html')

