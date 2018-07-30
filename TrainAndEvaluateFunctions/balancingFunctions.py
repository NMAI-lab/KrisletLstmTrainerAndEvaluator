# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:19:11 2018

@author: patrickgavigan
"""

from constants import getRandomSeed
from collections import Counter
#from imblearn.over_sampling import SMOTE 

from underSampling import randomUnderSample

import numpy as np
import random

# Options include: None, "randomUndersample". If option is other than those
# listed, default of "none" is used.
def balanceData(data, methodology = None, balanceThreshold = 0.05):
    originalBalance = np.asarray(checkBalance(data))
    if (np.std(originalBalance) > balanceThreshold):
        if methodology == "randomUndersample":
            # Balance the data set
            return randomUnderSample(data)
    
    # contingency return value - do nothing
    return data

# Get indeces of all elements of data that correspond to provided classID
def getIndecesOfValueInData(data, value):
    valueIndeces = list()
    for i in range(len(data)):
        if data[i] == value:
                valueIndeces.append(i)
    return valueIndeces
    
# Shuffles the order of the data elements
def shuffleOrder(data):
    (x,y) = data
    xNew = np.zeros(np.shape(x))
    yNew = np.zeros(np.shape(y))
    maxRange = len(y)
    random.seed(getRandomSeed())
    newOrder = random.sample(range(0, maxRange), maxRange)
    
    for i in range(maxRange):
        j = newOrder[i]
        xNew[i] = x[j]
        yNew[i] = y[j]
    
    return (xNew, yNew)

# Check the balance of the classes. Returns list of how many items data points 
# for each class exist.
def checkBalance(data):
    y = data[1].astype(int, copy = True)
    balanceCounter = Counter(y)
    
    balance = list()
    for i in range(len(balanceCounter)):
        balance.append(balanceCounter[i])
        
    return balance