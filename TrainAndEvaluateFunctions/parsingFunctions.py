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