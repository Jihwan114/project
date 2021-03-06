from django.shortcuts import render, redirect
from accounts.models import *
from dog.models import *
from .models import *

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdate
import numpy as np


def weightregister(request):  #다영이
    if request.user.is_authenticated:

        ##STEP0. 로그인 사용자가 선택한 강이지 이름 세션값 가져오기 
        selected_puppy_name = request.session.get('selected_puppy_name')
        print("TEST2")
        print(type(selected_puppy_name))
        selected_puppy_queryset = Puppy.objects.filter(name__contains=selected_puppy_name)
        print(selected_puppy_queryset)
        selected_puppy_object = selected_puppy_queryset[0]
        selected_puppy_animal_id = selected_puppy_object.animal_id

        if request.method == 'POST':
            puppy=selected_puppy_object
            date=datetime.datetime.now().date(),
            weight = request.POST['fname'],
            # print(weight)
            #개별몸무게객체 생성
            nowweight = IndiWeight.create_weight(
                puppy=selected_puppy_object,
                date=date,
                weight=float(weight[0]),
                )



def compare_puppy_weight(request):

    #사용자가 로그인했는지 확인
    if request.user.is_authenticated:

        ##STEP0. 로그인 사용자가 선택한 강이지 이름 세션값 가져오기 
        selected_puppy_name = request.session.get('selected_puppy_name')
        print("TEST2")
        print(selected_puppy_name)

        ##STEP1. 선택된 강아지 정보 불러오기
        #선택된 강아지 객체 가져오기
        if selected_puppy_name is None:
            pass
        else:
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
            #특수문자 제거하고 품종만 출력 (type=string)
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

            #STEP2-2.카테고리별 최소, 최대 평균값 가져오기 
            #type = queryset
            avg_queryset = Kindage.objects.filter(kind__contains = modified_p_kind, age = dog_age)
            print("avg_queryset")
            print(avg_queryset)
            
            #type_conversion = From queryset To object
            avg_object = avg_queryset[0]
            
            #최소, 최대값 변수 지정
            selected_puppy_avg_min = avg_object.min
            selected_puppy_avg_max = avg_object.max
            print(selected_puppy_avg_min)
            print(selected_puppy_avg_max)


            #STEP3. 사용자로부터 입력받은 현재 몸무게 가져오기 
            user_input_puppy_weight = request.session.get('input_puppy_weight')
            print("INPUT_WEIGHT")
            print(user_input_puppy_weight)


            #STEP4. 
            category_names = ['lack', 'good', 'too much']
            results = {'pupy': [selected_puppy_avg_min, selected_puppy_avg_max-selected_puppy_avg_min, selected_puppy_avg_min]}
            print("STEP4")

            #STEP5.
            labels = list(results.keys())
            data = np.array(list(results.values()))
            data_cum = data.cumsum(axis=1)
            category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))
            print("STEP5")

            #STEP6.
            fig, ax = plt.subplots(figsize=(9.2, 5),facecolor=('#eafff5')) #그래프 밖 색깔지정
            ax.yaxis.set_visible(False)
            ax.set_xlim(0, np.sum(data, axis=1).max())
            colo=['#1E98FD','violet','#FF00F7']  # 축 색깔 변경
            for i, (colname, color) in enumerate(zip(category_names, category_colors)):
                widths = data[:, i]
                starts = data_cum[:, i] - widths
                rects = ax.barh(labels, widths, left=starts, height=0.5,
                                label=colname, color=colo[i])
            print("STEP6")

            ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                    loc='lower left', fontsize='small')
            print("STEP6-1")

            #STEP7.
            plt.axvline(x=float(user_input_puppy_weight), color='lightgreen', linewidth=7,linestyle=(0,(5,1)))
            ax.set_facecolor('#eafff5') #그래프내 배경색
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_color('tab:orange')#축 색 변경
            ax.margins(x=0,y=0.3)
            ax.annotate('Now_Dog_Weight',((float(user_input_puppy_weight)+0.1),0.29),fontsize=15,color='tab:orange')
            print("STEP7")

            ax.tick_params(labelcolor='tab:orange',color='tab:orange')
            print("STEP7-1")

            #LAST_STEP
            print("TEST_SAVE")
            now_date = datetime.datetime.now().strftime('%Y-%m-%d')
            modified_p_name = selected_puppy_object.name[2:-3]
            print(modified_p_name)
            file_name = modified_p_name + now_date
            fig.savefig('/Users/jihwanseok/Desktop/project/trydjango/mungg/weight_compare/static/img/Now_Dog_Weight.jpg')



    return render(request, 'weight_compare/compare.html')




def make_graph_weight(request):
    list=[]
    selected_puppy_name = request.session.get('selected_puppy_name')
    print(selected_puppy_name)
    selected_puppy_queryset = Puppy.objects.filter(name=selected_puppy_name)
    selected_weight=IndiWeight.objects.filter(puppy=selected_puppy_queryset[0])
    # print(selected_weight)

    xdate=[]
    ydata=[]

    for x in selected_weight:
        xdate.append(x.date)
        ydata.append(x.weight)

    print(xdate)
    print(ydata)


    xlims = mdate.date2num([xdate[0], xdate[-1]])
    _, yv = np.meshgrid(np.linspace(0,1,210), np.linspace(0,1,90))


    fig, ax = plt.subplots(figsize=(9.2,5),facecolor=('#eafff5'))

    ax.plot(xdate, ydata, color='fuchsia',linewidth=4,alpha=0.4, label = 'My Strategy')
    extent = [xlims[0], xlims[1], 0, 1.4*max(ydata)]
    ax.imshow(yv, cmap=mpl.cm.RdPu, origin='lower',alpha = 0.5, aspect = 'auto',
              extent = [xlims[0], xlims[1], 0, max(ydata)])
    ax.fill_between(xdate, ydata, max(ydata), color='#eafff5')
    ax.set_facecolor('#eafff5')
    plt.yticks(color = 'gray')
    plt.xticks(color = 'gray',rotation = 15)
    plt.ylim(0,1.4*max(ydata))
    fontdict = {"family":"Times New Roman", 'size':12, 'color':'gray'} #Times New Roman, Arial
    # plt.title("Dog Wight ", fontdict = fontdict) 제목
    # plt.xlabel("date(day)", fontdict = fontdict)
    # plt.ylabel("Weight", fontdict = fontdict)

    # 축이름 변경
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgray')
    #축위치설정
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))


    # timedelta = (xdate[-1] - xdate[0]) / 10
    # plt.xticks(mdate.drange(xdate[0], xdate[-1], timedelta))
    # 分成 10 份
    delta = round(len(xdate) / 9)
    # plt.xticks([xdate[i*delta] for i in range(9)] + [xdate[-1]])#x 축 범위 정하기

    # plt.yticks(np.linspace(min(ydata), max(ydata), 5))  #y축 범위정하기
    plt.tick_params(left = 'off')
    plt.tick_params(which = 'major', direction = 'out', width = 0.2, length = 5) # in, out or inout

    plt.grid(axis = 'y', color = 'lightgray', linestyle = '-', linewidth = 0.5)

    # plt.legend(loc = 'best', fontsize = 12, frameon=False, ncol = 1)
    fig.savefig('/Users/jihwanseok/Desktop/project/trydjango/mungg/weight_compare/static/accumulate_img/weight12.jpg')
    plt.show()
