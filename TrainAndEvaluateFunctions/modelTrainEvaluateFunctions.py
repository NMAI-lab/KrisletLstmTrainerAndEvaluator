# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import StratifiedKFold
import numpy as np

from dataManagement import stratefiedSplit, convertToCategorical, getDataSpecification
from balancingFunctions import balanceData
from modelGenerators import defineModel, getNumConfigurations
from configurationGenerator import getBalanceOption

from modelSave import saveModel

# Train the model
def trainModel(model, data):

    # Check data balance, balance if needed
    (x, y) = balanceData(data)
        
    # Perform stratefied split
    (xTrain, yTrain), (xTest, yTest) = stratefiedSplit(x, y)
    
    # Configure callbacks
    callbacksList = configureCallBacks()
    
    # COnvert y data to categorical
    yTrainCategorical = convertToCategorical(yTrain)
    yTestCategorical = convertToCategorical(yTest)
    
    # Fit the model and return
    model.fit(xTrain, yTrainCategorical, epochs = 10, batch_size = 64, callbacks = callbacksList, validation_data = (xTest, yTestCategorical))
    return model

# Define and train the model (useful for cross-validation)
def defineAndTrainModel(data, configuration, dataSpecification):
    model = defineModel(configuration, dataSpecification)   # Define the model
    model = trainModel(model, data)                         # Train the model
    return model                                            # Return the model

def configureCallBacks():
    verbosity = 1
    stopper = EarlyStopping(monitor = 'loss',
                            min_delta = 0.01,
                            patience = 10,
                            verbose = verbosity,
                            mode = 'auto')
    
    rateReducer = ReduceLROnPlateau(monitor = 'loss', 
                                    factor = 0.2, 
                                    patience = 5, 
                                    verbose = verbosity, 
                                    min_lr = 0.001)
       
    callbacksList = [stopper, rateReducer]
    return callbacksList
    

def evaluateModel(model, data, configuration):
    balance = getBalanceOption(configuration)
    (x, y) = balanceData(data, balance)
    yCategorical = convertToCategorical(y)
    scores = model.evaluate(x, yCategorical, verbose = 0)
    return scores[1]
def trainWithCrossValidation(nFolds, data, configuration):
    
    # Get the data specifications
    dataSpecification = getDataSpecification(data)

    # Extract data
    (x, y) = (data)
    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
    accuracyOfFolds = np.zeros(nFolds)
    foldNumber = 1
    i = 0
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Define and train the model
        model = defineAndTrainModel((x[trainIndex], y[trainIndex]), configuration, dataSpecification)
    
        # Test the model
        accuracy = evaluateModel(model, (x[testIndex], y[testIndex]))
        accuracyOfFolds[i] = accuracy
        print("Accuracy of fold ", foldNumber, ": ", (accuracy * 100))
        foldNumber = foldNumber + 1
        i = i + 1
        
    # Train the final model
    model = defineAndTrainModel((x, y), configuration, dataSpecification)
    
    # Get performance estimations
    accuracyMean = np.mean(accuracyOfFolds)
    accuracyStandardDeviation = np.std(accuracyOfFolds)
    
    # Return results
    return (model, accuracyMean, accuracyStandardDeviation)


def crossValidateModelConfiguration(data, dataSpecification):
    numConfigurations = getNumConfigurations()
    skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
    accuracyOfConfigurations = np.zeros(numConfigurations)
    deviationOfConfigurations = np.zeros(numConfigurations)
    nFolds = 10
    configuration = 0
    i = 0
    note = 'NestedCrossValidation'
    (x, y) = (data)
    for trainIndex, testIndex in skf.split(x, y):
        print("Running configuration", configuration, "/", numConfigurations)
        
        # Perform cross validation for this configuration, save results. Do not save the model due to memory limit issues.
        (model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, (x[testIndex], y[testIndex]), configuration, dataSpecification)
        accuracyOfConfigurations[i] = accuracyMean
        deviationOfConfigurations[i] = accuracyStandardDeviation
        
        saveModel(model, configuration, accuracyMean, accuracyStandardDeviation, note)
        model = None    # Clear up some memory
        
        print("Accuracy of configuration ", configuration, ": ", (accuracyMean * 100), " +/- ", (accuracyStandardDeviation * 100))
        configuration = configuration + 1
        i = i + 1
    
    return (accuracyOfConfigurations, deviationOfConfigurations)