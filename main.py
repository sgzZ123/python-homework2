from search import *
from database import *
import sys
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 构建类
    #s = scraper()
    o = Operator('1')

    # 获得1999-2017年的年龄结构数据，并存入数据库的agestructure表
    #l = s.GetInfomation('agestructure', [i for i in range(1999, 2018)])
    #if l == -1:
     #   print('failed to connect')
      #  sys.exit()
    #o.CreateNewTable('agestructure',l[0].keys())
    #o.InsertInfo('agestructure', l)
    # 从数据库中读取agestructure表
    d1 = o.GetData('agestructure')
    print(d1)

    # 获得1999-2018年的人口数据，并存入数据库的popularity表
    #l = s.GetInfomation('popularity', [i for i in range(1999, 2019)])
    #if l == -1:
     #   print('failed to connect')
      #  sys.exit()
    #o.CreateNewTable('popularity', l[0].keys())
    #o.InsertInfo('popularity', l)
    # 从数据库中读取popularity表
    d2 = o.GetData('popularity')
    print(d2)

    # 构建人口图的横轴（年份）和纵轴（总人口，男性人口占比，女性人口占比）
    axes_Year2 = [int(data['year']) for data in d2]
    axes_population = [int(data['年末总人口']) for data in d2]
    axes_MenPart = [int(data['男性人口']) / int(data['年末总人口']) * 100 for data in d2]
    axes_WomenPart = [int(data['女性人口']) / int(data['年末总人口']) * 100 for data in d2]

    # 构建年龄结构图的横轴（年份）和纵轴（三个年龄段比例）
    axes_Year1 = [int(data['year']) for data in d1]
    axes_KidPart = [int(data['0-14岁人口']) / int(data['年末总人口']) * 100 for data in d1]
    axes_MidPart = [int(data['15-64岁人口']) / int(data['年末总人口']) * 100 for data in d1]
    axes_OldPart = [int(data['65岁及以上人口']) / int(data['年末总人口']) * 100 for data in d1]
    # 查找2016年的各年龄段人口比例
    for data in d1:
        if data['year'] == '2016':
            population = int(data['年末总人口'])
            KidPart_2016 = int(data['0-14岁人口']) / population * 100
            MidPart_2016 = int(data['15-64岁人口']) / population * 100
            OldPart_2016 = int(data['65岁及以上人口']) / population * 100
            break
    # 饼图标签
    labels = '0-14', '15-64', 'above 65'
    try:
        size = [KidPart_2016, MidPart_2016, OldPart_2016]
    except TypeError:
        sys.exit()

    # 图1，1999-2018年男性和女性人口比例变化折线图
    plt.figure(1)
    plt.title('the women and men part of 1999 - 2018')
    plt.plot(axes_Year2, axes_MenPart, label='Men part')
    plt.plot(axes_Year2, axes_WomenPart, label='Women part')
    plt.xlabel('year')
    plt.ylabel('patition')
    plt.ylim((40, 60))
    plt.xticks(axes_Year2, rotation=45)
    plt.legend(loc='upper left')
    plt.show()

    # 图2，1999-2018年总人口变化条形图
    plt.figure(2)
    plt.title('the population of 1999 - 2018')
    plt.xlabel('year')
    plt.ylabel('population')
    plt.bar(axes_Year2, axes_population, 0.5)
    plt.xticks(axes_Year2, rotation=45)
    plt.show()

    # 图3，2016年各年龄段人口比例扇形图
    plt.figure(3)
    plt.title('the age structure of 2016')
    plt.pie(size, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    # 图4，1999-2017年各年龄段人口比例折线图
    plt.figure(4)
    plt.title('the change of age structure between 1999 - 2017')
    plt.xlabel('year')
    plt.ylabel('part')
    plt.plot(axes_Year1, axes_KidPart, label='0-14')
    plt.plot(axes_Year1, axes_MidPart, label='15-64')
    plt.plot(axes_Year1, axes_OldPart, label='above 65')
    plt.xticks(axes_Year1, rotation=45)
    plt.legend(loc='upper left')
    plt.show()