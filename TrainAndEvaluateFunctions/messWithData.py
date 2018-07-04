# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from parsingFunctions import loadData, replacePlaceholder
#from dataManagement import convertToCategorical
from balancingFunctions import underSample, checkBalance

testType = "stateBasedKrislet"
depth = 2
data = loadData(testType, depth)

balancedData = underSample(data)

originalBalance = checkBalance(data)
newBalance = checkBalance(balancedData)

finalData = replacePlaceholder(balancedData[0])

#yCategorical = convertToCategorical(data[1])