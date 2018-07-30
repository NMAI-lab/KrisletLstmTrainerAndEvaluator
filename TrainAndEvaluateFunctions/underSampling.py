# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:00:28 2018

@author: patrickgavigan
"""

import numpy as np
import random
from balancingFunctions import checkBalance, getIndecesOfValueInData, shuffleOrder
from constants import getRandomSeed

# Perform random undersampling
def randomUnderSample(data):
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
        random.seed(getRandomSeed())
        keepIndeces = random.sample(classIndeces, numToKeep)
    return keepIndeces