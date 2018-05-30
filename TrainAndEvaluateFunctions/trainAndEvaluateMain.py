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
from modelFunctions import trainWithCrossValidation
from modelFunctions import evaluateModel

# fix random seed for reproducibility
#seed = 42;
#numpy.random.seed(seed)

# Load the data and preprocess
(xTrain, yTrain), (xTest, yTest), (x, y) = getData()

# Train network and evaluate with cross-validation
nFolds = 10
(model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, xTrain, yTrain)

# Evaluate with hold out sample for sanity check
holdOutAccuracy = evaluateModel(model, xTest, yTest)

# Train network and evaluate with cross-validation
nFolds = 10
(model, accuracyMeanFullData, accuracyStandardDeviationFullData) = trainWithCrossValidation(nFolds, x, y)

# Print summary
print('Cross validation accuracy mean: ', accuracyMean)
print('Cross validation accuracy standard deviation ', accuracyStandardDeviation)
print('Hold out accuracy: ', holdOutAccuracy)
print('Full data cross validation accuracy mean: ', accuracyMeanFullData)
print('Full data cross validation accuracy standard deviation ', accuracyStandardDeviationFullData)