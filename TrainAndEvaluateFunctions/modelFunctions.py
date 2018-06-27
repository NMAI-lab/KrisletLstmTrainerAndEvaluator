# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import StratifiedKFold
import numpy as np
import datetime

from dataManagement import stratefiedSplit, convertToCategorical
from modelGenerators import defineModel, getNumConfigurations

# Train the model
def trainModel(model, data):
    (x, y) = data
    (xTrain, yTrain), (xTest, yTest) = stratefiedSplit(x, y)
    callbacksList = configureCallBacks()
    yTrainCategorical = convertToCategorical(yTrain)
    yTestCategorical = convertToCategorical(yTest)
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
    

def evaluateModel(model, data):
    (x, y) = data
    yCategorical = convertToCategorical(y)
    scores = model.evaluate(x, yCategorical, verbose = 0)
    return scores[1]

def trainWithCrossValidation(nFolds, data, configuration, dataSpecification):
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
    defineAndTrainModel((x, y), configuration, dataSpecification)
    
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

def saveModel(model, configuration, accuracy, deviation, note = None):
    fileName = getModelFileName(configuration, accuracy, deviation, note)
    model.save(fileName)  # creates a HDF5 file 'my_model.h5'

def getModelFileName(configuration, accuracy, deviation, note = None):
    fileExtension = '.h5'
    fileNameSuffix = 'Configuration' + str(configuration) + 'Accuracy' + str(accuracy) + 'Deviation' + str(deviation)
    
    if note != None:
        fileNameSuffix = fileNameSuffix + str(note)
    fileNameSuffix = fileNameSuffix + fileExtension
    
    fileName = timeStamped(fileNameSuffix)
    return fileName  

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)