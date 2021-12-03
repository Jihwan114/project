import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from accounts.models import *
from dog.models import *
from django.db.models import Count
from django.contrib import messages
from weight_compare.views import *
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
        ##홈 화면 오른쪽 강아지 선택 리스트 생성 과정##
        #step1.로그인한 유저의 강아지 객체 불러오기 

        queryset = Puppy.objects.filter(user_id_id=now_user_id)
        print(len(queryset))

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


        #홈화면 우측 상단 선택된 강아지 정보 가져오기
        #사용자가 등록한 강아지가 1마리인 경우
        if len(queryset) == 1:
                selected_puppy_name = puppy_name_list[0]
                request.session['selected_puppy_name'] = selected_puppy_name
        #사용자가 등록한 강아지가 2마리 이상인 경우
        else:
            if request.user.is_authenticated and request.method == 'GET':
                #home.html input value 받기 
                selected_puppy_name = request.GET.get('dog')
                #선택된 강아지 이름 세션값 저장
                request.session['selected_puppy_name'] = selected_puppy_name
                print("TEST1")
                print(selected_puppy_name)


    #회원인지 물어보는 팝업 
    if request.user.is_authenticated:
        return render(request, 'dashboard/home.html',
                            {'countingUser':countingUser, 
                    'countingPuppy':countingPuppy, 
                    'puppy_name_list_modified':puppy_name_list_modified,
                    'now_user_id':now_user_id,
                    }
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
        input_puppy_weight = request.POST.get('fname')
        request.session['input_puppy_weight'] = input_puppy_weight
        print("TEST_INPUT_WEIGHT.VIEW.DASHBOARD")
        print(input_puppy_weight)
        #현재 몸무게 평균 비교하는 그래프
        compare_puppy_weight(request)
        #몸무게 테이블에 입력된 몸무게 누적 
        weightregister(request)
        make_graph_weight(request)
        return render(request, 'weight_compare/compare.html')
        
    return render(request, 'dashboard/강아지몸무게.html')

#근처 동물 병원
def aroundhospital(request):
    return render(request, 'dashboard/주변동물병원.html')

#강아지 키우는 방법
def well_with_puppy(request):
    return render(request, 'dashboard/생활팁.html')


def check_health_schedule(request):
    #홈에서 사용자가 선택한 강아지 이름 가져오기 
    selected_puppy_name = request.session.get('selected_puppy_name')
    
    #강아지 이름으로 선택된 강아지 쿼리 출력
    selected_puppy_queryset = Puppy.objects.filter(name__contains = selected_puppy_name)
    #출력된 쿼리에서 객체 출력
    selected_puppy_object = selected_puppy_queryset[0]
    #강아지 객체의 출생년도 출력
    selected_puppy_b_day = selected_puppy_object.birth_date

    # print(selected_puppy_b_day)
    # print(type(selected_puppy_b_day))

    #출생연도
    puppy_b_day_year = selected_puppy_b_day.strftime('%Y')
    #출생 월
    puppy_b_day_month = selected_puppy_b_day.strftime('%m')
    #출생 일 
    puppy_b_day_date = selected_puppy_b_day.strftime('%d')
    
    # print(puppy_b_day_year)
    # print(puppy_b_day_month)    
    # print(puppy_b_day_date)

    
    return render(request, 'dashboard/건강검진일정.html', {'puppy_b_day_year':puppy_b_day_year, 
                                                        'puppy_b_day_month':puppy_b_day_month,
                                                        'puppy_b_day_date':puppy_b_day_date})

