import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from accounts.models import *
from django.db.models import Count
from django.contrib import messages

# Create your views here.
# Home 화면 구성 및 유저 수 최신화 
def home(request):
    #메인화면 상단에 유저 숫자 나타내기 
    countingUser = MyUser.objects.count()
    #회원인지 물어보는 팝업
    messages.info(request, '멍바디에 회원가입 하시겠습니까?')

    return render(request, 'dashboard/home.html', {'countingUser':countingUser})

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


def make_graph(request):
    a=4
    b=7
    fig, ax = plt.subplots()
    dog_w = 50 #강아지 현재 몸무게
    
    ax.broken_barh([(0, a), (a, b-a), (b, 2*b)], (10, 9),
                facecolors=('blueviolet', 'mediumspringgreen', 'tomato'))
    ax.set_ylim(5, 20)
    ax.set_xlim(0, 2*b)
    ax.set_xlabel('compare weight')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Bill', 'Jim'],color='white')
    ax.grid(False)
    ax.annotate('your dog', (int(dog_w), 15),
                xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops=dict(facecolor='dodgerblue', shrink=0.05),
                fontsize=15,
                horizontalalignment='right', verticalalignment='top')
    plt.style.use('seaborn')
    # plt.show()
    f=plt.figure()
    
    fig.savefig('/Users/jihwanseok/Desktop/project/trydjango/mungg/dashboard/static/images')

    return render(request, 'dashboard/matplotlib.html')

    
 