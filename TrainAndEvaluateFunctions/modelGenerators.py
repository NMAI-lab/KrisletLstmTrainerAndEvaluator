# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:13:14 2018

@author: patrickgavigan
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
#from keras.layers.embeddings import Embedding
#from keras.preprocessing import sequence


def defineParameterizedModel(configuration, dataSpecification):
    # Unpack the parameters
    (_, numLSTMnodes, numHiddenNodes, useConvolution, activation, useEmbedding, _) = configuration
    (numCategories, elementDimension, sequenceLength) = dataSpecification

    # Setup the model
    model = Sequential()
    firstLayer = True
    if sequenceLength == 0:
        inputShapeParameter = (elementDimension,)
    else:
        inputShapeParameter = (sequenceLength, elementDimension)

    # Add embedding layer
#    if useEmbedding:
#        model.add(Embedding(input_dim, output_dim))
#        firstLayer = False

    # Add the convolution layer
    if useConvolution:
        if firstLayer:
            model.add(Conv1D(filters=32, kernel_size=3, padding = 'same', activation = activation, input_shape = inputShapeParameter))
            firstLayer = False
        else:
            model.add(Conv1D(filters=32, kernel_size=3, padding = 'same', activation = activation))
        model.add(MaxPooling1D(pool_size=2))
        firstLayer = False
    
    # Add the LSTM layer
    if numLSTMnodes > 0:
        if firstLayer:
            model.add(LSTM(numLSTMnodes, input_shape = inputShapeParameter))
            firstLayer = False
        else:
            model.add(LSTM(numLSTMnodes))
      
    # Add hidden fully connected layer
    if numHiddenNodes > 0:
        if firstLayer:
            model.add(Dense(inputShapeParameter[0], activation = activation, input_shape = inputShapeParameter))
            model.add(Dense(numHiddenNodes, activation = activation))
            firstLayer = False
        else:
            model.add(Dense(numHiddenNodes, activation = activation))
    
    # Add final layer, compile and return
    model.add(Dense(numCategories, activation = 'softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;
