from ExhibitionPackage import ExhibitionOFMro as EbMro
from ExhibitionPackage import ExhibitionOFLSQues as EbQuLS
from ExhibitionPackage import ExhibitionOFLSFee as EbQuLSFee
from ExhibitionPackage import ExhibitionOFLSService as EbQuLSService
from ExhibitionPackage import ExhibitionOFLSSuggesstionPie as EbQuLSItemsPie


def callExhibitionMro():
    EbMro.showDataInGraph()


def callExhibitionQuestionerLS():
    EbQuLS.runnerProcess()


def callExhibitionQuestionerLSFee():
    EbQuLSFee.FeeAnaGraph()


def callExhibitionQuestionerLSService():
    EbQuLSService.ServicesAnaGraph()


def callSingleLSItemsPercentage():
    global comd
    comd = '1'
    while 'exit' not in comd:
        EbQuLSItemsPie.showSingleDataInPieChart()
        waitingCome = input("Please enter next going to search another items, and "
                            "enter exit to quit. ")
        comd = waitingCome
    print("Searching exit.")


# callSingleLSItemsPercentage()

