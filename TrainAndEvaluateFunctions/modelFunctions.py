# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import StratifiedKFold
import numpy as np

from dataManagement import stratefiedSplit
from modelGenerators import defineModelVersion0, defineModelVersion1, defineModelVersion2, getNumConfigurations

# Create the model
def defineModel(configuration):
    
    # Return the requested version of the model
    if configuration == 0:
        return defineModelVersion0()
    elif configuration == 1:
        return defineModelVersion1()
    elif configuration == 2:
        return defineModelVersion2()
    
    # Default, configuration 0
    else:
        return defineModelVersion0()

# Train the model
def trainModel(model, x, y):
    (xTrain, yTrain), (xTest, yTest) = stratefiedSplit(x, y)
    callbacksList = configureCallBacks()
    model.fit(xTrain, yTrain, epochs = 10, batch_size = 64, callbacks = callbacksList, validation_data = (xTest, yTest))
    return model

# Define and train the model (useful for cross-validation)
def defineAndTrainModel(x, y, configuration):
    # Define the model
    model = defineModel(configuration)
    
    # Train the model
    model = trainModel(model, x, y)
    
    # Return the model
    return model

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
    

def evaluateModel(model, x, y):
    scores = model.evaluate(x, y, verbose=0)
    return scores[1]

def trainWithCrossValidation(nFolds, x, y, configuration):
    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
    accuracyOfFolds = np.zeros(nFolds)
    foldNumber = 1
    i = 0
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Define and train the model
        model = defineAndTrainModel(x[trainIndex], y[trainIndex], configuration)
    
        # Test the model
        accuracy = evaluateModel(model, x[testIndex], y[testIndex])
        accuracyOfFolds[i] = accuracy
        print("Accuracy of fold ", foldNumber, ": ", (accuracy * 100))
        foldNumber = foldNumber + 1
        i = i + 1
        
    # Train the final model
    defineAndTrainModel(x, y, configuration)
    
    # Get performance estimations
    accuracyMean = np.mean(accuracyOfFolds)
    accuracyStandardDeviation = np.std(accuracyOfFolds)
    
    # Return results
    return (model, accuracyMean, accuracyStandardDeviation)

def crossValidateModelConfiguration(x, y):
    numConfigurations = getNumConfigurations()
    skf = StratifiedKFold(n_splits = numConfigurations)#, shuffle = True, random_state = seed)
    accuracyOfConfigurations = np.zeros(numConfigurations)
    deviationOfConfigurations = np.zeros(numConfigurations)
    nFolds = 10
    configuration = 0
    i = 0
    for trainIndex, testIndex in skf.split(x, y):
        print("Running configuration", configuration, "/", numConfigurations)
        
        # Perform cross validation for this configuration, save results. Do not save the model due to memory limit issues.
        (_, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, x, y, configuration)
        accuracyOfConfigurations[i] = accuracyMean
        deviationOfConfigurations[i] = accuracyStandardDeviation
        
        print("Accuracy of configuration ", configuration, ": ", (accuracyMean * 100), " +/- ", (accuracyStandardDeviation * 100))
        configuration = configuration + 1
        i = i + 1
    
    return (accuracyOfConfigurations, deviationOfConfigurations)

def saveModel(model, configuration):
    filename = 'my_model.h5'
    model.save(filename)  # creates a HDF5 file 'my_model.h5'