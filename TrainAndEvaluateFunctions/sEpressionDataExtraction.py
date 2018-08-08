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
def getFeatureList(data, excludeList = list(), featureList = list()):

    # Check if data is a list, iterate through the list
    if type(data) is list:
        for i in range(len(data)):
            featureList = getFeatureList(data[i], excludeList, featureList)
    
    # Check if data is a Symbol, if not in the feature list add it
    elif type(data) is Symbol:
        feature = data._val
        if ((feature in featureList) or (feature in excludeList)) == False:
            featureList.append(feature)
        
    return featureList

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
    