# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras import predict
from sklearn.model_selection import StratifiedKFold

from sklearn.metrics import recall_score, precision_score

import numpy as np

from dataManagement import stratefiedSplit, convertToCategorical, getDataSpecification, convertToClassID
from balancingFunctions import balanceData
from modelGenerators import defineModel, getNumConfigurations
from configurationGenerator import getBalanceOption
from evaluationMetrics import evaluateSpecificity

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
    # PErform balancing (if needed)
    balance = getBalanceOption(configuration)
    (x, y) = balanceData(data, balance)
    
    # Perform evaluation with keras (accuracy only)
    yCategorical = convertToCategorical(y)
    scores = model.evaluate(x, yCategorical, verbose = 0)
    accuracy = scores[1]
    
    # Calculate other metrics
    yPredicted = convertToClassID(predict(model, x))
    labels = [i for i in range(min(y),max(y))]
    precision = precision_score(y, yPredicted, labels, average = None)
    sensitivity = recall_score(y, yPredicted, labels, average = None)
    specificity = evaluateSpecificity(y, yPredicted, labels) 
    
    # Return results
    return (accuracy, precision, sensitivity, specificity)

def evaluateCustomMetrics(data):
    scores = 1
    return scores

def trainWithCrossValidation(nFolds, data, configuration):
    
    # Get the data specifications
    dataSpecification = getDataSpecification(data)

    # Extract data
    (x, y) = (data)
    
    # Setup the folds
    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
    scoreOfFolds = np.zeros(nFolds)
    foldNumber = 1
    i = 0
    
    # Cross validation loop
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Define and train the model
        model = defineAndTrainModel((x[trainIndex], y[trainIndex]), configuration, dataSpecification)
    
        # Test the model
        scoreOfFolds[i] = evaluateModel(model, (x[testIndex], y[testIndex]))
        #printScore(scoreOfFolds[i])
        #print("Accuracy of fold ", foldNumber, ": ", (accuracy * 100))
        foldNumber = foldNumber + 1
        i = i + 1
        
    # Train the final model
    model = defineAndTrainModel((x, y), configuration, dataSpecification)
    
    # Get performance estimations
    #accuracyMean = np.mean(accuracyOfFolds)
    #accuracyStandardDeviation = np.std(accuracyOfFolds)
    
    # Return results
    return (model, scoreOfFolds)


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