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
from modelFunctions import trainWithCrossValidation, crossValidateModelConfiguration, saveModel
from modelFunctions import evaluateModel
from modelGenerators import getNumConfigurations

# fix random seed for reproducibility
#seed = 42;
#numpy.random.seed(seed)

# Load the data and preprocess
trainData, testData, fullData, dataSpecification = getData()

# Perform nested cross validation for parameter tuning and model evaluation. Saves models within function
print('Run 1: Train using nested cross validation')
(accuracyOfConfigurations, deviationOfConfigurations) = crossValidateModelConfiguration(fullData, dataSpecification)

print('Run 1 Summary')
numConfigurations = getNumConfigurations()
for i in range(numConfigurations):
    print('Configuration ', i, " Accuracy : ", accuracyOfConfigurations[i], " +/- ", deviationOfConfigurations[i])
print('*****')

# Train network and evaluate with cross-validation
print('Run 2: Train using cross validation and hold out')
nFolds = 10
configuration = 0
(model, accuracyMean, accuracyStandardDeviation) = trainWithCrossValidation(nFolds, trainData, configuration, dataSpecification)

# Evaluate with hold out sample for sanity check
holdOutAccuracy = evaluateModel(model, testData)
note = 'VanillaCrossValidationWithHoldOutAccuracy' + str(holdOutAccuracy)
saveModel(model, configuration, accuracyMean, accuracyStandardDeviation, note)
model = None    # Clear up some memory

print('Run 2 Summary')
print('Cross validation accuracy mean: ', accuracyMean)
print('Cross validation accuracy standard deviation ', accuracyStandardDeviation)
print('Hold out accuracy: ', holdOutAccuracy)
print('*****')

# Train network and evaluate with cross-validation
print('Run 3: Train using cross validation')
(model, accuracyMeanFullData, accuracyStandardDeviationFullData) = trainWithCrossValidation(nFolds, fullData, configuration, dataSpecification)
note = 'CrossValidationWithFullData'
saveModel(model, configuration, accuracyMeanFullData, accuracyStandardDeviationFullData, note)
model = None    # Clear up some memory

print('Run 3 Summary')
print('Full data cross validation accuracy mean: ', accuracyMeanFullData)
print('Full data cross validation accuracy standard deviation ', accuracyStandardDeviationFullData)
print('*****')

# Print summary
print('Full Summary')
print('Cross validation accuracy mean: ', accuracyMean)
print('Cross validation accuracy standard deviation ', accuracyStandardDeviation)
print('Hold out accuracy: ', holdOutAccuracy)
print('Full data cross validation accuracy mean: ', accuracyMeanFullData)
print('Full data cross validation accuracy standard deviation ', accuracyStandardDeviationFullData)

numConfigurations = getNumConfigurations()
for i in range(numConfigurations):
    print('Configuration ', i, " Accuracy : ", accuracyOfConfigurations[i], " +/- ", deviationOfConfigurations[i])
