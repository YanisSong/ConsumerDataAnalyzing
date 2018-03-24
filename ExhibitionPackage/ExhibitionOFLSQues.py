# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


mpl.rcParams['font.sans-serif'] = ['SimHei']


def DrawAnaGraph(Dts, Dtr):
    font_size = 9
    statistics = Dts
    keys = statistics.keys()
    values = statistics.values()
    name_list = []
    ID_List = []
    ID_N_List = []
    Map_List = {}
    count = 0
    for item in keys:
        name_list.append(item)
    for i in range(1, len(name_list)+1):
        ID_List.append('No.' + str(i))
    for i in range(1, len(name_list)):
        ID_N_List.append('No.' + str(i))
    for item in ID_List:
        Map_List[item] = name_list[count]
        count += 1
    # Todo: Adding the map of id to name in the graph or find a pretty way to show the name in the graph.
    unsatisfiedValue_list = values
    satisfiedValue_list = [1-c for c in unsatisfiedValue_list]
    index_x = np.arange(len(unsatisfiedValue_list))
    total_width, n = 0.7, 2
    barWidth = total_width/n
    # Dividing the whole graph into two parts. This graph locates in the first line.
    plt.subplot(211)
    plt.rcParams['font.size'] = font_size
    plt.xlabel('调查景区')
    plt.ylabel('数值比率')
    yMajorLocator = MultipleLocator(0.2)  # Set the Y-axis main calibration label to a multiple of 0.2.
    yMinorLocator = MultipleLocator(0.02)  # Set the Y-axis scale label to a multiple of 0.02.
    ax = plt.subplot(211)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    plt.bar(index_x, unsatisfiedValue_list, width=barWidth, label='不满', fc='r')
    plt.ylim(0, 1)
    plt.bar(index_x + barWidth, satisfiedValue_list, width=barWidth, label='满意', tick_label=ID_List, fc='g')
    plt.legend(loc='lower center', bbox_to_anchor=(0.8, 1.01), fancybox=True, ncol=5)
    # Dividing the whole graph into two parts. This graph locates in the second line.
    plt.subplot(212)
    normalEvaluationNameList = Dtr.keys()
    normalEvaluationValueList = Dtr.values()
    boringEvaluationValueList = [1-num for num in normalEvaluationValueList]
    index_p2 = np.arange(len(normalEvaluationNameList))
    plt.rcParams['font.size'] = font_size
    plt.xlabel('调查景区')
    plt.ylabel('数值比率')
    yMajorLocator = MultipleLocator(0.2)  # Set the Y-axis main calibration label to a multiple of 0.2.
    yMinorLocator = MultipleLocator(0.02)  # Set the Y-axis scale label to a multiple of 0.02.
    ax = plt.subplot(212)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    plt.bar(index_p2, normalEvaluationValueList, width=barWidth, label='评价一般', fc='g')
    plt.ylim(0, 1)
    plt.bar(index_p2 + barWidth, boringEvaluationValueList, width=barWidth, label='评价极差',
            tick_label=ID_N_List, fc='r')
    plt.legend(loc='lower center', bbox_to_anchor=(0.8, 1.01), fancybox=True, ncol=5)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, hspace=0.4, wspace=0.4)
    plt.show()


# plt.xticks(rotation=90)
# plt.savefig('123.pdf')


