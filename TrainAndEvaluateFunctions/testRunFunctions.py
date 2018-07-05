# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:04:38 2018

@author: patrickgavigan
"""
from parsingFunctions import loadData, replacePlaceholder
#from dataManagement import convertToCategorical
from balancingFunctions import underSample, checkBalance

from dataManagement import getData
from modelTrainEvaluateFunctions import trainWithCrossValidation, crossValidateModelConfiguration
from modelTrainEvaluateFunctions import evaluateModel
from modelGenerators import getNumConfigurations
from modelSave import saveModel


def runTestCase(testType, configurations):
    (accuracyOfConfigurations, deviationOfConfigurations) = crossValidateConfiguration(testType, configurations)
    printResults(testType, configurations, accuracyOfConfigurations, deviationOfConfigurations)
    
def crossValidateConfiguration(testType, configurations):
    
    numConfigurations = len(configurations)
    skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
    accuracyOfConfigurations = np.zeros(numConfigurations)
    deviationOfConfigurations = np.zeros(numConfigurations)
    nFolds = 10
    i = 0
    note = 'NestedCrossValidation'
    (x, y) = (data)
    for trainIndex, testIndex in skf.split(x, y):
        
        # Need to solve chicken and egg problem of run length and splitting each needing to be done before the other.
        
        print("Running configuration", i, "/", numConfigurations)
        
        # Perform cross validation for this configuration, save results. Do not save the model due to memory limit issues.
        (model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, (x[testIndex], y[testIndex]), configurations[i], dataSpecification)
        accuracyOfConfigurations[i] = accuracyMean
        deviationOfConfigurations[i] = accuracyStandardDeviation
        
        saveModel(model, configuration, accuracyMean, accuracyStandardDeviation, note)
        model = None    # Clear up some memory
        
        print("Accuracy of configuration ", configuration, ": ", (accuracyMean * 100), " +/- ", (accuracyStandardDeviation * 100))
        configuration = configuration + 1
        i = i + 1
    
    return (accuracyOfConfigurations, deviationOfConfigurations)
    
    
    
    
    
    #loadData(testType, depth)
#    balancedData = underSample(data)
    
#   originalBalance = checkBalance(data)
#   newBalance = checkBalance(balancedData)

#    finalData = replacePlaceholder(balancedData[0])

    #yCategorical = convertToCategorical(data[1])
    
    accuracyOfConfigurations = 0
    deviationOfConfigurations = 0
    
    
    return (accuracyOfConfigurations, deviationOfConfigurations)
    

def printResults(testType, configurations, accuracyOfConfigurations, deviationOfConfigurations):    
    print('--------------------------------')
    print('Summary of ' + testType + ' test')

    numConfigurations = getNumConfigurations()
    for i in range(numConfigurations):
        print('Configuration ', i, " Accuracy : ", accuracyOfConfigurations[i], " +/- ", deviationOfConfigurations[i])
    
    print('--------------------------------')


