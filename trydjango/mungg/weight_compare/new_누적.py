import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import matplotlib.dates as mdate
import numpy as np
import matplotlib as mpl
import pymysql
def make_graph_weight(animal_id):
    list=[]

    mydb = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="kjs1058815!",
        db="hana_db",
        charset="utf8")
    mycursor = mydb.cursor()

    sql ="SELECT * from 몸무게"   #강아지 있는 테이블
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for x in result:
        if animal_id==x[0]:
            list.append(x)

    list.sort(key=lambda x:x[1])

    xdate=[]
    ydata=[]

    for i in list:
        xdate.append(i[1])
        ydata.append(i[2])


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
    # plt.title("Dog Weight ", fontdict = fontdict) 제목
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
    fig.savefig('weight12.jpg')
    plt.show()


make_graph_weight('kimjs0911')
