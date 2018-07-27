# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:47:51 2018

@author: patrickgavigan
"""

from sklearn.model_selection import StratifiedKFold
from configutationGenerator import getBalanceOption
from dataManagement import getDataSpecification, cropSequenceLength
from modelTrainEvaluateFunctions import defineAndTrainModel, evaluateModel
from resultOutput import printConfigurationResultSummary
from modelSave import saveModel

def trainWithCrossValidation(data, configuration, nFolds = 10):
    
    # Get the data specifications
    #dataSpecification = getDataSpecification(data)

    # Extract data
    (x, y) = (data)
    
    # Setup the folds
    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
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


def crossValidateConfiguration(data, configurations):
    numConfigurations = len(configurations)
    configurationID = 0
    results = list()
    
    # Deal with multi configuration case
    if (numConfigurations > 1):
        (x, y) = (data)
        skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
        note = 'NestedCrossValidation'
        for trainIndex, testIndex in skf.split(x, y):
            print("Running configuration", configurationID, "/", numConfigurations)
            
            currentResult = crossValidateLoopIteration((x[testIndex], y[testIndex]), configurations[configurationID], configurationID, note)
            results.append(currentResult)
            configurationID = configurationID + 1
    
    # Deal with single configuration case
    else:
        note = 'SingleConfiguration'
        currentConfiguration = configurations[0]
        currentResult = crossValidateLoopIteration(data, currentConfiguration, configurationID,  note)
        results.append(currentResult)

    # Return results    
    return results

def crossValidateLoopIteration(data, configuration, configurationID, note):

    # Crop the data depth, if necessary    
    (x,y) = data
    depth = configuration[0]
    currentX = cropSequenceLength(x, depth)
    data = (currentX, y)
    
    # Train with cross validation
    (model, scoreOfFoldsBalanced, scoreOfFoldsUnbalanced) = trainWithCrossValidation(data, configuration)
    result = (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configuration)
    
    # Print results, save model
    printConfigurationResultSummary(result)
        
    # Save the model as a file and then clear the memory
    saveModel(model, result, configurationID, note)

    # Return result
    return result

## This function is defunct - check the implementation before using
#def crossValidateModelConfiguration(data, dataSpecification):
#    numConfigurations = getNumConfigurations()
#    skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
#    accuracyOfConfigurations = np.zeros(numConfigurations)
#    deviationOfConfigurations = np.zeros(numConfigurations)
#    nFolds = 10
#    configuration = 0
#    i = 0
#    note = 'NestedCrossValidation'
#    (x, y) = (data)
#    for trainIndex, testIndex in skf.split(x, y):
#        print("Running configuration", configuration, "/", numConfigurations)
#        
#        # Perform cross validation for this configuration, save results. Do not save the model due to memory limit issues.
#        (model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation((x[testIndex], y[testIndex]), configuration, nFolds)
#        accuracyOfConfigurations[i] = accuracyMean
#        deviationOfConfigurations[i] = accuracyStandardDeviation
#        
#        saveModel(model, configuration, accuracyMean, accuracyStandardDeviation, note)
#        model = None    # Clear up some memory
#        
#        print("Accuracy of configuration ", configuration, ": ", (accuracyMean * 100), " +/- ", (accuracyStandardDeviation * 100))
#        configuration = configuration + 1
#        i = i + 1
#    
#    return (accuracyOfConfigurations, deviationOfConfigurations)