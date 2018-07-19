# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:04:38 2018

@author: patrickgavigan
"""

import numpy as np
from sklearn.model_selection import StratifiedKFold

from configutationGenerator import getMaxDepth

from parsingFunctions import loadData
#from dataManagement import convertToCategorical
from balancingFunctions import underSample, checkBalance

from dataManagement import getData, cropSequenceLength, getDataSpecification
from modelTrainEvaluateFunctions import trainWithCrossValidation, crossValidateModelConfiguration
from modelTrainEvaluateFunctions import evaluateModel
from modelGenerators import getNumConfigurations
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
    printResults(testType, configurations, results)
    
def crossValidateConfiguration(data, configurations):
    
    numConfigurations = len(configurations)
    skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
    accuracyOfConfigurations = np.zeros(numConfigurations)
    deviationOfConfigurations = np.zeros(numConfigurations)
    nFolds = 10
    configuration = 0
    note = 'NestedCrossValidation'
    (x, y) = (data)
    for trainIndex, testIndex in skf.split(x, y):
        print("Running configuration", configuration, "/", numConfigurations)
        
        currentDepth = configurations[configuration][0]
        
        # Crop the data depth, if necessary
        currentX = cropSequenceLength(x, currentDepth)
        
        # Perform cross validation for this configuration
        (model, scores) = trainWithCrossValidation(nFolds, (currentX[testIndex], y[testIndex]), configurations[configuration])
        
        # Extract performance results
        #accuracyOfConfigurations[configuration] = accuracyMean
        #deviationOfConfigurations[configuration] = accuracyStandardDeviation
        
        # Save the model as a file and then clear the memory
        #saveModel(model, configuration, accuracyMean, accuracyStandardDeviation, note)
        #model = None
        
        #print("Accuracy of configuration ", configuration, ": ", (accuracyMean * 100), " +/- ", (accuracyStandardDeviation * 100))
        configuration = configuration + 1

    # Return results    
    return (accuracyOfConfigurations, deviationOfConfigurations)
    
# Print a summary of the test run
def printResults(testType, configurations, results): 
    (accuracyOfConfigurations, deviationOfConfigurations) = results
    print('--------------------------------')
    print('Summary of ' + testType + ' test')

    numConfigurations = getNumConfigurations()
    for i in range(numConfigurations):
        print('Configuration ', i, " Accuracy : ", accuracyOfConfigurations[i], " +/- ", deviationOfConfigurations[i])
    
    print('--------------------------------')