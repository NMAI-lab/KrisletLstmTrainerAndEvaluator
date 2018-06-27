# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from parsingFunctions import loadData
from dataManagement import convertToCategorical

testType = "stateBasedKrislet"
depth = 2
data = loadData(testType, depth)

yCategorical = convertToCategorical(data[1])