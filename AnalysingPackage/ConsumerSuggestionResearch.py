from AnalysingPackage import QuestionerOfLandSpotAnalysation as QACall
from xlwt import *


def suggestionClean():
    # suggesstionDict = QACall.suggesstionDict
    suggesstionDict = QACall.dataProgramming()
    global phoneCallData
    phoneCallData = {}
    global messageData
    messageData = {}
    global netWorkData
    netWorkData = {}
    for key, item in suggesstionDict.items():
        # Todo: Phone number is the key that may be used in the future function
        dataList = item.split("**")
        processingPhoneCall(dataList, phoneCallData)
        processingMessage(dataList, messageData)
        processingNetWork(dataList, netWorkData)
    outputDataInExcel(phoneCallData, messageData, netWorkData)


def outputDataInExcel(phoneCallItems, messageItems, netWorkItems):
    workSheet = Workbook(encoding='utf-8')
    table = workSheet.add_sheet('景区数据统计')
    allData = [["景区名称", "通话质量", "即时通讯质量", "网络质量"]]
    sortedPhoneCallItems = sorted(phoneCallItems.items(), key=lambda d: d[0])
    sortedMessageItems = sorted(messageItems.items(), key=lambda d: d[0])
    sortedNetWorkItems = sorted(netWorkItems.items(), key=lambda d: d[0])
    length = len(sortedPhoneCallItems)
    nameList = []
    phoneCallItems = []
    messageItems = []
    netWorkItems = []
    for item in sortedPhoneCallItems:
        nameList.append(item[0])
        phoneCallItems.append(item[1])
    for item in sortedMessageItems:
        messageItems.append(item[1])
    for item in sortedNetWorkItems:
        netWorkItems.append(item[1])
    for i in range(length):
        items = [nameList[i], phoneCallItems[i], messageItems[i], netWorkItems[i]]
        allData.append(items)
    for x_track, value in enumerate(allData):
        for y_track, data in enumerate(value):
            table.write(x_track, y_track, data)
    workSheet.save('景区调研.xls')


def processingPhoneCall(dataList, phoneCallData):
    spotName = dataList[1].split(u':')
    phoneItem = dataList[2].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in phoneItem[1]):
            if spotName[1] in phoneCallData:
                phoneCallData[spotName[1]] += 1
            else:
                phoneCallData[spotName[1]] = 1


def processingMessage(dataList, messageData):
    spotName = dataList[1].split(u':')
    messageItem = dataList[3].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in messageItem[1]):
            if spotName[1] in messageData:
                messageData[spotName[1]] += 1
            else:
                messageData[spotName[1]] = 1


def processingNetWork(dataList, netWorkData):
    spotName = dataList[1].split(u':')
    netWorkItem = dataList[4].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in netWorkItem[1]):
            if spotName[1] in netWorkData:
                netWorkData[spotName[1]] += 1
            else:
                netWorkData[spotName[1]] = 1


suggestionClean()

