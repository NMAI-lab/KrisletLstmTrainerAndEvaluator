# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:02:37 2018

@author: patrickgavigan
"""

from constants import setSeeds
setSeeds()

from testRunFunctions import runTestCase
from configutationGenerator import buildConfigurationList

# List of test scenarios
testType = ["classicKrislet-sexp"]#, "stateBasedKrislet-sexp"]

configurations = list()

# List of model configurations with an LSTM layer
#runDepthOptions = [50]
#numLSTMnodeOptions = [50]
#numHiddenNodeOptions = [0]
#useConvolutionOptions = [False]#, True]
#activationOptions = ['relu']#, 'sigmoid']
#embeddingOptions = [False]
#balanceOptions = ['None']#["randomUndersample"]
#configurations.extend(buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions, balanceOptions))

# List of model configurations with NO LSTM layer
runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [10]
useConvolutionOptions = [False]
activationOptions = ['relu']#, 'sigmoid']
embeddingOptions = [False]
balanceOptions = ['None']#["randomUndersample"]
configurations.extend(buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions, balanceOptions))

# Run all tests
for i in range(len(testType)):
    runTestCase(testType[i], configurations)