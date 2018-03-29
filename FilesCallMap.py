from AnalysingPackage.AnalyzingMroInformation import MroAnalysing as callMro
from DataTransfer import LandSpotStatisticsData as LSData
from AnalysingPackage import ConsumerSuggestionResearch as AlyCS
from AnalysingPackage.AnalyzingHighWayInfomation import HighWayQuestionerProcessor as HWPro


def callMroAlys():
    waitingFileName = input("Please input candidate file's URL:")
    fileURL = waitingFileName
    destinyPath = input("Please input output TXT file's URL:")
    if ".txt" not in destinyPath:
        destinyPath += "_.txt"
    resultURL = destinyPath
    callMro.dataProgramming(fileURL, resultURL)


def callLandSpotAlys():
    LSData.QuestionerOFLSDT()
    LSData.QuestionerOFLSDTSave()


def consumerSuggesstionSave():
    AlyCS.suggestionClean()


def callLandSpotAlysOnFee():
    LSData.QuestionerOFLSFDT()
    LSData.QuestionerOFLSFDTSave()


def callLandSpotAlysOnServices():
    LSData.QuestionerOFLSSDT()
    LSData.QuestionerOFLSSDTSave()


def callHighWayDataAly():
    HWPro.cleanedData
    savingPath = input("Please input output file's URL:")
    if '.xls' not in savingPath and '.xlsx' not in savingPath:
        savingPath += '_.xls'
    HWPro.dataSaving(savingPath)


# def callQuesAly():
def userRequest():
    # TODO: LIKE FOLLOWS.
    print("Get user request here. ")


callHighWayDataAly()
