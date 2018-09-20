# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.metrics import recall_score, precision_score, f1_score

from dataManagement import stratefiedSplit, convertToCategorical, convertToClassID, getDataSpecification
from balancingFunctions import balanceData
from configutationGenerator import getBalanceOption
from modelGenerators import defineParameterizedModel
from evaluationMetrics import evaluateSpecificity

# Train the model
def trainModel(model, data, balanceOption = None):

    # Check data balance, balance if needed
    (x, y) = balanceData(data, balanceOption)
        
    # Perform stratefied split
    (xTrain, yTrain), (xTest, yTest) = stratefiedSplit(x, y)
    
    # Configure callbacks
    callbacksList = configureCallBacks()
    
    # Convert y data to categorical
    yTrainCategorical = convertToCategorical(yTrain)
    yTestCategorical = convertToCategorical(yTest)
    
    # Fit the model and return
    model.fit(xTrain, yTrainCategorical, epochs = 10, batch_size = 64, callbacks = callbacksList, validation_data = (xTest, yTestCategorical))
    return model

# Define and train the model (useful for cross-validation)
def defineAndTrainModel(data, configuration):#, dataSpecification):
    dataSpecification = getDataSpecification(data)          # Get the data specifications
    model = defineParameterizedModel(configuration, dataSpecification)   # Define the model
    balanceOption = getBalanceOption(configuration)
    model = trainModel(model, data, balanceOption)          # Train the model
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
    

def evaluateModel(model, data, balanceOption):
    # Perform balancing (if needed)
    (x, y) = balanceData(data, balanceOption)
    
    # Perform evaluation with keras (accuracy only)
    yCategorical = convertToCategorical(y)
    scores = model.evaluate(x, yCategorical, verbose = 0)
    accuracy = scores[1]
    
    # Calculate other metrics
    yPredicted = convertToClassID(model.predict(x))
    minLabel = int(min(y))
    maxLabel = int(max(y)) + 1
    labels = [i for i in range(minLabel,maxLabel)]
    precision = precision_score(y, yPredicted, labels = labels, average = None)
    sensitivity = recall_score(y, yPredicted, labels = labels, average = None)
    specificity = evaluateSpecificity(y, yPredicted, labels) 
    fMeasure = f1_score(y, yPredicted, labels = labels, average = None)
    
    # Return results
    return (accuracy, precision, sensitivity, specificity, fMeasure)