# File processing.
def dataProgramming(cf, rf):
    with open(rf, "a") as head:
        head.write("eNBId, objectId, LteScRSRP, LteNcRSRP, LteScRSRQ, LteNcRSRQ, LteScTadv, "
                   "LteScAOA, LteScSinrUL, LteScEarfcn, LteScPci, Longitude, Latitude" + "\n")
    head.close()
    fr = open(cf, encoding='gb18030', errors='ignore')
    for line in fr:
        strSet = line.split("VALUES")
        valueItem = strSet[1].lstrip(" (").replace(");", ",#@#")
        reason = processingLine(valueItem)
        with open(rf, "a") as destiny:
            destiny.write(reason + '\n')
    destiny.close()
    fr.close()


# Deal with the data in each line.
def processingLine(value):
    valueSet = value.split(",")
    valueList = []
    markSet = [31, 36, 4, 23, 5, 24, 6, 8, 9, 2, 3, 19, 20]
    for i in range(0, 13):
        if valueSet[markSet[i] - 1] == " ''":
            valueSet[markSet[i] - 1] = " '---'"
        valueList.append(valueSet[markSet[i] - 1])
    valueList.append(' --Ending;\n')
    reasonItem = ''.join(valueList)
    return reasonItem


