# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

#from parsingFunctions import loadData, replacePlaceholder
#from dataManagement import convertToCategorical
#from balancingFunctions import underSample, checkBalance

#from dataManagement import cropSequenceLength


#from sexpdata import loads #,load, dumps

from parsingFunctions import getFileNames

from sEpressionDataExtraction import getReducedFileData, getActionList, getFeatureList, getRunTable

# Get the file names for available data
testType = 'sexpt_tests'
fileNames = getFileNames(testType)

actionIncludeList = ['turn', 'dash', 'kick']
featureCheckActionList = ['see']
includeList = list()
includeList.extend(actionIncludeList)
includeList.extend(featureCheckActionList)

# Load S-expressions from the first file
(data, goalSide) = getReducedFileData(fileNames[0], includeList)

# Get the possible actions
actionList = getActionList(data)

# Get the feature list
featureList = getFeatureList(data, actionList, [])

run = getRunTable(data, actionIncludeList, featureList, goalSide)

#run = list()
#
#for i in range(len(result)):
#    currentPrefix = prefix[i]
#    currentResult = result[i]
#    runStep = {}
#    runStep['prefix'] = currentPrefix
#    runStep['reply'] = currentResult
#    run.append(runStep)


# Get index list for each prefix
#indecies = list()
#for currentPrefixOption in prefixOptions:
#    currentIndexGenerator = (i for i, e in enumerate(prefix) if e == currentPrefixOption)
#    currentIndexList = list()
#    for nextIndex in currentIndexGenerator:
#        currentIndexList.append(nextIndex)
#    indecies.append(currentIndexList)

#testType = "stateBasedKrislet"
#depth = 3
#data = loadData(testType, depth)

#croppedX = cropSequenceLength(data[0], 1)

#balancedData = underSample(data)

#originalBalance = checkBalance(data)
#newBalance = checkBalance(balancedData)

#finalData = replacePlaceholder(balancedData[0])

#yCategorical = convertToCategorical(data[1])