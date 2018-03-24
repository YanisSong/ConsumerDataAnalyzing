# This module is used to analysing the questioner that is collected from the land spots.
import re


# data input and output interface.
# Todo: Modifying the function use the input file URLs.
def priceProgramming():
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    outputUrl = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    countingDict = {}
    distributeConsumerDict = {}
    # Todo: Add userDict in the future, which is used to analysing user information.
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, outputUrl)
        if reason:
            analysingPrice(reason, countingDict, distributeConsumerDict)
    fr.close()
    priceStatistics = priceProcess(countingDict, distributeConsumerDict)
    return priceStatistics


def serviceProgramming():
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    outputUrl = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    countingDict = {}
    distributeConsumerDict = {}
    # Todo: Add userDict in the future, which is used to analysing user information.
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, outputUrl)
        if reason:
            analysingServices(reason, countingDict, distributeConsumerDict)
    fr.close()
    servicesStatistics = serviceProcess(countingDict, distributeConsumerDict)
    return servicesStatistics


# Data cleaning function.
def processingLine(value, outputUrl):
    involvingNumber = re.findall(r"\d{11}", value)
    if not involvingNumber:
        return
    valueSet = value.split(",")
    valueList = []
    markSet = [8, 28, 29]
    for i in range(0, 3):
        if len(valueSet) < 29:
            return
        if valueSet[markSet[i] - 1] == "":
            return
        valueList.append(valueSet[markSet[i] - 1])
    reasonItem = ''.join(valueList)
    with open(outputUrl, "a") as destiny:
        destiny.write(reasonItem)
    return valueList


# Analysing function is used to collect different kinds of prices.
def analysingPrice(reason, countingDict, distributeConsumerDict):
    if ("满意" in reason[0]) or ("惊喜" in reason[0]):
        if reason[2] in distributeConsumerDict:
            distributeConsumerDict[reason[2]] += 1
        else:
            distributeConsumerDict[reason[2]] = 1
    else:
        if reason[1] in distributeConsumerDict:
            distributeConsumerDict[reason[1]] += 1
        else:
            distributeConsumerDict[reason[1]] = 1
        if reason[2] in countingDict:
            countingDict[reason[2]] += 1
        else:
            countingDict[reason[2]] = 1


# Analysing function is used to collect different kinds of networks.
def analysingServices(reason, countingDict, distributeConsumerDict):
    if ("满意" in reason[0]) or ("惊喜" in reason[0]):
        if reason[1] in distributeConsumerDict:
            distributeConsumerDict[reason[1]] += 1
        else:
            distributeConsumerDict[reason[1]] = 1
    else:
        if reason[1] in distributeConsumerDict:
            distributeConsumerDict[reason[1]] += 1
        else:
            distributeConsumerDict[reason[1]] = 1
        if reason[1] in countingDict:
            countingDict[reason[1]] += 1
        else:
            countingDict[reason[1]] = 1


# This function is used to deal with the statistics exhibition.
def priceProcess(countingDict, distributeConsumerDict):
    statistics = {}
    for (key, value) in distributeConsumerDict.items():
        if not('元' in key):
            continue
        else:
            if key in countingDict:
                oneSpotStatistics = countingDict[key]/value
            else:
                oneSpotStatistics = 1.0
            statistics[key] = oneSpotStatistics
    sortResult = {}
    for key, value in statistics.items():
        if re.findall(r"\d{2,3}", key) and "以上" in key:
            price = re.findall(r"\d{2,3}", key)
            sortResult[int(price[0])] = value
        else:
            if re.findall(r"\d{2,3}", key) and "以下" in key:
                price = re.findall(r"\d{2,3}", key)
                sortResult[int(price[0])] = value
            else:
                keyPrice = re.findall(r"\d{2,3}", key)
                sortResult[int(keyPrice[0])] = value
    sortedResult = sorted(sortResult.items(), key=lambda d: d[0])
    return sortedResult


# This function is used to deal with the statistics exhibition.
def serviceProcess(countingDict, distributeConsumerDict):
    statistics = {}
    for (key, value) in distributeConsumerDict.items():
        if not ("M" in key) and not ("G" in key):
            continue
        else:
            if key in countingDict:
                oneSpotStatistics = countingDict[key]/value
            else:
                oneSpotStatistics = 1.0
        statistics[key] = oneSpotStatistics
    sortResult = {}
    for key, value in statistics.items():
        if re.findall(r"\d{1,3}", key) and "M" in key and "以上" in key:
            name = re.findall(r"\d{1,3}", key)
            sortResult[name[0] + "A" + "Z"] = value
        else:
            if re.findall(r"\d{1,3}", key) and "M" in key and "以内" in key:
                name = re.findall(r"\d{1,3}", key)
                sortResult[name[0] + "A" + "A"] = value
            else:
                if re.findall(r"\d{1,3}", key) and "G" in key and "以内" in key:
                    name = re.findall(r"\d{1,3}", key)
                    sortResult[name[0] + "Z" + "A"] = value
                else:
                    name = re.findall(r"\d{1,3}", key)
                    sortResult[name[0] + "Z" + "Z"] = value
    sortedResult = sorted(sortResult.items(), key=lambda d: d[0])
    return sortedResult


# @Test
# data = priceProgramming()
# print(data)

