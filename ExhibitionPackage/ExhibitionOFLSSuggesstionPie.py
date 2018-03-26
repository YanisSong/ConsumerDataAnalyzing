from AnalysingPackage import ConsumerSuggestionResearch as ExCS
import matplotlib.pyplot as plt


def showSingleDataInPieChart():
    count = 1
    ExCS.suggesstionInfoFilter()
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
    total = phoneNumber[ID-1] + messageNumber[ID-1] + netNumber[ID-1]
    labels = ['phone', 'message', 'network']
    percentages = [phoneNumber[ID-1]/total, messageNumber[ID-1]/total, netNumber[ID-1]/total]
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    plt.pie(x=percentages, labels=labels, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.show()


# showSingleDataInPieChart()

