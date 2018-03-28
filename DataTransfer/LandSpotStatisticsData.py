from AnalysingPackage.AnalyzingLandSpotQuestioner import QuestionerOfLandSpotAnalysation as DTinterface, \
    QuestionerOfLandSpotAnalysatoinOnItems as DTFinterface


def QuestionerOFLSDT():
    waitingFileName = input("Please input candidate file's URL:")
    fileURL = waitingFileName
    quesDS = DTinterface.dataProgramming(fileURL)
    return quesDS


def QuestionerOFLSDTSave():
    waitingFileName = input("Please input candidate file's URL:")
    filename = waitingFileName
    print("This function is used to process price information."
          " Please input a suitable URL to store these data.")
    DTinterface.dataSaving(filename)


def QuestionerOFLSFDT():
    waitingFileName = input("Please input candidate file's URL:")
    filename = waitingFileName
    DSF = DTFinterface.priceProgramming(filename)
    return DSF


def QuestionerOFLSFDTSave():
    waitingFileName = input("Please input candidate file's URL:")
    filename = waitingFileName
    print("This function is used to process price information."
          " Please input a suitable URL to store these data.")
    DTFinterface.savingDataInFile(filename)


def QuestionerOFLSSDT():
    waitingFileName = input("Please input candidate file's URL:")
    filename = waitingFileName
    DSS = DTFinterface.serviceProgramming(filename)
    return DSS


def QuestionerOFLSSDTSave():
    waitingFileName = input("Please input candidate file's URL:")
    filename = waitingFileName
    print("This function is used to process price information."
          " Please input a suitable URL to store these data.")
    DTFinterface.savingDataInFile(filename)


# @Test
# print(QuestionerOFLSSDT())

