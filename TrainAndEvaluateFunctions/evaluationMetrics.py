# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:40:06 2018

@author: patrickgavigan
"""

import numpy as np

# Evaluate the specificity
def evaluateSpecificity(y, yPredicted, labels):
    Sp = np.zeros(labels.size)
    for currentClassID in range(labels):
        TN = getTrueNegative(y, yPredicted, currentClassID)
        FP = getFalsePositive(y, yPredicted, currentClassID)
        Sp[currentClassID] = TN / (TN + FP)
    return Sp

# Get the true negatives
def getTrueNegative(y, yPredicted, classID):
    TN = 0
    for i in range(len(y)):
        if ((y != classID) and (yPredicted != classID)):
            TN = TN + 1
    return TN


# Cound the false positives
def getFalsePositive(y, yPredicted, classID):
    FP = 0
    for i in range(len(y)):
        if ((y != classID) and (yPredicted == classID)):
            FP = FP + 1
    return FP