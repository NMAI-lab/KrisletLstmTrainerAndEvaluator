# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:04:38 2018

@author: patrickgavigan
"""

#import numpy as np
from sklearn.model_selection import StratifiedKFold

from configutationGenerator import getMaxDepth

from parsingFunctions import loadData
#from dataManagement import convertToCategorical
#from balancingFunctions import underSample, checkBalance

from dataManagement import cropSequenceLength#, getDataSpecification
from modelTrainEvaluateFunctions import trainWithCrossValidation#, crossValidateModelConfiguration
#from modelTrainEvaluateFunctions import evaluateModel
#from modelGenerators import getNumConfigurations
from modelSave import saveModel


def runTestCase(testType, configurations):
    
    # Determine the largest depth, get data set for max depth case. Will need 
    # to crop data depth for cases where smaller depth is to be used
    maxDepth = getMaxDepth(configurations)
    data = loadData(testType, maxDepth)
    
    # Should we deal with placeholder calues?
    # finalData = replacePlaceholder(balancedData[0])
    
    # Run nested cross validation
    results = crossValidateConfiguration(data, configurations)
    
    # Print results
    printResultSummary(testType, results)
    
def crossValidateConfiguration(data, configurations):
    
    # Deal with multi configuration case
    if (len(configurations) > 1):
        (x, y) = (data)
        numConfigurations = len(configurations)
        skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
        results = list()
        configuration = 0
        note = 'NestedCrossValidation'
        for trainIndex, testIndex in skf.split(x, y):
            print("Running configuration", configuration, "/", numConfigurations)
            
            currentDepth = configurations[configuration][0]
        
            # Crop the data depth, if necessary
            currentX = cropSequenceLength(x, currentDepth)
        
            # Perform cross validation for this configuration
            (model, scoreOfFoldsBalanced, scoreOfFoldsUnbalanced) = trainWithCrossValidation((currentX[testIndex], y[testIndex]), configurations[configuration])
            currentResult = (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configurations[configuration])
            results.append(currentResult)
        
            # Print results, save model
            printConfigurationResultSummary(currentResult)
        
            # Save the model as a file and then clear the memory
            saveModel(model, currentResult, note)
            model = None
        
            configuration = configuration + 1
    
    # Deal with single configuration case
    else:
        currentConfiguration = configurations[0]
        (model, scoreOfFoldsBalanced, scoreOfFoldsUnbalanced) = trainWithCrossValidation(data, currentConfiguration)
        currentResult = (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, currentConfiguration)
        
        # Print results, save model
        printConfigurationResultSummary(currentResult)
        
        # Save the model as a file and then clear the memory
        note = 'SingleConfiguration'
        saveModel(model, currentResult, note)

    # Return results    
    return results