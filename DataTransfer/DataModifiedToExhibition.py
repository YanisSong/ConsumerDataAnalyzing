from ExhibitionPackage import ExhibitionOFLSQues as MoEx


def dataFromComputationToExhibition(statistics, result):
    Dts = statistics
    Dtr = result
    MoEx.DrawAnaGraph(Dts, Dtr)


