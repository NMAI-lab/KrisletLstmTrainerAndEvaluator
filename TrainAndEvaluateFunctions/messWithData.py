# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

#from parsingFunctions import loadData, replacePlaceholder
#from dataManagement import convertToCategorical
#from balancingFunctions import underSample, checkBalance

#from dataManagement import cropSequenceLength


from sexpdata import loads #,load, dumps

from parsingFunctions import getFileNames


testType = 'stateBasedKrislet-sexp'
fileNames = getFileNames(testType)

with open (fileNames[0]) as myfile:
    data = myfile.readlines()

result = list()
prefix = list()
for i in range(len(data)):
    currentResult = loads(data[i])
    result.append(currentResult)
    prefix.append(currentResult[0]._val)
#    print(result[i])
prefixOptions = set(prefix)

indecies = list()
for currentPrefixOption in prefixOptions:
    currentIndexGenerator = (i for i, e in enumerate(prefix) if e == currentPrefixOption)
    currentIndexList = list()
    for nextIndex in currentIndexGenerator:
        currentIndexList.append(nextIndex)
    indecies.append(currentIndexList)

#testType = "stateBasedKrislet"
#depth = 3
#data = loadData(testType, depth)

#croppedX = cropSequenceLength(data[0], 1)

#balancedData = underSample(data)

#originalBalance = checkBalance(data)
#newBalance = checkBalance(balancedData)

#finalData = replacePlaceholder(balancedData[0])

#yCategorical = convertToCategorical(data[1])