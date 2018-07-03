# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:19:11 2018

@author: patrickgavigan
"""

from collections import Counter
#from imblearn.over_sampling import SMOTE 
import numpy as np
import random

# Perform random undersampling
def underSample(data):
    # Set parameters
    (x,y) = data
    balance = checkBalance(data)
    numSamplesEachClass = min(balance)
    numClasses = len(balance)
    newDataLength = numClasses * numSamplesEachClass
    xShape = np.shape(x)
    
    # Build arrays for output data
    xNew = np.zeros((newDataLength, xShape[1], xShape[2]))
    yNew = np.zeros(newDataLength)
    
    # Undersample each class
    i = 0
    for currentClass in range(numClasses):
        # Get the indeces of the elements we are keeping for this class
        indexList = getUnderSampledClassIndeces(y, currentClass, numSamplesEachClass)
        
        # Copy relevant values from original list
        for j in range(len(indexList)):
            currentIndex = indexList[j]
            xNew[i] = x[currentIndex]
            yNew[i] = y[currentIndex]
            i = i + 1
    
    # Shuffle the data
    newData = shuffleOrder((xNew, yNew))
    
    # Return undersampled data
    return (newData)
        

# Get the undersampled indeces for the specified class.
def getUnderSampledClassIndeces(y, classID, numToKeep):
    classIndeces = getIndecesOfValueInData(y, classID)
    if (len(classIndeces) <= numToKeep):
        keepIndeces = classIndeces
    else:
        keepIndeces = random.sample(classIndeces, numToKeep)
    return keepIndeces

# Get indeces of all elements of data that correspond to provided classID
def getIndecesOfValueInData(data, value):
    valueIndeces = list()
    for i in range(len(data)):
        if data[i] == value:
                valueIndeces.append(i)
    return valueIndeces
    

# Shuffles the order of the data elements
def shuffleOrder(data):
    (x,y) = data
    xNew = np.zeros(np.shape(x))
    yNew = np.zeros(np.shape(y))
    maxRange = len(y)
    newOrder = random.sample(range(0, maxRange), maxRange)
    
    for i in range(maxRange):
        j = newOrder[i]
        xNew[i] = x[j]
        yNew[i] = y[j]
    
    return (xNew, yNew)
    

# Perform oversampling on the data using SMOTE
#def overSample(data):
#    balance = checkBalance(data)
#    numSamplesEachClass = max(balance)
#    
#    return (X_res, y_res)

# Measures the distance between two data points: a and b. Assumes that both
# are members of the same class
#def getDistance(a,b):
    

# Check the balance of the classes. Returns list of how many items data points 
# for each class exist.
def checkBalance(data):
    y = data[1].astype(int, copy = True)
    balanceCounter = Counter(y)
    
    balance = list()
    for i in range(len(balanceCounter)):
        balance.append(balanceCounter[i])
        
    return balance