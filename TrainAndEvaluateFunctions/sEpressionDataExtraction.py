# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:38:05 2018

@author: patrickgavigan
"""

from sexpdata import loads, Symbol
import numpy as np

"""
"""
def getReducedFileData(fileName, includeList):
    fullData = loadSExpressions(fileName)
    reducedData = reduceSExpressions(fullData, includeList)
    goalSide = getGoalSide(fullData)
    return (reducedData, goalSide)

"""
"""
def loadSExpressions(fileName):
    # Extract the contents from the first file
    with open (fileName) as myfile:
        data = myfile.readlines()

    # Parse the data using sexptdata.
    result = list()
    for i in range(len(data)):
        currentResult = loads(data[i])
        result.append(currentResult)
    return result

"""
Determine which side the goal is
"""
def getGoalSide(data):
    for i in range(len(data)):
        (dataElement, elementName) = getElement(data, i)
        if (elementName == 'init'):
            if dataElement[1] == 'r':
                return 'l'
            else:
                return 'r'

"""
"""
def getElement(data, i):
    dataElement = data[i]
    elementName = dataElement[0]._val
    return(dataElement, elementName)

"""
Removes any top lever S-Expressions (related to actions for robocup) that are 
not in the include list.
"""
def reduceSExpressions(data, includeList):
    reducedData = list()
    for i in range(len(data)):
        currentResult = data[i]
        currentAction = currentResult[0]._val
        if currentAction in includeList:
            reducedData.append(currentResult)
    return reducedData

def getActionList(data):
    actions = list()
    for i in range(len(data)):
        currentResult = data[i]
        currentAction = currentResult[0]._val
        if (currentAction in actions) == False:
            actions.append(currentAction)
    return actions

"""
"""
def getFeatureList(data, featureCheckActionList, featureList = list()):

    # Iterate through the list looking for feature actions
    for i in range(len(data)):
        if (type(data[i][0]) is Symbol):
            if (data[i][0]._val in featureCheckActionList):
                currentFeatures = extractFeatureNames(data[i], featureCheckActionList)
                featureList.extend(currentFeatures)
    featureSet = set(featureList)
    featureList = list(featureSet)
    return featureList


"""
"""
def extractFeatureNames(data, excludeList = list()):
    featureList = list()
    for i in range(len(data)):
        if ((i == 0) or (i == 1)) == False:
            featureName = extracatSymbols(data[i][0])
            featureList.append(featureName)
    return featureList


"""
"""
def extracatSymbols(data):
    if (type(data) is list) == False:
        dataList = list()
        dataList.append(data)
    else:
        dataList = data

    symbolString = ''
    for i in range(len(dataList)):
        if containsSymbolsCheck(data):
            if type(dataList[i]) is Symbol:
                symbolString = symbolString + str(dataList[i]._val)
            elif (type(dataList[i]) is list) == False:
                symbolString = symbolString + str(dataList[i])
    
    return symbolString

"""
Check if data contains Symbols (cannot be in lower level of a list)
"""
def containsSymbolsCheck(data):
    containsSymbols = False
    dataList = list()
    dataList.extend(data)
    
    for i in range(len(data)):
        if type(data[i]) is Symbol:
            containsSymbols = True
            break
    return containsSymbols
    

"""
Check if data is a list that contains other lists
"""
def containsListCheck(data):
    containsList = False
    
    if type(data) is list:
        for i in range(len(data)):
            if type(data[i]) is list:
                containsList = True
                break
    return containsList


        

"""
"""
def getRunTable(data, actionList, featureList, goalSide):
    numElements = len(data)
    numActions = len(actionList)
    numFeatures = len(featureList)
    
    x = np.zeros((numElements, numFeatures))
    y = np.zeros((numElements, numActions))
    featureCount = 0
    actionCount = 0
    
    for i in range(numElements):
        currentResult = data[i]
        currentAction = currentResult[0]._val
        
        if currentAction in actionList:
            # Extract action data
            y[i,:] = extractAction(currentResult, actionList)
            actionCount = actionCount + 1
        else:
            # Extract feature data
            x = x
            featureCount = featureCount + 1
        
        
    return (x,y)

def extractAction(element, includeList):
    numElements = len(includeList)
    extractedData = np.zeros(numElements)
    i = includeList.index(element[0]._val)
    extractedData[i] = element[1]
    return extractedData


"""
Find a specific feature value in the element
"""
def extractIndividualFeature(element, feature):
    if element is list():
        for i in range(len(element)):
            ### Continue here tomorrow
            if element == feature:  # Not quite right
                print('meow')                