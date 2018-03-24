import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from DataTransfer import LandSpotStatisticsData as exhibitionCall


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


font = {'color': 'g',
        'weight': 'normal',
        'size': 16
        }


def ServicesAnaGraph():
    yMajorLocator = MultipleLocator(0.1)
    yMinorLocator = MultipleLocator(0.01)
    dataDict = exhibitionCall.QuestionerOFLSSDT()
    services = []
    statistics = []
    for item in dataDict:
        services.append(item[0])
    for item in dataDict:
        statistics.append(item[1])
    plt.ylim(0, 0.5)
    ax = plt.subplot(111)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    plt.plot(services, statistics, marker='o', linestyle='solid')
    plt.xlabel(u'网络类型', fontdict=font)
    plt.ylabel(u'比率', fontdict=font)
    plt.title(u'比率趋势图', fontdict=font)
    plt.legend()
    plt.show()


ServicesAnaGraph()

