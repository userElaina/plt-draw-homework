import os
from copy import deepcopy as dcp
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)
# 不使用科学计数法(方便debug)
normalization=False
# 是否标准化
debug=False
# debug=True
# show or save

dirpath=os.path.dirname(__file__)
csvpath=os.path.join(dirpath,'WineQT.csv')

a=[i.split(',')[:-1] for i in open(csvpath,'rb').read().decode('utf-8').splitlines()]
# split by \n, the splt by ,

names=[i.lower().replace(' ','_') for i in a[0]]
# the first line

a=np.array([[float(j) if '.' in j else int(j) for j in i] for i in a[1:-1]])

# print(a.shape)
# for i in b:
#     print(i.shape)
# print(type(a),type(a[0]),type(a[0][0]))

# 固定酸度 挥发性酸度 柠檬酸 残糖
# 氯化物 游离二氧化硫 总二氧化硫 密度
# pH 硫酸盐 酒精 质量

means=list(a.mean(axis=0))
# per col
mins=list(a.min(axis=0))
maxs=list(a.max(axis=0))
lens=[maxs[i]-mins[i] for i in range(12)]

a_n=np.array([[(j-mins[_j])/lens[_j] if _j<11 else j for _j,j in enumerate(i)] for i in a])

b=[np.array([j[:-1] for j in a_n if j[-1]==i]) for i in range(3,9)]
meanb=[list(i.mean(axis=0)) for i in b]

if normalization:
    a=a_n
    means=list(a.mean(axis=0))
    mins=[0.0]*11+[3,]
    maxs=[1.0]*11+[8,]
    lens=[1.0]*11+[5,]

    ticks1=[[0.0,0.2,0.4,0.6,0.8,1.0],]*11+[[3,4,5,6,7,8],]
    ticks2=[[str(j) for j in i] for i in ticks1]

# if debug:
#     for i in range(len(means)):
#         print(names[i],means[i],mins[i],maxs[i])

'''
fixed acidity 8.313222416812618 4.6 15.9
volatile acidity 0.5312390542907177 0.12 1.58
citric acid 0.26849387040280115 0.0 1.0
residual sugar 2.532618213660242 0.9 15.5
chlorides 0.08694308231173353 0.012 0.611
free sulfur dioxide 15.601138353765323 1.0 68.0
total sulfur dioxide 45.916374781085814 6.0 289.0
density 0.9967315148861652 0.9900700000000001 1.00369
pH 3.3107880910683027 2.74 4.01
sulphates 0.657661996497373 0.33 2.0
alcohol 10.442323409223569 8.4 14.9
quality 5.657618213660245 3.0 8.0
Id 804.2758318739054 0.0 1595.0
'''
ticks1=[
    np.arange(4,20,4),
    np.arange(0,2,0.4),
    np.arange(0,1.2,0.2),
    np.arange(0,20,4),
    np.arange(0,1,0.2),
    np.arange(0,80,10),
    np.arange(0,320,80),
    np.arange(0.991,1.005,0.002),
    np.arange(2.4,4.8,0.6),
    np.arange(0,2.4,0.6),
    np.arange(8,18,2),
    np.arange(3,9,1),
]

ticks1=[list(i) for i in ticks1]

ticks2=list()
for i in ticks1:
    __mx=-1
    for j in i:
        __l=len(str(j).split('.')[-1])
        if __l>__mx:
            __mx=__l
    ticks2.append([str(round(j,__mx)) for j in i])
# convert to string
# labels

def show(
    t:str,
    i0:int=None,
    i1:int=None,
    i2:int=None,
    clear:bool=True,
    width:int=4,
    height:int=4,
    dpi:int=256,
):
    n=t
    if i0 is not None:
        t+='-'+str(i0)
        # t+='-'+names[i0]
    if i1 is not None:
        t+='-'+str(i1)
        # t+='-'+names[i1]
    if i2 is not None:
        t+='-'+str(i2)
        # t+='-'+names[i2]

    plt.title(t)
    if debug:
        plt.show()
    figure=plt.gcf()
    '''
    Get the current figure.
    If there is currently no figure on the pyplot figure stack, a new one is created using ~.pyplot.figure(). (To test whether there is currently a figure on the pyplot figure stack, check whether ~.pyplot.get_fignums() is empty.)
    '''
    figure.set_size_inches(width,height)
    plt.savefig(os.path.join(dirpath,'img',t+'.png'),dpi=dpi)
    if clear:
        plt.close()
        plt.clf()
        # clear the figure

def scatter(x:int,y:int=11):
    X=a[:,x]
    Y=a[:,y]
    C=a[:,-1]
    plt.axes([0.05,0.05,0.9,0.9])
    # [图片位移x,y,缩放比例x,y]

    plt.scatter(X,Y,s=20,c=C,alpha=0.75,marker='.',linewidths=0)
    '''
    用于在图像中绘制散点
    x/y: 都是向量形式, 且维度相同, 分别对应坐标点的横纵坐标
    s: 标记大小, 以平方磅为单位的标记面积
    c: color
    marker: 
    '''

    plt.xlim(mins[x]-lens[x]/20,maxs[x]+lens[x]/20)
    plt.ylim(mins[y]-lens[y]/20,maxs[y]+lens[y]/20)
    '''ylim
    axis range
    '''

    plt.xticks(ticks1[x],ticks2[x])
    plt.yticks(ticks1[y],ticks2[y])
    '''yticks
    axis label
    '''

    show('scatter',x,y)


def histogram(x:int):
    plt.hist(a[:,x],bins=10,facecolor='blue',edgecolor='black',alpha=0.75,)
    '''
    绘制直方图
    bins: 直方图的长条形数目, 可选项, 默认为10
    normed: 是否将得到的直方图向量归一化, (0,1)
    facecolor: fill
    edge
    '''

    plt.xlabel(names[x])
    plt.ylabel('Frequency')
    show('histogram',x)

def column():
    X=[len(i) for i in b]
    C=list('rygcbm')
    # color
    plt.bar(range(3,9),X,alpha=0.75,color=C,hatch='*',ec=C[3:]+C[:-3],ls='--',lw=2)
    '''
    ec: edge color
    ls: line shape
    lw line width
    '''
    show('column')

def columns():
    X=range(0,88,8)
    # 11 * 8
    C=list('rygcbm')
    w=1
    rects=list()
    for i in range(6):
        rects.append(plt.bar(
            [j+w*i for j in X], # start x
            height=meanb[i],
            width=w,
            alpha=0.75,
            color=C[i],
            label=str(i+3)
        ))

    plt.ylabel('Normalized Value')
    plt.xticks([index+4 for index in X],[i.replace('_','\n') for i in names[:-1]])
    plt.xlabel('Properties')
    plt.legend()

    show('columns',width=16,height=8)


def boxplot():
    X=a_n[:,:-1]
    plt.boxplot(X,labels=names[:-1],vert=False,showmeans=True)
    '''
    vert: 水平 or 垂直
    '''
    show('boxplot',width=16,height=8)

def line(x:int):
    import matplotlib.pyplot as plt

    X=range(3,9)
    Y=[i[x] for i in meanb]
    plt.plot(X,Y,'ro-',markersize=5,alpha=0.75)
    # ro- red shape line-shape
    plt.xlabel('Quality')
    plt.ylabel(names[x])
    show('line',x)

def pie():
    X=[len(i) for i in b]
    C=list('rygcbm')
    explode=[0.05,0,0,0,0,0]
    # 各部分突出值
    plt.pie(
        X,
        explode=explode,
        colors=C,
        labels=range(3,9),
        labeldistance=0.5, # 设置标签文本距圆心位置, 1.1表示1.1倍半径
        autopct="%1.1f%%", # 设置圆里面文本
        shadow=True,
        startangle=90,
        pctdistance=1.05
    )
    '''
    绘制饼图
    explode: 设置各部分突出
    labeldistance: 设置标签文本距圆心位置, 1.1表示1.1倍半径
    autopct: 设置圆里面文本
    startangle: 起始角度, 默认从0开始逆时针转
    pctdistance: 设置圆内文本距圆心距离
    '''
    plt.axis('equal') # set circle
    plt.legend()
    show('pie',width=8,height=8)

def nightingale():
    Y=[len(i) for i in b]
    N=6
    X=np.linspace(0,2*np.pi,N,endpoint=False)
    # 
    C=list('rygcbm')
    
    ax=plt.subplot(111,projection='polar')
    ax.bar(X,Y,color=C,width=2*np.pi/N,bottom=90)
    # 哪个角度画,长度,扇形角度,从距离圆心90的地方开始画

    show('polar')

def radar(x:int):
    name=names[:-1]
    X=np.linspace(0,2*np.pi,len(name),endpoint=False)
    #将圆根据标签的个数等比分
    Y=meanb[x]
    X=np.concatenate((X,[X[0]]))
    Y=np.concatenate((Y,[Y[0]]))
    name=np.concatenate((name,[name[0]]))
    #闭合

    ax=plt.subplot(111,projection='polar')
    ax.plot(X,Y,'g-',lw=1,alpha=0.75)
    # green -
    # line width
    ax.fill(X,Y,'g',alpha=0.75)
    ax.set_thetagrids(X*180/np.pi,name)
    #替换标签
    ax.set_ylim(0,1)
    #设置极轴的区间
    ax.set_theta_zero_location('N')
    #设置极轴方向
    show('radar',x,width=8,height=8)

def contour(x:int,y:int):
    _x=a_n[:,x]
    _y=a_n[:,y]
    X=np.arange(0.1,1,0.2)
    Y=np.arange(0.1,1,0.2)
    X,Y=np.meshgrid(X,Y)
    # 网格化
    # X: (1,2,3) -> ((1,2,3),(1,2,3),(1,2,3))
    # Y: (1,2,3) -> ((1,1,1),(2,2,2),(3,3,3))

    maps=np.zeros((len(X),len(Y)))
    for i in a_n:
        maps[min(4,int(i[x]*5)),min(4,int(i[y]*5))]+=1

    plt.contourf(X,Y,maps)
    # fill
    plt.contour(X,Y,maps,colors='black')
    # line
    show('contour',x,y)

if __name__ == '__main__':
    # 散点图
    # for i in range(11):
    #     for j in range(11):
    #         if i==j:
    #             continue
    #         scatter(i,j)

    # 柱状图
    # column()

    # 分组柱状图
    # columns()

    # 直方图
    # for i in range(11):
    #     histogram(i)

    # 箱线图
    # boxplot()

    # 折线图
    # for i in range(11):
    #     line(i)

    # 饼图
    # pie()

    # 玫瑰图
    # nightingale()

    # 雷达图
    # for i in range(6):
    #     radar(i)

    # 地形图
    for i in range(11):
        for j in range(11):
            contour(i,j)

# qwq

'''
酒精度数, 与品质呈正相关关系, 度数越高品质趋向升高;
挥发性酸, 与品质呈负相关关系, 酸度越高品质趋向降低;
硫酸盐, 与品质呈正相关关系, 硫酸盐越多品质趋向升高;
柠檬酸, 与品质呈正相关关系, 酸度越高品质趋向降低;
'''