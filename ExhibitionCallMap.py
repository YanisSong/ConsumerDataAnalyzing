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
    waitingIndexNo_ = input("Please input which index you want to research:")
    keyword1 = input("Please input the first keyword in this column:")
    keyword2 = input("Please input the second keyword in this column:")
    keyword3 = input("Please input the third keyword in this column:")
    index = int(waitingIndexNo_)
    percentage = EbQuLSPhoUserPie.phoneDataAnalysationExhibit(fileURL, index, keyword1, keyword2, keyword3)
    EbQuLSPhoUserPie.showPieChart(percentage, keyword1, keyword2, keyword3)


def callSingleLSItemsPercentage():
    comd = '1'
    while 'exit' not in comd:
        EbQuLSItemsPie.showSingleDataInPieChart()
        waitingCome = input("Please enter next going to search another items, and "
                            "enter exit to quit. ")
        comd = waitingCome
    print("Searching exit.")


# callSingleLSItemsPercentage()
totalPhoneUserSuggesstionExhibition()

