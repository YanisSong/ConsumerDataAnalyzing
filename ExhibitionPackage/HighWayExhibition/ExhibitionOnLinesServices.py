from AnalysingPackage.AnalyzingHighWayInfomation import HighWayQuestionerProcessor as AnaHWInfo
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
import pandas as pd


plt.rcParams['font.sans-serif'] = ['SimHei']


def showServicesAlyLineChart():
    dataShow, totalNum, highScoreNum = AnaHWInfo.dataAlyGroupByService()
    dataShow = dataShow.sort_index()
    yMajorLocator = MultipleLocator(20)
    yMinorLocator = MultipleLocator(2)
    services = dataShow.index.tolist()
    statistics = dataShow.values.tolist()
    ax = plt.subplot(111)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    theLabel = ["总用户数量：" + str(totalNum), "投诉用户数量：" + str(highScoreNum)]
    plt.plot(services, statistics, label=theLabel, marker='o', linestyle='solid')
    plt.xlabel(u'套餐类型')
    plt.ylabel(u'投诉数量')
    plt.title(u'投诉/套餐-趋势图')
    plt.legend()
    plt.show()


showServicesAlyLineChart()

