import json
import ast
import numpy as np
import pprint

fileDict = {}
lines = []

def readFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].rstrip()
    return lines

def getProfitMaxMin():
    tempDict = {}
    profit = getProfit()
    tempDict['Full Max/min Profit'] = {'Max': max(profit), 'Min': min(profit)}
    tempDict['ETH Max/min '] = {'Max': max(profit[::11]), 'Min': min(profit[::11])}
    tempDict['XRP Max/min '] = {'Max': max(profit[1::11]), 'Min': min(profit[1::11])}
    tempDict['BTC Max/min '] = {'Max': max(profit[2::11]), 'Min': min(profit[2::11])}
    tempDict['LTC Max/min '] = {'Max': max(profit[3::11]), 'Min': min(profit[3::11])}
    tempDict['ETC Max/min '] = {'Max': max(profit[4::11]), 'Min': min(profit[4::11])}
    tempDict['ZEC Max/min '] = {'Max': max(profit[5::11]), 'Min': min(profit[5::11])}
    tempDict['ZRX Max/min '] = {'Max': max(profit[6::11]), 'Min': min(profit[6::11])}
    tempDict['BCH Max/min BinSS'] = {'Max': max(profit[7::11]), 'Min': min(profit[7::11])}
    tempDict['REP Max/min BinSS'] = {'Max': max(profit[8::11]), 'Min': min(profit[8::11])}
    tempDict['BCH Max/min '] = {'Max': max(profit[9::11]), 'Min': min(profit[9::11])}
    tempDict['REP Max/min '] = {'Max': max(profit[10::11]), 'Min': min(profit[10::11])}
    return tempDict

def getProfitMeans():
    tempDict = {}
    profit = getProfit()
    tempDict['Full Mean Profit'] = np.mean(profit)
    tempDict['ETH Mean Profit'] = np.mean(profit[::11])
    tempDict['XRP Mean Profit'] = np.mean(profit[1::11])
    tempDict['BTC Mean Profit'] = np.mean(profit[2::11])
    tempDict['LTC Mean Profit'] = np.mean(profit[3::11])
    tempDict['ETC Mean Profit'] = np.mean(profit[4::11])
    tempDict['ZEC Mean Profit'] = np.mean(profit[5::11])
    tempDict['ZRX Mean Profit'] = np.mean(profit[6::11])
    tempDict['BCH Mean Profit BinSS'] = np.mean(profit[7::11])
    tempDict['REP Mean Profit BinSS'] = np.mean(profit[8::11])
    tempDict['BCH Mean Profit'] = np.mean(profit[9::11])
    tempDict['REP Mean Profit'] = np.mean(profit[10::11])
    return tempDict

def getProfitStdev():
    tempDict = {}
    profit = getProfit()
    tempDict['Full std Dev'] = np.std(np.array(profit))
    tempDict['ETH std Dev'] = np.std(np.array(profit[::11]))
    tempDict['XRP std Dev'] = np.std(np.array(profit[1::11]))
    tempDict['BTC std Dev'] = np.std(np.array(profit[2::11]))
    tempDict['LTC std Dev'] = np.std(np.array(profit[3::11]))
    tempDict['ETC std Dev'] = np.std(np.array(profit[4::11]))
    tempDict['ZEC std Dev'] = np.std(np.array(profit[5::11]))
    tempDict['ZRX std Dev'] = np.std(np.array(profit[6::11]))
    tempDict['BCH std Dev BinSS'] = np.std(np.array(profit[7::11]))
    tempDict['REP std Dev BinSS'] = np.std(np.array(profit[8::11]))
    tempDict['BCH std Dev'] = np.std(np.array(profit[9::11]))
    tempDict['REP std Dev'] = np.std(np.array(profit[10::11]))
    return tempDict

def getAskSpread():
    return getInfo('Ask_Spread')

def getProfit():
    return getInfo('Profit')

def getInfo(info):
    l = []
    for x in fileDict:
        for y in fileDict[x]:
            l.append(y[info])
    return l

def readLines():
    with open('5minTest.txt') as f:
        lines = f.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].rstrip()
    return lines

def fixReading():
    temp, counter = 0,0
    listTemp = []
    for x in range(len(lines)):
        lines[x] = ast.literal_eval(lines[x])
        listTemp.append(lines[x])
        if temp == 10:
            fileDict[counter] = listTemp
            counter = counter +1
            listTemp = []
            temp = 0
        temp = temp +1

if __name__ == '__main__':
	file = ''
	file = input("Enter File Name: ")
	lines = readFile(file)
	fixReading()
	pprint.pprint(getProfitMaxMin())
	print()
	pprint.pprint(getProfitMeans())
	print()
	pprint.pprint(getProfitStdev())