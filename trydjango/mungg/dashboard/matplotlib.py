import matplotlib.pyplot as plt


# Create your tests here.

def matplotlib_graph(request):
    a=4
    b=7
    fig, ax = plt.subplots()
    dog_w = weight #강아지 현재 몸무게
    print(dog_w+"KG")

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
    plt.show()
    f=plt.figure()
    
    fig.savefig('/Users/jihwanseok/Desktop/project/trydjango/mungg/dashboard/static/images')