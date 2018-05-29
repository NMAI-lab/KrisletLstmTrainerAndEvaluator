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
from sklearn.cross_validation import StratifiedKFold

# fix random seed for reproducibility
numpy.random.seed(7)
top_words = 5000
max_review_length = 500

# Load the data and preprocess
(x, y) = getData()

# Create the model
#model = defineModel(top_words, max_review_length)

n_folds = 10
skf = StratifiedKFold(y, n_folds=n_folds, shuffle=True)

for i, (train, test) in enumerate(skf):
    print("Running Fold", i+1, "/", n_folds)
    model = None # Clearing the NN.
    model = defineModel(top_words, max_review_length)
    
    trainModel(model, x[train], y[train])
    scores = model.evaluate(x[test], y[test], verbose=0)
    print("Accuracy: %.2f%%" % (scores[1]*100))