import matplotlib.pyplot as plt


def phoneDataAnalysationExhibit(fileURL, index, keyword1, keyword2, keyword3):
    valueList = []
    fr = open(fileURL, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, index)
        if reason:
            valueList.append(reason)
    fr.close()
    frequentBoring = 0
    sometimeBoring = 0
    pretty = 0
    total = len(valueList)
    if total == 0:
        print("We get a wrong data in processing: total number is None!")
        return
    for item in valueList:
        if keyword1 in item:
            pretty += 1
        else:
            if keyword2 in item:
                sometimeBoring += 1
            else:
                if keyword3 in item:
                    frequentBoring += 1
    percentages = [frequentBoring / total, sometimeBoring / total, pretty / total,
                   1 - frequentBoring / total - sometimeBoring / total - pretty / total]
    return percentages


def processingLine(value, index):
    valueSet = value.split(",")
    valueList = ''
    markSet = index - 1
    if len(valueSet) >= index:
        valueList += valueSet[markSet]
    if valueList != '':
        return valueList
    else:
        return None


def showPieChart(percentageList, keyword1, keyword2, keyword3):
    labels = [keyword1, keyword2, keyword3, '其他']
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    explode_setting = [0.2, 0.1, 0.1, 0.1]
    plt.pie(x=percentageList, explode=explode_setting, labels=labels, autopct='%3.1f %%',
            labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=True)
    plt.show()


