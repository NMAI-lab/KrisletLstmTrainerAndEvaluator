# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:40:06 2018

@author: patrickgavigan
"""

import numpy as np

# Evaluate the specificity
def evaluateSpecificity(y, yPredicted, labels):
    numLabels = len(labels)
    Sp = np.zeros(numLabels)
    for i in range(numLabels):
        currentClassID = labels[i]
        TN = getTrueNegative(y, yPredicted, currentClassID)
        FP = getFalsePositive(y, yPredicted, currentClassID)
        Sp[i] = TN / (TN + FP)
    return Sp

# Get the true negatives
def getTrueNegative(y, yPredicted, classID):
    TN = 0
    for i in range(len(y)):
        if ((y[i] != classID) and (yPredicted[i] != classID)):
            TN = TN + 1
    return TN


# Cound the false positives
def getFalsePositive(y, yPredicted, classID):
    FP = 0
    for i in range(len(y)):
        if ((y[i] != classID) and (yPredicted[i] == classID)):
            FP = FP + 1
    return FP

def getSummaryStatistics(result):
    accuracy = list()
    precision = list()
    sensitivity = list()
    specificity = list()
    fMeasure = list()
    
    for i in range(len(result)):
        (accuracyCurrent, precisionCurrent, sensitivityCurrent, specificityCurrent, fMeasureCurrent) = result[i]
        accuracy.append(accuracyCurrent)
        precision.append(precisionCurrent)
        sensitivity.append(sensitivityCurrent)
        specificity.append(specificityCurrent)
        fMeasure.append(fMeasureCurrent)
        
    accuracySummary = getConfidenceRange(accuracy)
    precisionSummary = getConfidenceRange(precision)
    sensitivitySummary = getConfidenceRange(sensitivity)
    specificitySummary = getConfidenceRange(specificity)
    fMeasureSummary = getConfidenceRange(fMeasure)
  
    return (accuracySummary, precisionSummary, sensitivitySummary, specificitySummary, fMeasureSummary)


def getConfidenceRange(values):
    values = np.asarray(values)
    mean = np.mean(values, axis = 0)
    standardDeviation = np.std(values, axis = 0)
    return (mean, standardDeviation)
    