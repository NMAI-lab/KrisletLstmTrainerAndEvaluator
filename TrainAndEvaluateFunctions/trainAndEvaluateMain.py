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

# fix random seed for reproducibility
#seed = 42;
#numpy.random.seed(seed)

# Load the data and preprocess
(x, y) = getData()

# Create the model
#model = defineModel(top_words, max_review_length)

# Train network and evaluate with cross-validation
nFolds = 3
trainWithCrossValidation(nFolds, x, y)