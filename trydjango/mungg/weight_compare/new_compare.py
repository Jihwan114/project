import numpy as np
import pymysql
import matplotlib.pyplot as plt, mpld3
import numpy as np
import datetime



def find_dog_data(animal_id):
    mydb = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="kjs1058815!",
        db="hana_db",
        charset="utf8")
    mycursor = mydb.cursor()

    sql ="SELECT * from pupy"   #강아지 있는 테이블
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for x in result:
        if animal_id==x[0]:
            dogname=x[1] #강아지 품종 있는 인덱스
            dog_birth=x[2] #강아지 생년월일 있는 인덱스, type은 datetime으로 가정한다.
            break
    #a 정상 몸무게 낮은값
    #b 정상 몸무게 높은값
    dog_age_dif=datetime.datetime.now()-dog_birth   #현재 나이계산.
    dog_age_day=int(dog_age_dif.days)

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

    sql ="SELECT * from dog_average"
    mycursor.execute(sql)
    # dog_name='아펜핀셔 (AFFENPINSCHER)'# 강아지 현재 이름 가저오기
    # dog_age# 강아지 현재 나이를 구분화한 등급
    result = mycursor.fetchall()

    for x in result:
        if dogname==x[0] and dog_age==x[1]:
            a=x[3]
            b=x[4]
            break
    #a 정상 몸무게 낮은값
    #b 정상 몸무게 높은값
    return a,b




 #강아지 현재 몸무게



def make_graph(animal_id,input_w):
    #animal_id =>pupuy id
    #input_w=>강아지 몸무게 현재값
    a,b=find_dog_data(animal_id)
    category_names = ['lack', 'good',
                      'too much']
    results = {'pupy': [a, b-a, a]}


    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5),facecolor=('#eafff5')) #그래프 밖 색깔지정
    ax.yaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    colo=['#1E98FD','violet','#FF00F7']  # 축 색깔 변경
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=colo[i])

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    plt.axvline(x=float(input_w), color='lightgreen', linewidth=7,linestyle=(0,(5,1)))
    ax.set_facecolor('#eafff5') #그래프내 배경색
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('tab:orange')#축 색 변경
    ax.margins(x=0,y=0.3)
    ax.annotate('your dog',((float(input_w)+0.1),0.29),fontsize=15,color='tab:orange')

    ax.tick_params(labelcolor='tab:orange',color='tab:orange')


    fig.savefig('newdog_compare33.jpg')
    # f=plt.figure()
    # mpld3.fig_to_html(f, figid='compa'))
    return fig, ax


make_graph('kimjs0912',0.3)
plt.show()
