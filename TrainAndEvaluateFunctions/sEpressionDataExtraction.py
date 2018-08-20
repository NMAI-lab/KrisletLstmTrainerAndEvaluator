# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:38:05 2018

@author: patrickgavigan
"""

from parsingFunctions import getFileNames
from dataManagement import buildSequenceDataSet, convertToClassID, convertToCategorical 
from sexpdata import loads, Symbol
import numpy as np


"""
Load data stored in S-Expression log files
"""
def loadData(testType, depth):
        
    # Get the file names for available data
    #testType = 'sexpt_tests'
    fileNames = getFileNames(testType)

    # Setup feature parameters
    # Need to clean this up
    actionIncludeList = ['turn', 'dash', 'kick']
    featureCheckActionList = ['see']
    includeList = list()
    includeList.extend(actionIncludeList)
    includeList.extend(featureCheckActionList)

    # ga is short for goal adversary (where we don't want the ball to go)
    # go is short for goal own (where we want the ball to go)
    featureIncludeList = ['b','ga']#['b','go','ga']

    for i in range(len(fileNames)):
        # Load S-expressions from the first file
        (data, goalSide) = getReducedFileData(fileNames[i], includeList)

        # Get the run table from the current file
        (xCurrent,yCurrent) = getRunTable(data, actionIncludeList, featureCheckActionList, featureIncludeList, goalSide)
        
        # Convert to 1 hot categorical (need to revisit this)
        yCurrent = convertToBinaryCategoricalFromAnalog(yCurrent)
        
        # Turn this into a sequenced run
        (xCurrent, yCurrent) = buildSequenceDataSet(xCurrent, yCurrent, depth)
    
        # Add this to the existing (or create new) trace table
        if i == 0:
            x = xCurrent
            y = yCurrent
        else:
            x = np.append(x, xCurrent, axis = 0)
#            if (np.shape(y)[1]) != (np.shape(yCurrent)[1]):
#                print(np.shape(y))
#                print(np.shape(yCurrent))
            y = np.append(y, yCurrent, axis = 0)
        
    return (x,y)


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
Converts a data table (for the y data) to a 1 hot categorical given a data table
containing raw 'analog' results for each of the possible y values
"""
def convertToBinaryCategoricalFromAnalog(data):
    arrayLength = np.shape(data)[0]
    numCategories = np.shape(data)[1]
    
    for i in range(arrayLength):
        for j in range(numCategories):
            if data[i,j] > 0:
                data[i,j] = 1
    return data 
   

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
            x[i,:] = extractFeature(currentResult, featureNameList, featureActionList)
            featureCount = featureCount + 1
        
    # Reduce rows
    (x,y) = clearBlankRows(x,y)
        
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
    
    newIncludeList = list()
    for i in range(len(includeList)):
        newItem = includeList[i][:-1]
        if (newItem in newIncludeList) == False:
            newIncludeList.append(newItem)
    includeList = newIncludeList
        
    availableFeatures = [None, None]
    availableFeatures.extend(extractFeatureNames(element))
    
    numElements = 2 * len(includeList)      # Features have 2 parameters
    extractedData = np.zeros(numElements)
    
    for i in range(len(availableFeatures)):
        if ((availableFeatures[i] is None) == False):
            if (availableFeatures[i] in includeList):
                featureIndex = 2 * includeList.index(availableFeatures[i])
                extractedData[featureIndex] = element[i][1]
                featureIndex = featureIndex + 1
                extractedData[featureIndex] = element[i][2]
    return extractedData


"""
Determine which side the goal is. Goal side is opposite of the chracter in the 
init message in the log file. (r means that the goal is on the l side and vice 
versa)
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
build feature list that takes into account own goal and away goal naming issues.
"""          
def buildFeatureIncludeList(desiredFeatures, goalSide):
    featureList = list()
    
    # First, get the proper names of all the features in a list
    for i in range(len(desiredFeatures)):
        if desiredFeatures[i] == 'ga':          # ga is short for goal adversary (where we don't want the ball to go)
            featureList.append('g' + goalSide)
        elif desiredFeatures[i] == 'go':        # go is short for goal own (where we want the ball to go)
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


"""
Removes blank rows in the x and y tables. Also, aligns rows of y with the 
corresponding x
"""
def clearBlankRows(x, y):
    newX = np.zeros(np.shape(x))
    newY = np.zeros(np.shape(y))
    
    numElements = np.shape(x)[0]
    numXFeatures = np.shape(x)[1]
    blankXFeature = np.zeros(numXFeatures)
    
    newRowI = 0
    for i in range(numElements):
        # Check if the current x has any data in it, not the last row
        if (np.array_equal(blankXFeature,x[i,:]) == False) and (i < (numElements-1)):
            # Check to make sure that the next row isn't a new set of features
            if (np.array_equal(blankXFeature,x[i+1,:])):
                newX[newRowI,:] = x[i,:]
                newY[newRowI,:] = y[i+1,:]
                newRowI = newRowI + 1
    
    xReduced = newX[0:newRowI,:]
    yReduced = newY[0:newRowI,:]
    
    return(xReduced, yReduced)
