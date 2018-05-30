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

from sklearn.model_selection import StratifiedKFold

# Create the model
def defineModel(top_words, max_review_length):
    embedding_vecor_length = 32
    model = Sequential()
    model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;

def trainModel(model, x, y):
    model.fit(x, y, epochs = 3, batch_size = 64)
    return model

def evaluateModel(model, x, y):
    scores = model.evaluate(x, y, verbose=0)
    return scores[1]

def trainWithCrossValidation(nFolds, x, y):
    # Need to get rid of these variables
    top_words = 5000
    max_review_length = 500

    skf = StratifiedKFold(n_splits = nFolds)#, shuffle = True, random_state = seed)
    foldNumber = 1;
    for trainIndex, testIndex in skf.split(x, y):
        print("Running Fold", foldNumber, "/", nFolds)

        # Build the model
        model = None # Clearing the NN.
        model = defineModel(top_words, max_review_length)
    
        # Train the model
        trainModel(model, x[trainIndex], y[trainIndex])
    
        # Test the model
        accuracy = evaluateModel(model, x, y)
        print("Accuracy of fold ", foldNumber, ": ", (accuracy*100))
        foldNumber = foldNumber + 1