# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:35:58 2018

@author: patrickgavigan
"""

import numpy as np
#from keras.datasets import imdb
#from keras.preprocessing import sequence
from keras.utils import to_categorical
from sklearn.model_selection import StratifiedShuffleSplit
#from parsingFunctions import parseFile
import random
from constants import getRandomSeed

#def getData():
#
#    # This function needs to be reimplemented for the Krislet logs. For now,
#    # it's a hack based on a tutorial. Currently, combining the imdb data
#    # training and testing data into a single data set in order to have a
#    # sample data set for testing nexted cross-validation functionality in 
#    # other parts of this program.
#
#    
#    # Need to get rid of these variables
#    top_words = 5000
#    max_review_length = 500
#        
#    # Load the dataset but only keep the top n words, zero the rest
#    (xTrain, yTrain), (xTest, yTest) = imdb.load_data(num_words=top_words)
#
#    # Truncate and pad input sequences
#    xTrain = sequence.pad_sequences(xTrain, maxlen=max_review_length)
#    xTest = sequence.pad_sequences(xTest, maxlen=max_review_length)
#
#    # Concatenate the data
#    x = np.concatenate((xTrain, xTest), axis=0)
#    y = np.concatenate((yTrain, yTest), axis=0)
#    
#    numCategories = getNumCategories(y)
#    (numElements, sequenceLength, elementDimension) = getInputDimensions(x)
#
#    # Return result
#    return (xTrain, yTrain), (xTest, yTest), (x, y), (numCategories, elementDimension, sequenceLength)

#def getLogFileData():
#    (x,y) = parseFile()
#    depth = 2
#    (newX, newY) = buildSequenceDataSet(x, y, depth)
#    return (newX,newY)


# Get the specifications of the data set
def getDataSpecification(data):
    (x,y) = data
    #xShape = x.shape
    
    (_, sequenceLength, numFeatures) = getInputDimensions(x)
    
    # Sequence length is the 0th parameter
    #sequenceLength = xShape[0]
    
    # Use shape of the first element to get element dimensions
    #elementDimension = x[0].shape
    #if len(elementDimension) > 1:
    #    sequenceLength = elementDimension[1]
    #    numFeatures = elementDimension[0]
    #else:
    #    sequenceLength = 0
    #    numFeatures = elementDimension[0]
    
    # Get the number of categories
    numCategories = getNumCategories(y)
    
    # Return result
    return (numCategories, numFeatures, sequenceLength)


# Gets the dimensions of the x data
def getInputDimensions(x):
    xShape = x.shape
    numElements = xShape[0]

    # Deal with the less than 3 dimensional case    
    if len(xShape) > 2:
        sequenceLength = xShape[1]
        elementDimension = xShape[2]
    else:
        elementDimension = xShape[1]
        sequenceLength = 0
        
    # Return result
    return (numElements, sequenceLength, elementDimension)


def stratefiedSplit(x, y):
    nSplits = 1
    testProportion = 0.2
    splits = StratifiedShuffleSplit(nSplits, testProportion, random_state = getRandomSeed())
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
    
    # Add the previous y to the current x features if depth is greater than 0
    if maxDepth > 0:
        x = addPreviousYAsFeature(x,y)
        
    if maxDepth > 1:
    
        # Iterate through the elements
        for index in range(len(x)):
            (currentX, currentY) = buildSingleSequence(x, y, index, maxDepth)
            xList.append(currentX)
            yList.append(currentY)
        
        # Convert to arrays
        newX = np.asarray(xList)
        newY = np.asarray(yList)
        
    # Deal with null case where depth is smaller than 1
    else:
        newX = x
        newY = y

    # Return results
    return newX, newY

# Build a history sequence based on given x, y for a given index of x. 
# The depth specifies how far back in history to go
def buildSingleSequence(x, y, index, depth):
    # Set parameters (number of features)
    numFeatures = len(x[0])
    
    # Setup return values
    sequenceY = y[index]
    sequenceX = np.zeros((depth, numFeatures))
    
    # Iteratively build the return values (iterates through the depth)
    i = depth
    for currentDepth in range(index, index-depth, -1):
        i = i - 1
        if currentDepth < 0:
            # deal with case where there is no more data and we need to pad
            currentX = np.zeros(numFeatures)
        else:
            # Get current x array of features
            currentX = x[currentDepth]
        
        # Copy current x features to the output matrix
        for j in range(0, numFeatures):
            sequenceX[i,j] = currentX[j]            
            
    # Return the results
    return (sequenceX, sequenceY)
    
# Adds the result for the previous steps's Y as a feature of the current step 
# in X
def addPreviousYAsFeature(x,y):
    dim0 = np.size(x,0)
    dim1 = np.size(x,1) + 1
    newX = np.zeros((dim0, dim1))
    for i in range(dim0):
        for j in range(dim1):
            if ((i == 0) and (j == dim1 - 1)):
                # Insert random y for first case (there is no previous case)
                newX[i,j] = random.choice(y)
            elif ((i != 0) and (j == dim1 - 1)):
                newX[i,j] = y[i-1]
            else:
                newX[i,j] = x[i,j]
    return newX

# Returns the number of categories of data set
def getNumCategories(y):
    ySet = set(y)
    numCategories = len(ySet)
    return numCategories

# Converts the y data to categorical (for use with softmax activartion)
def convertToCategorical(y):
    numCategories = getNumCategories(y)
    yCategorical = to_categorical(y, numCategories)
    return yCategorical


def convertToClassID(yCategorical):
    numElements = yCategorical.shape[0]
    y = np.zeros(numElements)
    for i in range(numElements):
        y[i] = np.argmax(yCategorical[i])
    return y
   
# Known issu: Can't crop from depth 1 to depth 0
def cropSequenceLength(data, depth):
    # Get data dimensions
    (numElements, sequenceLength, elementDimension) = getInputDimensions(data)
    
    # Deal with case where the desired depth is the same length (or longer) 
    # than the provided data depth
    if depth >= sequenceLength:
        newData = data
        
    # Deal with special case where new depth is 0 (or negative). In this case, 
    # need to remove last feature (previous action) as well as remove the data
    # from the previous time steps
    elif depth <= 0:
        maxDimension = elementDimension - 1
        startIndex = sequenceLength - 1
        newData = data[:, startIndex, 0:maxDimension]

    # Deal with special case for depth = 1 (last action kept but otherwise depth 0)
    elif depth == 1:
        startIndex = sequenceLength - 1
        newData = data[:, startIndex, :]
        
    # No funny business, just shorten the history depth    
    else:
        endIndex = sequenceLength - 1
        startIndex = endIndex - depth
        newData = data[:, startIndex:endIndex, :]

    # Return the result    
    return newData