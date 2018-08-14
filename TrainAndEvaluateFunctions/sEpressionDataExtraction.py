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
#def containsListCheck(data):
#    containsList = False
#    
#    if type(data) is list:
#        for i in range(len(data)):
#            if type(data[i]) is list:
#                containsList = True
#                break
#    return containsList


        

"""
"""
def getRunTable(data, actionList, featureActionList, featureList, goalSide):
    
    # Get the internal names for the feature list
    featureNameList = buildFeatureIncludeList(featureList, goalSide)
    
    # Determine number of elements, actions and features
    numElements = len(data)
    numActions = len(actionList)
    numFeatures = len(featureNameList)
    
    # Build a placeholder for the run table. The headdings of each column
    # correspond to the items in feature List (x) and action list (y)
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
        elif currentAction in featureActionList:
            # Extract feature data
            x[i,:] = extractFeature(currentResult, featureList, featureActionList)
            featureCount = featureCount + 1
        
        # Reduce rows
        
    return (x,y)

"""
Extract an individual action and parameters for the run table
"""
def extractAction(element, includeList):
    numElements = len(includeList)
    extractedData = np.zeros(numElements)
    i = includeList.index(element[0]._val)
    extractedData[i] = element[1]
    return extractedData

"""
Extract an individual feature and parameters for the run table
"""
def extractFeature(element, includeList, featureActionList):
    numElements = 2 * len(includeList)      # Features have 2 parameters
    extractedData = np.zeros(numElements)
    
    for i in range(len(element)):  
        if (type(element[i]) is list) == False:
            currentElement = list()
            currentElement.append(element[i])
        else:
            currentElement = element[i]
        
        currentFeatures = extractFeatureNames(currentElement)

        
        # Is the current element on the list
        for j in range(len(currentFeatureAsList)):
            if currentFeatureAsList[j] in includeList:
                # If yes, get the parameters
                extractedData = 5

#    i = includeList.index(element[0]._val)
#    extractedData[i] = element[1]
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
      
"""
build feature list that takes into account own goal and away goal naming issues.
"""          
def buildFeatureIncludeList(desiredFeatures, goalSide):
    featureList = list()
    
    # First, get the proper names of all the features in a list
    for i in range(len(desiredFeatures)):
        if desiredFeatures[i] == 'go':          # go is short for goal own
            featureList.append('g' + goalSide)
        elif desiredFeatures[i] == 'ga':        # ga is short for goal away
            if goalSide == 'gl':
                featureList.append('gr')
            else:
                featureList.append('gl')
        else:
            featureList.append(desiredFeatures[i])
        
    # Add indeces to the list elements
    featureList = generateFeatureListIndecies(featureList)
        
    return featureList


def generateFeatureListIndecies(featureList):
    indexedFeatureList = list()
    for i in range(len(featureList)):
        indexedFeatureList.append(featureList[i] + str(0))
        indexedFeatureList.append(featureList[i] + str(1))
    return indexedFeatureList