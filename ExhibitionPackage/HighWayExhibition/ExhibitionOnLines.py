from AnalysingPackage.AnalyzingHighWayInfomation import HighWayQuestionerProcessor as AnaHWInfo
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']


def LinesInfo():
    linesInfo = AnaHWInfo.meanOFLines()  # .sort_values()
    totalIndexList = linesInfo.index.tolist()
    dataList = []
    indexList = []
    midValue = 0
    boolValue = 1
    singleIndex = ''
    for index in totalIndexList:
        if boolValue == 1:
            midValue += linesInfo[index]
            boolValue *= 2
            singleIndex += index[0]
        else:
            midValue += linesInfo[index]
            indexList.append(singleIndex)
            item = (midValue,linesInfo[index])
            dataList.append(item)
            midValue = 0
            boolValue = 1
            singleIndex = ''
    LinesSeries = pd.Series(dataList, index=indexList)
    return LinesSeries


def countingForBarShow():
    LinesSeries = LinesInfo()
    newIndexes = []
    totalIndexList = LinesSeries.index.tolist()
    for item in totalIndexList:
        itemList = item.split('（')
        newIndexes.append(itemList[0])
    totalValueList = LinesSeries.values.tolist()
    newLinesSeries = pd.Series(totalValueList, index=newIndexes)
    return newLinesSeries


def countingForPieShow(newLinesSeries):
    sortedLinesSeries = newLinesSeries.sort_values()
    largestThreeIndexes = sortedLinesSeries.tail(3).index.tolist()
    percentageList = []
    for index in largestThreeIndexes:
        valueSet = sortedLinesSeries[index]
        singlePercentage = valueSet[1] / valueSet[0]  # In province
        percentageList.append(singlePercentage)
    newPercentageSeries = pd.Series(percentageList, index=largestThreeIndexes)
    return newPercentageSeries


def graphShow():
    font_size = 9
    newLinesSeries = countingForBarShow()
    names = newLinesSeries.index.tolist()
    values = newLinesSeries.values.tolist()
    valueList = []
    for item in values:
        valueList.append(item[0])
    index_x = np.arange(len(names))
    barWidth = 0.4
    # Dividing the whole graph into two parts. This graph locates in the first line.
    plt.subplot(212)
    plt.rcParams['font.size'] = font_size
    plt.xlabel('行驶路线')
    plt.ylabel('数值比率')
    plt.title("线路评价权值情况")
    yMajorLocator = MultipleLocator(10)  # Set the Y-axis main calibration label to a multiple of 0.2.
    yMinorLocator = MultipleLocator(1)  # Set the Y-axis scale label to a multiple of 0.02.
    ax = plt.subplot(212)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    plt.bar(index_x, valueList, width=barWidth, tick_label=names, label='线路信息', fc='g')
    plt.legend(loc='lower center', bbox_to_anchor=(0.8, 1.01), fancybox=True, ncol=5)
    # Dividing the whole graph into two parts. This graph locates in the second line.
    percentageSeries = countingForPieShow(newLinesSeries)
    indexes = percentageSeries.index.tolist()
    percentages = []
    for item in indexes:
        percentages.append(percentageSeries[item])

    plt.subplot(231)
    percentageList1 = [percentages[0], 1 - percentages[0]]
    labels = [u'省内区域', u'跨省边界区']
    explode_setting = [0.1, 0]
    plt.title(indexes[0])
    plt.pie(x=percentageList1, explode=explode_setting, labels=labels, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.5, 1.3))

    plt.subplot(232)
    percentageList2 = [percentages[1], 1 - percentages[1]]
    explode_setting = [0.1, 0]
    plt.title(indexes[1])
    plt.pie(x=percentageList2, explode=explode_setting, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))

    plt.subplot(233)
    percentageList3 = [percentages[2], 1 - percentages[2]]
    explode_setting = [0.1, 0]
    plt.title(indexes[2])
    plt.pie(x=percentageList3, explode=explode_setting, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))

    plt.show()


graphShow()

