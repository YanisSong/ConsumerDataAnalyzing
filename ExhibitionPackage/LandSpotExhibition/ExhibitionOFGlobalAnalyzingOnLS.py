import matplotlib.pyplot as plt


def phoneDataAnalysationExhibit(fileURL, index, keyword1, keyword2, keyword3, nameIndex, defaultSpotName=''):
    valueList = []
    fr = open(fileURL, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLineWithSpotName(line, index, nameIndex)
        if reason:
            valueList.append(reason)
    fr.close()
    processingList = []
    frequentBoring = 0
    sometimeBoring = 0
    pretty = 0
    total_all = len(valueList)
    if total_all == 0:
        print("We get a wrong data in processing: total number is None!")
        return
    if defaultSpotName != '':
        for item in valueList:
            if defaultSpotName in item[0]:
                processingList.append(item)
    else:
        processingList = valueList
    total = len(processingList)
    for item in processingList:
        if keyword1 in item[1]:
            pretty += 1
        else:
            if keyword2 in item[1]:
                sometimeBoring += 1
            else:
                if keyword3 in item[1]:
                    frequentBoring += 1
    percentages = [frequentBoring / total, sometimeBoring / total, pretty / total,
                   1 - frequentBoring / total - sometimeBoring / total - pretty / total]
    return percentages


def processingLineWithSpotName(value, index, nameIndex):
    valueSet = value.split(",")
    valueList = []
    markSet = index - 1
    if len(valueSet) >= markSet:
        valueList.append(valueSet[nameIndex-1])
        valueList.append(valueSet[markSet])
    if len(valueList) >= 1:
        return valueList
    else:
        return None


# def processingLine(value, index):
#     valueSet = value.split(",")
#     valueList = []
#     markSet = index - 1
#     if len(valueSet) >= index:
#         valueList.append(valueSet[markSet])
#     if len(valueList) >= 1:
#         return valueList
#     else:
#         return None


def showPieChart(percentageList, keyword1, keyword2, keyword3):
    labels = [keyword1, keyword2, keyword3, '其他']
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    explode_setting = [0.1, 0.1, 0.1, 0.1]
    plt.title("总体调研情况", fontsize=9, bbox={'facecolor': '0.8', 'pad': 5},
              horizontalalignment='left', verticalalignment='top')
    plt.pie(x=percentageList, explode=explode_setting, labels=labels, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))
    plt.tight_layout()
    plt.show()


def showPieChartOfDistinctSpot(percentageList, landSpot, keyword1, keyword2, keyword3):
    labels = [keyword1, keyword2, keyword3, '其他']
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    explode_setting = [0.1, 0.1, 0.1, 0.1]
    plt.title(landSpot + "调研情况", fontsize=9, bbox={'facecolor': '0.8', 'pad': 5},
              horizontalalignment='left', verticalalignment='top')
    plt.pie(x=percentageList, explode=explode_setting, labels=labels, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))
    plt.show()

