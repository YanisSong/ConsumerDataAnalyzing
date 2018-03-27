import re
from ExhibitionPackage import ExhibitionOFMro as EbMro
from ExhibitionPackage import ExhibitionOFLSQues as EbQuLS
from ExhibitionPackage import ExhibitionOFLSFee as EbQuLSFee
from ExhibitionPackage import ExhibitionOFLSService as EbQuLSService
from ExhibitionPackage import ExhibitionOFLSSuggesstionPie as EbQuLSItemsPie
from ExhibitionPackage import ExhibitionOfGlobalAnalyzationOnLS as EbQuLSPhoUserPie


def callExhibitionMro():
    EbMro.showDataInGraph()


def callExhibitionQuestionerLS():
    EbQuLS.runnerProcess()


def callExhibitionQuestionerLSFee():
    EbQuLSFee.FeeAnaGraph()


def callExhibitionQuestionerLSService():
    EbQuLSService.ServicesAnaGraph()


def totalPhoneUserSuggesstionExhibition():
    waitingFileName = input("Please input candidate file's URL:(involve the extend file style name!)")
    fileURL = waitingFileName
    waitingIndexNo_ = input("Please input which index you want to research:(Indexes' number start from one.)")
    index = int(waitingIndexNo_)
    keyword1 = input("Please input the first keyword in this column:")
    keyword2 = input("Please input the second keyword in this column:")
    keyword3 = input("Please input the third keyword in this column:")
    spotNameIndexNo_ = input("The default spot names' index is 7, input a new one if necessary:")
    if re.match(r"\d+", spotNameIndexNo_):
        nameIndex = int(spotNameIndexNo_)
    else:
        nameIndex = 7
    specialName = input("If you want to check a special spot, please in put the spot's name,"
                        " or press enter to continue:")
    if specialName == '':
        percentage = EbQuLSPhoUserPie.phoneDataAnalysationExhibit(fileURL, index, keyword1, keyword2, keyword3,
                                                                  nameIndex)
        EbQuLSPhoUserPie.showPieChart(percentage, keyword1, keyword2, keyword3)
    else:
        percentage = EbQuLSPhoUserPie.phoneDataAnalysationExhibit(fileURL, index, keyword1, keyword2, keyword3,
                                                                  nameIndex, specialName)
        EbQuLSPhoUserPie.showPieChartOfDistinctSpot(percentage, specialName, keyword1, keyword2, keyword3)


def callSingleLSItemsPercentage():
    command = '1'
    while 'exit' not in command:
        EbQuLSItemsPie.showSingleDataInPieChart()
        waitingCome = input("Please enter next going to search another items, and "
                            "enter exit to quit. ")
        command = waitingCome
    print("Searching exit.")


# callSingleLSItemsPercentage()
totalPhoneUserSuggesstionExhibition()

