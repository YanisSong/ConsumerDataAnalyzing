from AnalysingPackage import ConsumerSuggestionResearch as ExCS
import matplotlib.pyplot as plt


def showSingleDataInPieChart():
    count = 1
    print("Please input which land spot you want to search:")
    print("Name list like follows")
    for item in ExCS.phoneCallData.keys():
        print(str(count) + "--" + item)
        count += 1
    waitingItemNumber = input("Please input search item id:")
    drawPieChart(waitingItemNumber)


def drawPieChart(Number):
    ID = int(Number)
    phoneNumber = list(ExCS.phoneCallData.values())
    messageNumber = list(ExCS.messageData.values())
    netNumber = list(ExCS.netWorkData.values())
    total = phoneNumber[ID] + messageNumber[ID] + netNumber[ID]
    labels = ['phone', 'message', 'network']
    percentages = [phoneNumber[ID]/total, messageNumber[ID]/total, netNumber[ID]/total]
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    plt.pie(x=percentages, labels=labels, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.show()


showSingleDataInPieChart()

