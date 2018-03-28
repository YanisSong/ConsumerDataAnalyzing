from AnalysingPackage.AnalyzingHighWayInfomation import HighWayQuestionerProcessor as AnaHWInfo
from matplotlib import pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']


def locationInfoPie():
    percentageList = [AnaHWInfo.locationCounting(), 1 - AnaHWInfo.locationCounting()]
    labels = [u'省内区域', u'跨省边界区']
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    explode_setting = [0.1, 0]
    plt.title(u"行驶区域调研情况", fontsize=9, bbox={'facecolor': '0.8', 'pad': 5},
              horizontalalignment='left', verticalalignment='top')
    plt.pie(x=percentageList, explode=explode_setting, labels=labels, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))
    plt.show()


locationInfoPie()

