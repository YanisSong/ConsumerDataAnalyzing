# This module is used to analysing the questioner that is collected from the land spots.
import re


# data input and output interface.
def dataProgramming(fileURL):
    countingDict = {}
    unSatisfiedItems = {}
    suggesstionDick = {}
    distributeConsumerDict = {}
    totalCustomer = []
    uselessConsumer = []
    # Todo: Add userDict in the future, which is used to analysing user information.
    fr = open(fileURL, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line)
        if reason:
            analysingProcess(reason, countingDict, suggesstionDick, totalCustomer, uselessConsumer,
                             distributeConsumerDict, unSatisfiedItems)
    fr.close()
    global questionerStatistics
    questionerStatistics = statisticsProcess(totalCustomer, uselessConsumer, countingDict, distributeConsumerDict)
    global questionerResultResearch
    questionerResultResearch = unSatisfiedItemsResearch(countingDict, unSatisfiedItems)
    # Todo: Check this module when the function completed.
    global meaningfulCollection
    meaningfulCollection = countingDict.copy()
    return suggesstionDick


def dataSaving(fileURL):
    destinyPath = input("Please input output file's URL:")
    outputURL = destinyPath
    fr = open(fileURL, encoding='gb18030', errors='ignore')
    for line in fr:
        valueList = processingLine(line)
        if valueList:
            valueItems = ''.join(valueList)
        else:
            continue
        with open(outputURL, "a") as destiny:
            destiny.write(valueItems)
    fr.close()


# Data cleaning function.
def processingLine(value):
    involvingNumber = re.findall(r"\d{11}", value)
    if not involvingNumber:
        return
    valueSet = value.split(",")
    valueList = []
    markSet = [7, 8, 19, 20, 23, 24, 30]
    for i in range(0, 7):
        if len(valueSet) < 30:
            continue
        if valueSet[markSet[i] - 1] == "":
            valueSet[markSet[i] - 1] = "---"
        valueList.append(valueSet[markSet[i] - 1])
    return valueList


# Analysing function is used to collect different kinds of consumers' number and suggestions and store them in a
# suitable data structure.
def analysingProcess(reason, countingDict, suggesstionDick, totalCustomer, uselessConsumer,
                     distributeConsumerDict, unSatisfiedItems):
    if ("---" in reason[0]) or ("上述一个都没去过" in reason[0]):
        uselessConsumer.append("1")
        totalCustomer.append("1")
    else:
        totalCustomer.append("1")
        if ("满意" in reason[1]) or ("惊喜" in reason[1]):
            if reason[0] in distributeConsumerDict:
                distributeConsumerDict[reason[0]] += 1
            else:
                distributeConsumerDict[reason[0]] = 1
        else:
            if reason[0] in distributeConsumerDict:
                distributeConsumerDict[reason[0]] += 1
            else:
                distributeConsumerDict[reason[0]] = 1
            if reason[0] in countingDict:
                countingDict[reason[0]] += 1
            else:
                countingDict[reason[0]] = 1
            if "一般" in reason[1]:
                if reason[0] in unSatisfiedItems:
                    unSatisfiedItems[reason[0]] += 1
                else:
                    unSatisfiedItems[reason[0]] = 1
        suggesstion = "满意度调查:&&" + "**调研景区:" + reason[0] + "**通话:" + reason[2] + "**即时信息:" + reason[3] +\
                      "**网络速度:" + reason[4] + "**个人意见:" + reason[5]
        if reason[6] in suggesstionDick and reason[0] in countingDict:
            # There are more than one report under the same person in one spot.
            uselessConsumer.append("1")
        else:
            suggesstionDick[reason[6]] = suggesstion


# Computing the different classes of the dissatisfied consumers.
def unSatisfiedItemsResearch(countingDict, unSatisfiedItems):
    result = {}
    for key, value in countingDict.items():
        if key in unSatisfiedItems:
            unsatisfiedItem = unSatisfiedItems[key]
            result[key] = unsatisfiedItem / value
        else:
            result[key] = 0
    return result


# This function is used to deal with the comparison between satisfied and dissatisfied.
def statisticsProcess(total, useless, countingDict, distributeConsumerDict):
    statistics = {}
    if total != 0:
        uselessStatistics = len(useless)/len(total)
    else:
        uselessStatistics = 0
    statistics['无效数据比率：'] = uselessStatistics
    for (key, value) in distributeConsumerDict.items():
        if key in countingDict:
            oneSpotStatistics = countingDict[key]/value
        else:
            oneSpotStatistics = 1.0
        statistics[key] = oneSpotStatistics
    return statistics


# global suggesstionDict
# suggesstionDict = dataProgramming()


# @Test
# data = dataProgramming()
# print(data)

