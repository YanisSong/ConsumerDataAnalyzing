# _*_ coding:utf-8 _*_
import pandas as pd


locationInfo = []


def dataCleaning():
    names = []
    locationInCount = 0
    locationOutCount = 0
    for i in range(1, 39):
        names.append('item' + str(i))
    # file = open(r'D:\workDir\客服部调查问卷分析报告\云南高铁网络质量调查情况-有效样本清单.xlsx', 'rb')
    dataF = pd.read_excel(r'D:\workDir\客服部调查问卷分析报告\云南高铁.xlsx', 'Sheet1', skiprows=[0], names=names)
    dataF = dataF.dropna(subset=['item7'])
    dataFFilter = dataF[(True ^ dataF['item7'].isin(['其他，请您补充']))]
    # Delete the useless columns from the DataFrame.
    dataFSelected = dataFFilter.drop(['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item8', 'item10', 'item15',
                                      'item17', 'item18', 'item19', 'item20', 'item21', 'item22', 'item23', 'item24',
                                      'item25', 'item26', 'item27', 'item30', 'item31', 'item33', 'item37', 'item38'],
                                     axis=1)
    dataFSelected = dataFSelected.dropna(subset=['item12'])  # type: pd.DataFrame
    # Modifying the columns' name.
    dataFSelected.columns = ['线路', '频次', '评分权重', '意见反馈', '附加信息', '概率权重', '跨省(Y/N)', '通讯情况',
                             '娱乐情况', '年龄段', '网络类型', '套餐类型', '号码']
    indexList = dataFSelected[(dataFSelected['意见反馈'] == '其他，请您补充')].index.tolist()
    for i in indexList:
        dataFSelected['意见反馈'][i] = dataFSelected['附加信息'][i]
    dataFSelected.pop('附加信息')
    # Modifying the frequency data to integer and using to compute the weight.
    dataFSelected = dataFSelected.dropna(subset=['意见反馈'])
    dataFSelected = dataFSelected.fillna(1)
    dataFSelected = dataFSelected.replace(u'每年1~2次', 2)
    dataFSelected = dataFSelected.replace(u'每年3~6次', 4)
    dataFSelected = dataFSelected.replace(u'每年6~12次', 8)
    dataFSelected = dataFSelected.replace(u'几乎每月都要乘坐1次及以上', 16)
    dataFSelected = dataFSelected.replace(u'没有', 1)
    dataFSelected = dataFSelected.replace(u'没有留意', 1)
    dataFSelected = dataFSelected.replace(u'很少', 2)
    dataFSelected = dataFSelected.replace(u'有时', 4)
    dataFSelected = dataFSelected.replace(u'经常', 8)
    dataFSelected = dataFSelected.replace(u'跨省交界', 1 / 3)
    # Computing the weight of each item.
    totalIndexList = dataFSelected.index.tolist()
    for i in totalIndexList:
        if dataFSelected.ix[i, '评分权重'] == 4:
            dataFSelected.ix[i, '评分权重'] = 1
        else:
            if dataFSelected.ix[i, '评分权重'] == 3:
                dataFSelected.ix[i, '评分权重'] = 2
            else:
                if dataFSelected.ix[i, '评分权重'] == 2:
                    dataFSelected.ix[i, '评分权重'] = 4
                else:
                    if dataFSelected.ix[i, '评分权重'] == 1:
                        dataFSelected.ix[i, '评分权重'] = 8
        weight = dataFSelected.ix[i, '频次'] * dataFSelected.ix[i, '评分权重'] * \
            dataFSelected.ix[i, '概率权重'] * dataFSelected.ix[i, '跨省(Y/N)']
        if weight.is_integer():
            locationInCount += 1
        else:
            locationOutCount += 1
        dataFSelected.ix[i, '评分权重'] = round(weight, 2)
    locationInfo.append(locationInCount)
    locationInfo.append(locationOutCount)
    dataFSelected.pop('频次')
    dataFSelected.pop('概率权重')
    return dataFSelected


cleanedData = dataCleaning()


def dataSaving():
    cleanedData.to_excel(r'D:\workDir\客服部调查问卷分析报告\云南高铁_Clean.xls', sheet_name='cleanData')


def locationCounting():
    withinProvince = int(locationInfo[0])
    outOfProvince = int(locationInfo[1])
    percentage = withinProvince / (withinProvince + outOfProvince)
    return percentage


def meanOFLines():
    # grouped = cleanedData['评分权重'].groupby(cleanedData['线路'])
    groupMean = cleanedData['评分权重'].groupby([cleanedData['线路'], cleanedData['跨省(Y/N)']]).mean()
    return groupMean

