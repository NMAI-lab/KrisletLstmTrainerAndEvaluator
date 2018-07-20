# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:04:38 2018

@author: patrickgavigan
"""

from configutationGenerator import getMaxDepth
from parsingFunctions import loadData
from resultOutput import printResultSummary
from crossValidation import crossValidateConfiguration

def runTestCase(testType, configurations):
    
    # Determine the largest depth, get data set for max depth case. Will need 
    # to crop data depth for cases where smaller depth is to be used
    maxDepth = getMaxDepth(configurations)
    data = loadData(testType, maxDepth)
    
    # Should we deal with placeholder calues?
    # finalData = replacePlaceholder(balancedData[0])
    
    # Feature selection?
    
    # Run nested cross validation
    results = crossValidateConfiguration(data, configurations)
    
    # Print results
    printResultSummary(testType, results)