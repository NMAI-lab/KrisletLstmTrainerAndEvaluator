# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:40:06 2018

@author: patrickgavigan
"""

from sklearn.metrics import confusion_matrix
import numpy as np

def evaluateSpecificity(y, yPredicted, labels):
    confusionMatrix = confusion_matrix(y, yPredicted, labels)

    Sp = np.zeros(labels.size)
    
    for currentClassID in range(labels):
        TN = getTrueNegative(currentClassID, confusionMatrix)
        FP = getFalsePositive(currentClassID, confusionMatrix)
        Sp[currentClassID] = TN / (TN + FP)
    
    return Sp

def getTrueNegative(classID, confusionMatrix):
    return 1

def getFalsePositive(classID, confusionMatrix):
    return 1