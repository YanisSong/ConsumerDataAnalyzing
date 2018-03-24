import re


def dickTest():
    dick = {'monkey': 1, 'banana': 1}
    if 'apple' in dick:
        dick['apple'] += 1
    else:
        dick['apple'] = 1
    print(dick)


def dataProgramming():
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    outputUrl = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, outputUrl)
        if reason:
            print(reason[0])
            if "景区" in reason[0]:
                print("HHHHH")
                if "满意" in reason[1]:
                    print(reason[1] + "LLLLLLL")
                    print()
            else:
                print("yyyyyyyyyyyyyyyyyyyyyyyyyy")
    fr.close()


# Data cleaning function.
def processingLine(value, outputUrl):
    involvingNumber = re.findall(r"\d{11}", value)
    if not involvingNumber:
        return
    valueSet = value.split(",")
    valueList = []
    markSet = [7, 8, 19, 20, 23, 24, 30]
    for i in range(0, 7):
        if len(valueSet) < 30:
            continue
        if valueSet[markSet[i] - 1] == "":
            valueSet[markSet[i] - 1] = "---"
        valueList.append(valueSet[markSet[i] - 1])
    reasonItem = ''.join(valueList)
    with open(outputUrl, "a") as destiny:
        destiny.write(reasonItem)
    return valueList


x = []


def iii(i):
    print(len(i))
    i.append("1")


iii(x)
print(len(x))