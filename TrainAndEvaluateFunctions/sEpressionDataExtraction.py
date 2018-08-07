# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:38:05 2018

@author: patrickgavigan
"""

from sexpdata import loads, Symbol #,load, dumps

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


def getActionList(data):
    actions = list()
    for i in range(len(data)):
        currentResult = data[i]
        currentAction = currentResult[0]._val
        if (currentAction in actions) == False:
            actions.append(currentAction)
    return actions


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

def getRunTable(data, actionList, featureList):
    x = []
    y = []
    return (x,y)