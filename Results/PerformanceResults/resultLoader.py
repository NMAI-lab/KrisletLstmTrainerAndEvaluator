# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:59:27 2019

@author: Patrick
"""

import csv
from sklearn.metrics import f1_score
from os import listdir


def getAllScores(logPath):
    files = listdir(logPath)
    scores = list()
    for name in files:
        scores.append(getTestScore(logPath + "/" + name))
        
    return (files,scores)


def getTestScore(path):
    
    # Initialize the data lists
    true = list()
    predicted = list()
    
    # Get the file names in this directory
    fileNames = listdir(path)
    
    # Get scores from each file
    for currentFileName in fileNames:
        currentPath = path + "/" + currentFileName
        (currentTrue, currentPredicted) = loadResults(currentPath)
        
        true.extend(currentTrue)
        predicted.extend(currentPredicted)
        
    scores = getFMeasure(true, predicted)
    
    # Return result
    return scores
    

def loadResults(fileName):
    
    with open(fileName, mode='r') as csv_file:
        resultFile = csv.DictReader(csv_file)
        expertAction = list()
        studentAction = list()
    
        for row in resultFile:
            expertAction.append(row.get("Expert"))
            studentAction.append(row.get("Student"))
            
    return (expertAction, studentAction)

def getFMeasure(true, predicted, numClasses = 4):
    minLabel = int(min(true))
    maxLabel = int(max(true)) + 1
    labels = [i for i in range(numClasses)]
    return f1_score(true, predicted, labels = labels, average = None)

