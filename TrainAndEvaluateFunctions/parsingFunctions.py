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

def buildHistory(x, y, depth = 5):
    
    numFeatures = len(x[0]) + 1
    numSamples = len(y)
    numNewSamples = numSamples - (depth - 1)
    
    newX = np.zeros((depth, numFeatures, numNewSamples))
    newY = np.zeros(numNewSamples)
    firstY = random.choice(y)
    
    for i in range (numNewSamples - 1):
        for j in range (numFeatures - 1):
            for k in range (depth - 1):
                newX[k,j,i] = x[k,j+i]
                newY[i] = y[i + depth]
        
    
    return newX, newY