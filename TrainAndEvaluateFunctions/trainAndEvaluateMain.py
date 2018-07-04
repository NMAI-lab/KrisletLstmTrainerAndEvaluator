# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:02:37 2018

@author: patrickgavigan
"""

from testRunFunctions import runTestCase
from configurationGenerator import buildConfigurationList

# List of test scenarios
testType = ["stateBasedKrislet", "ClassicKrislet"]

# List of model configurations with an LSTM layer
runDepthOptions = [10, 50, 100, 500, 1000]
numLSTMnodeOptions = [10, 50, 100, 500, 1000]
numHiddenNodeOptions = [0, 10, 20, 30]
useConvolutionOptions = [True, False]
activationOptions = ['relu', 'sigmoid']
embeddingOptions = [False]
configurations = buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions)

# List of model configurations with NO LSTM layer
runDepthOptions = [1]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [10, 20, 30]
useConvolutionOptions = [False]
activationOptions = ['relu', 'sigmoid']
embeddingOptions = [False]
baselineConfigurations = buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions)

# Include baseline options in configurations to test
configurations.extend(baselineConfigurations)

# Run all tests
for i in range(len(testType)):
    runTestCase(testType[i], configurations)