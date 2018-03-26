from AnalysingPackage import MroAnalysing as callMro
from DataTransfer import LandSpotStatisticsData as LSData
from AnalysingPackage import ConsumerSuggestionResearch as AlyCS


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


# def callQuesAly():
def userRequest():
    # TODO: LIKE FOLLOWS.
    print("Get user request here. ")


