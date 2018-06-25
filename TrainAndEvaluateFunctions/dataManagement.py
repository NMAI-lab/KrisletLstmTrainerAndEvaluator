# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:35:58 2018

@author: patrickgavigan
"""

import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.utils import np_utils
from sklearn.model_selection import StratifiedShuffleSplit
from parsingFunctions import parseFile
import random

def getData():

    # This function needs to be reimplemented for the Krislet logs. For now,
    # it's a hack based on a tutorial. Currently, combining the imdb data
    # training and testing data into a single data set in order to have a
    # sample data set for testing nexted cross-validation functionality in 
    # other parts of this program.

    
    # Need to get rid of these variables
    top_words = 5000
    max_review_length = 500
        
    # Load the dataset but only keep the top n words, zero the rest
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)

    # Truncate and pad input sequences
    X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
    X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

    # Concatenate the data
    x = np.concatenate((X_train, X_test), axis=0)
    y = np.concatenate((y_train, y_test), axis=0)

    # Return result
    return (X_train, y_train), (X_test, y_test), (x, y)

def getLogFileData():
    (x,y) = parseFile()
    depth = 2
    (newX, newY) = buildSequenceDataSet(x, y, depth)
    return (newX,newY)
    

def stratefiedSplit(x, y):
    nSplits = 1
    testProportion = 0.2
    splits = StratifiedShuffleSplit(nSplits, testProportion)
    splits.get_n_splits(x, y)
    
    for trainIndex, testIndex in splits.split(x, y):
        xTrain, xTest = x[trainIndex], x[testIndex]
        yTrain, yTest = y[trainIndex], y[testIndex]
        
    return (xTrain, yTrain), (xTest, yTest)

# Builds the dequence data set using the provided depth setting
def buildSequenceDataSet(x, y, maxDepth = 3):
    # Use lists (in order to append the next element)
    xList = list()
    yList = list()
    
    # Add the previous y to the current x features
    x = addPreviousYAsFeature(x,y)
    
    # Iterate through the elements
    for index in range(len(x)):
        (currentX, currentY) = buildSingleSequence(x, y, index, maxDepth)
        xList.append(currentX)
        yList.append(currentY)
        
    # Convert to arrays
    newX = np.asarray(xList)
    newY = np.asarray(yList)

    # Return results
    return newX, newY

# Build a history sequence based on given x, y for a given index of x. 
# The depth specifies how far back in history to go
def buildSingleSequence(x, y, index, depth):
    # Set parameters (number of features)
    numFeatures = len(x[0])
    
    # Setup return values
    sequenceY = y[index]
    sequenceX = np.zeros((numFeatures, depth))
    
    # Iteratively build the return values (iterates through the depth)
    j = depth
    for currentDepth in range(index, index-depth, -1):
        j = j - 1
        if currentDepth < 0:
            # deal with case where there is no more data and we need to pad
            currentX = np.zeros(numFeatures)
        else:
            # Get current x array of features
            currentX = x[currentDepth]
        
        # Copy current x features to the output matrix
        for i in range(0, numFeatures):
            sequenceX[i,j] = currentX[i]            
            
    # Return the results
    return (sequenceX, sequenceY)
    
# Adds the result for the previous steps's Y as a feature of the current step 
# in X
def addPreviousYAsFeature(x,y):
    for i in range(len(x)):
        if i == 0:
            x[i].append(random.choice(y))
        else:
            x[i].append(y[i-1])
    return x

# Converts the y data to categorical (for use with softmax activartion)
def convertToCategorical(y):
    ySet = set(y)
    numCategories = len(ySet)
    yCategorical = np_utils.to_categorical(y, numCategories)
    return (yCategorical, numCategories)

# Gets the dimensions of the x data
def getInputDimensions(x):
    xShape = x.shape
    numElements = xShape[0]
    sequenceLength = xShape[1]

    if len(xShape) == 3:
        elementDimension = xShape[2]
    else:
        elementDimension = 1
        
    return (elementDimension, sequenceLength, numElements)