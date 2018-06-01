# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:32:58 2018

@author: patrickgavigan
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
#from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

from sklearn.model_selection import StratifiedKFold

from dataManagement import stratefiedSplit

import numpy as np

# Create the model
def defineModel(configuration):
    # Need to get rid of these variables
    top_words = 5000
    max_review_length = 500
    
    embedding_vecor_length = 32
    model = Sequential()
    model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;

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

def trainWithCrossValidation(nFolds, x, y):
    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
    accuracyOfFolds = np.zeros(nFolds)
    foldNumber = 1
    i = 0
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Define and train the model
        configuration = 0
        model = defineAndTrainModel(x[trainIndex], y[trainIndex], configuration)
    
        # Test the model
        accuracy = evaluateModel(model, x[testIndex], y[testIndex])
        accuracyOfFolds[i] = accuracy
        print("Accuracy of fold ", foldNumber, ": ", (accuracy * 100))
        foldNumber = foldNumber + 1
        i = i + 1
        
    # Train the final model
    configuration = 0
    defineAndTrainModel(x, y, configuration)
    
    # Get performance estimations
    accuracyMean = np.mean(accuracyOfFolds)
    accuracyStandardDeviation = np.std(accuracyOfFolds)
    
    # Return results
    return (model, accuracyMean, accuracyStandardDeviation)