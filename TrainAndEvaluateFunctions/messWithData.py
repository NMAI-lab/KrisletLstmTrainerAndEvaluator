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

#from parsingFunctions import getFileNames

#from sEpressionDataExtraction import getReducedFileData, getActionList, getFeatureList, getRunTable, buildFeatureIncludeList, loadData

#import numpy as np

from csvLogFunctions import writeSingleResult
from configutationGenerator import buildConfigurationList

configurations = list()

testType = ["FiniteTurnKrislet"]

runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [100, 10]
useConvolutionOptions = [False]
activationOptions = ['relu']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
configurations.extend(buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions, balanceOptions))

result = ['Beans', 'Spam'];

for i in range (len(configurations)):
    writeSingleResult(testType[0], configurations[i], result[i]);


# Get the file names for available data
#testType = 'StateBasedKrislet'#'sexpt_tests'
#fileNames = getFileNames(testType)

#actionIncludeList = ['turn', 'dash', 'kick']
#featureCheckActionList = ['see']
#includeList = list()
#includeList.extend(actionIncludeList)
#includeList.extend(featureCheckActionList)

# Load S-expressions from the first file
#(data, goalSide) = getReducedFileData(fileNames[0], includeList)

# Get the possible actions
#actionList = getActionList(data)

# Get the feature list
#featureList = getFeatureList(data, featureCheckActionList, [])

# ga is short for goal adversary (where we don't want the ball to go)
# go is short for goal own (where we want the ball to go)
#featureIncludeList = ['b','ga']#['b','go','ga']

#run = getRunTable(data, actionIncludeList, featureCheckActionList, featureIncludeList, goalSide)
#(x,y) = run

#(x,y) = loadData(testType, depth = 5)
#count = np.count_nonzero(y, axis=0)



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