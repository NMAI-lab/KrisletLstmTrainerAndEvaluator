# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:47:51 2018

@author: patrickgavigan
"""

from sklearn.model_selection import StratifiedKFold
from configutationGenerator import getBalanceOption, getConfigID
from dataManagement import cropSequenceLength
from modelTrainEvaluateFunctions import defineAndTrainModel, evaluateModel
from resultOutput import printConfigurationResultSummary
from modelSave import saveModel
from constants import getRandomSeed
from csvLogFunctions import writeCSVResult

def trainWithCrossValidation(data, configuration, nFolds = 10):
    
    # Get the data specifications
    #dataSpecification = getDataSpecification(data)

    # Extract data
    (x, y) = (data)
    
    # Setup the folds
    skf = StratifiedKFold(n_splits = nFolds, random_state = getRandomSeed())
    scoreOfFoldsBalanced = list()
    scoreOfFoldsUnbalanced = list()
    foldNumber = 1
    
    # Cross validation loop
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Define and train the model
        model = defineAndTrainModel((x[trainIndex], y[trainIndex]), configuration)#, dataSpecification)
    
        # Test the model
        balance = getBalanceOption(configuration)
        scoreOfFoldsBalanced.append(evaluateModel(model, (x[testIndex], y[testIndex]), balance))
        balance = None
        scoreOfFoldsUnbalanced.append(evaluateModel(model, (x[testIndex], y[testIndex]), balance))
        
        foldNumber = foldNumber + 1
        
    # Train the final model
    model = defineAndTrainModel((x, y), configuration)#, dataSpecification)
    
    # Get performance estimations
    #accuracyMean = np.mean(accuracyOfFolds)
    #accuracyStandardDeviation = np.std(accuracyOfFolds)
    
    # Return results
    return (model, scoreOfFoldsBalanced, scoreOfFoldsUnbalanced)


def crossValidateConfiguration(data, configurations, testType):
    numConfigurations = len(configurations)
    configurationIndex = 0
    results = list()
    
    # Deal with multi configuration case
    if (numConfigurations > 1):
        (x, y) = (data)
        skf = StratifiedKFold(n_splits = numConfigurations, random_state = getRandomSeed())
        note = 'NestedCrossValidation'
        for trainIndex, testIndex in skf.split(x, y):
            configurationID = getConfigID(configurations[configurationIndex])
            print("Running ", testType, " configuration ", configurationID, "/", numConfigurations)
            
            currentResult = crossValidateLoopIteration((x[testIndex], 
                                                        y[testIndex]), 
                                                        configurations[configurationIndex],
                                                        testType,
                                                        note)
            results.append(currentResult)
            configurationID = configurationIndex + 1
    
    # Deal with single configuration case
    else:
        note = 'SingleConfiguration'
        currentConfiguration = configurations[configurationIndex]
        configurationID = getConfigID(currentConfiguration)
        currentResult = crossValidateLoopIteration(data, currentConfiguration, 
                                                   testType, note)
        results.append(currentResult)

    # Return results    
    return results

def crossValidateLoopIteration(data, configuration, testType, note):

    # Crop the data depth, if necessary    
    (x,y) = data
    depth = configuration[0]
    currentX = cropSequenceLength(x, depth)
    data = (currentX, y)
    configurationID = getConfigID(configuration)
    
    # Train with cross validation
    (model, scoreOfFoldsBalanced, scoreOfFoldsUnbalanced) = trainWithCrossValidation(data, configuration)
    result = (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configuration)
    
    # Print results, save model
    printConfigurationResultSummary(result)
        
    # Save the model as a file and then clear the memory
    saveModel(model, result, configurationID, note)

    # Save result to the CSV log
    writeCSVResult(testType, result)

    # Return result
    return result
