from os import listdir
import numpy as np
from os.path import isdir

from dataManagement import buildSequenceDataSet

def loadData(testType, depth):
    fileNames = getFileNames(testType)
    for i in range(len(fileNames)):
        (xCurrent,yCurrent) = parseFile(fileNames[i])
        (xCurrent, yCurrent) = buildSequenceDataSet(xCurrent, yCurrent, depth)
    
        if i == 0:
            x = xCurrent
            y = yCurrent
        else:
            x = np.append(x, xCurrent, axis = 0)
            y = np.append(y, yCurrent, axis = 0)
        
    return (x,y)
    

"""
"""
def getFileNames(testType):
    
    # Initialize the output list
    fileNames = list()
    
    # Establish if this is a full path or just the last directory name
    if isdir(testType):
        # Path is the test type
        path = testType
    else:
        # Need to turn into a full path name
        path = "data/" + testType + "/"
       
    # Get the file names in this directory
    fileNamesInDirectory = listdir(path)
     
    # interate through fileNamesInDirectory
    for i in range(len(fileNamesInDirectory)):
        currentPath = path + fileNamesInDirectory[i]

        # If this is a directory, need to enter the directory and repeat
        # (recursive). Otherwise, add to the list
        if isdir(currentPath):
            # Use extend, the function will return a list
            fileNames.extend(getFileNames(currentPath + '/'))
        else:
            # Use append, we are adding a single string to the end of the list
            # (if we use extend, it will add each character to the list 
            # individually)
            fileNames.append(currentPath)
    
    # Return the result
    return fileNames


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
    y = shiftIndex(y)
    return (x, y)


def shiftIndex(data):
    for i in range(len(data)):
        data[i] = data[i] - 1
    return data

# Krislet log files contain 6.6 as placeholder values instead of NULL. Need to
# fine and replace these values with 0.
    # Implemented using recursion as the input can be multidimensional
def replacePlaceholder(x, currentPlaceholder = 6.6, newPlaceholder = 0):
    # Deal with the case where a scalar has been passed in.
    if (np.shape(x) == ()):
        if x == currentPlaceholder:
            x = newPlaceholder
    
    # Deal with vector or matrix case by calling function recursively
    else:
        for i in range(len(x)):
            x[i] = replacePlaceholder(x[i], currentPlaceholder, newPlaceholder)
    
    return x