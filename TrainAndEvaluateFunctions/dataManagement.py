# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:35:58 2018

@author: patrickgavigan
"""

import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence

def getData():

    # This function needs to be reimplemented for the Krislet logs. For now,
    # it's a hack based on a tutorial. Currently, combining the imdb data
    # training and testing data into a single data set in order to have a
    # sample data set for testing nexted cross-validation functionality in 
    # other parts of this program.

    
    # Need to get rid of these variables
    top_words = 5000
    max_review_length = 500
        
    # Load the dataset but only keep the top n words, zero the rest
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)

    # Truncate and pad input sequences
    X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
    X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

    # Concatenate the data
    x = np.concatenate((X_train, X_test), axis=0)
    y = np.concatenate((y_train, y_test), axis=0)

    # Return result
    return (x, y)