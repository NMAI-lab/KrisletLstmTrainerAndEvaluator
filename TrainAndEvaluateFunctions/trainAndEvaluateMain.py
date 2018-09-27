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
testType = ["ClassicKrislet", "StateBasedKrislet", "FiniteTurnKrislet"]
#testType = ["sexpt_tests"]

configurations = list()

# List of model configurations with an LSTM layer
runDepthOptions = [100]
numLSTMnodeOptions = [100]
numHiddenNodeOptions = [100]
useConvolutionOptions = [False]#, True]
activationOptions = ['relu']#, 'sigmoid']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
configurations.extend(buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions, balanceOptions))

# List of model configurations with NO LSTM layer
runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [100]
useConvolutionOptions = [False]
activationOptions = ['relu']#, 'sigmoid']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
configurations.extend(buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions, balanceOptions))

# Run all tests
for i in range(len(testType)):
    runTestCase(testType[i], configurations)