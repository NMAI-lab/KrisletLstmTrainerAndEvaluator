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
from keras.layers.embeddings import Embedding
#from keras.preprocessing import sequence

def defineParameterizedModel(configuration, dataSpecification):
    (_, numLSTMnodes, numHiddenNodes, useConvolution, activation) = configuration
    (numCategories, _, _) = dataSpecification

    # Setup the model
    model = Sequential()

    # Add the convolution layer
    if useConvolution:
        model.add(Conv1D(filters=32, kernel_size=3, padding = 'same', activation = activation))
        model.add(MaxPooling1D(pool_size=2))
    
    # Add the LSTM layer
    if numLSTMnodes > 0:
        model.add(LSTM(numLSTMnodes))
      
    # Add hidden fully connected layer
    if numHiddenNodes > 0:
        model.add(Dense(numHiddenNodes, activation = activation))
    
    # Add final layer, compile and return
    model.add(Dense(numCategories, activation = 'softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;






# Create the model
def defineModel(configuration, dataSpecification):
    
    # Return the requested version of the model
    if configuration == 0:
        return defineModelVersion0(dataSpecification)
    elif configuration == 1:
        return defineModelVersion1(dataSpecification)
    elif configuration == 2:
        return defineModelVersion2(dataSpecification)
    
    # Default, configuration 0
    else:
        return defineModelVersion0(dataSpecification)

def getNumConfigurations():
    return 3

def defineModelVersion2(dataSpecification):
    (numCategories, elementDimension, sequenceLength) = dataSpecification
    model = Sequential()

    # vvv Remove from final
    top_words = 5000
    embedding_vecor_length = 32
    model.add(Embedding(top_words, embedding_vecor_length, input_length = sequenceLength))
    # ^^^ Remove from final

    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(100))
    model.add(Dense(numCategories, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;

def defineModelVersion1(dataSpecification):
    (numCategories, elementDimension, sequenceLength) = dataSpecification
    model = Sequential()

    # vvv Remove from final
    top_words = 5000
    embedding_vecor_length = 32
    model.add(Embedding(top_words, embedding_vecor_length, input_length = sequenceLength))
    # ^^^ Remove from final

    model.add(LSTM(100))
    model.add(Dense(numCategories, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;

def defineModelVersion0(dataSpecification):
    (numCategories, elementDimension, sequenceLength) = dataSpecification
    model = Sequential()

    # vvv Remove from final
    top_words = 5000
    embedding_vecor_length = 32
    model.add(Embedding(top_words, embedding_vecor_length, input_length = sequenceLength))
    # ^^^ Remove from final

    model.add(LSTM(100))
    model.add(Dense(50, activation='sigmoid'))
    model.add(Dense(numCategories, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model;