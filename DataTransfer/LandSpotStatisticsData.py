from AnalysingPackage import QuestionerOfLandSpotAnalysation as DTinterface
from AnalysingPackage import QuestionerOfLandSpotAnalysatoinOnItems as DTFinterface


def QuestionerOFLSDT():
    quesDS = DTinterface.dataProgramming()
    return quesDS


def QuestionerOFLSFDT():
    DSF = DTFinterface.priceProgramming()
    return DSF


def QuestionerOFLSSDT():
    DSS = DTFinterface.serviceProgramming()
    return DSS


# @Test
# print(QuestionerOFLSFDT())

