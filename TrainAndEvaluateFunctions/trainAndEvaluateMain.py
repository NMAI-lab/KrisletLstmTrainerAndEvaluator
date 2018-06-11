# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:18:48 2018

@author: patrickgavigan

Tutorial from: 
https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/

"""

# LSTM and CNN for sequence classification in the IMDB dataset
#import numpy

from dataManagement import getData
from modelFunctions import trainWithCrossValidation, crossValidateModelConfiguration
from modelFunctions import evaluateModel
from modelGenerators import getNumConfigurations

# fix random seed for reproducibility
#seed = 42;
#numpy.random.seed(seed)

# Load the data and preprocess
(xTrain, yTrain), (xTest, yTest), (x, y) = getData()

# Train network and evaluate with cross-validation
nFolds = 10
configuration = 0
(model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, xTrain, yTrain, configuration)

# Evaluate with hold out sample for sanity check
holdOutAccuracy = evaluateModel(model, xTest, yTest)
model = None    # Clear up some memory

# Train network and evaluate with cross-validation, ignore model parameter that is returned
#nFolds = 10
(_, accuracyMeanFullData, accuracyStandardDeviationFullData) = trainWithCrossValidation(nFolds, x, y, configuration)

# Perform nested cross validation for parameter tuning and model evaluation
(accuracyOfConfigurations, deviationOfConfigurations) = crossValidateModelConfiguration(x, y)

# Print summary
print('Cross validation accuracy mean: ', accuracyMean)
print('Cross validation accuracy standard deviation ', accuracyStandardDeviation)
print('Hold out accuracy: ', holdOutAccuracy)
print('Full data cross validation accuracy mean: ', accuracyMeanFullData)
print('Full data cross validation accuracy standard deviation ', accuracyStandardDeviationFullData)

numConfigurations = getNumConfigurations()
for i in range(numConfigurations):
    print('Configuration ', i, " Accuracy : ", accuracyOfConfigurations[i], " +/- ", deviationOfConfigurations[i])
