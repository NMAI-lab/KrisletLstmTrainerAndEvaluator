import numpy as np
import random

#parses a single line of bayesian.txt e.g. 0.1, 0.2, 0.3
def parse(line):
    line = [float(i) for i in line.split(',')]
    lastCharacter = len(line) - 1
    return [line[:lastCharacter], [line[lastCharacter]]]

def parseFile(fileName = "logFile.txt"):
    x = list()
    y = list()
    with open(fileName) as f:
        for line in f:
            (currentX, currentY) = (parse(line))
            x.append(currentX)
            y.append(currentY[0])
    return (x, y)

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