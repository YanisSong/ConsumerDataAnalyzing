from DataTransfer import LandSpotStatisticsData as LSStatistics
from xlwt import *


global phoneCallData
phoneCallData = {}
global messageData
messageData = {}
global netWorkData
netWorkData = {}


def suggestionClean():
    suggesstionDict = LSStatistics.QuestionerOFLSDT()
    phoneCallData.clear()
    messageData.clear()
    netWorkData.clear()
    for key, item in suggesstionDict.items():
        # Todo: Phone number is the key that may be used in the future function
        dataList = item.split("**")
        processingPhoneCall(dataList, phoneCallData)
        processingMessage(dataList, messageData)
        processingNetWork(dataList, netWorkData)
    outputDataInExcel(phoneCallData, messageData, netWorkData)


def suggesstionInfoFilter():
    suggesstionDict = LSStatistics.QuestionerOFLSDT()
    phoneCallData.clear()
    messageData.clear()
    netWorkData.clear()
    for key, item in suggesstionDict.items():
        dataList = item.split("**")
        processingPhoneCall(dataList, phoneCallData)
        processingMessage(dataList, messageData)
        processingNetWork(dataList, netWorkData)


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
    waitingFileName = input("Please input a suitable output Office_excel file's URL:")
    fileURL = waitingFileName
    if fileURL.endswith(".xlsx"):
        fileURL.replace(".xlsx", ".xls")
    if ".xls" not in fileURL:
        fileURL += "_.xls"
    workSheet.save(fileURL)


def processingPhoneCall(dataList, phoneCallDict):
    spotName = dataList[1].split(u':')
    phoneItem = dataList[2].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in phoneItem[1]):
            if spotName[1] in phoneCallDict:
                phoneCallDict[spotName[1]] += 1
            else:
                phoneCallDict[spotName[1]] = 1


def processingMessage(dataList, messageDict):
    spotName = dataList[1].split(u':')
    messageItem = dataList[3].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in messageItem[1]):
            if spotName[1] in messageDict:
                messageDict[spotName[1]] += 1
            else:
                messageDict[spotName[1]] = 1


def processingNetWork(dataList, netWorkDict):
    spotName = dataList[1].split(u':')
    netWorkItem = dataList[4].split(u':')
    if len(spotName) < 2:
        return
    if "---" in spotName[1]:
        return
    else:
        if not ("---" in netWorkItem[1]):
            if spotName[1] in netWorkDict:
                netWorkDict[spotName[1]] += 1
            else:
                netWorkDict[spotName[1]] = 1


