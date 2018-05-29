# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:18:48 2018

@author: patrickgavigan

Tutorial from: 
https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/

"""

# LSTM and CNN for sequence classification in the IMDB dataset
import numpy

from dataManagement import getData
from modelFunctions import defineModel, trainModel
from sklearn.model_selection import StratifiedKFold

# fix random seed for reproducibility
seed = 42;
numpy.random.seed(seed)
top_words = 5000
max_review_length = 500

# Load the data and preprocess
(x, y) = getData()

# Create the model
#model = defineModel(top_words, max_review_length)

nFolds = 3
skf = StratifiedKFold(n_splits = nFolds, shuffle = True, random_state = seed)

foldNumber = 1;
for trainIndex, testIndex in skf.split(x, y):
    print("Running Fold", foldNumber, "/", nFolds)

    # Build the model
    model = None # Clearing the NN.
    model = defineModel(top_words, max_review_length)
    
    # Train the model
    trainModel(model, x[trainIndex], y[trainIndex])
    
    # Test the model
    scores = model.evaluate(x[testIndex], y[testIndex], verbose=0)
    print("Accuracy of fold ", foldNumber, ": ", (scores[1]*100))
    foldNumber = foldNumber + 1