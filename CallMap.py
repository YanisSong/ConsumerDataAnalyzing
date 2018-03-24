from AnalysingPackage import MroAnalysing as callMro, QuestionerOfLandSpotAnalysation as callLandSpot


def callMroAlys():
    waitingFileName = input("Please input candidate file's URL:")
    fileURL = waitingFileName
    destinyPath = input("Please input output file's URL:")
    resultURL = destinyPath
    callMro.dataProgramming(fileURL, resultURL)


def callSpotAlys():
    callLandSpot.analysingProcess()

# def callQuesAly():