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
testType = ["FiniteTurnKrislet", "StateBasedKrislet"] #"ClassicKrislet",  
#testType = ["sexpt_tests"]

configurations = list()

# List of model configurations with an LSTM layer
runDepthOptions = [100]#, 50, 40]
numLSTMnodeOptions = [100]#, 50, 40]
numHiddenNodeOptions = [100]#, 50, 10, 0]
useConvolutionOptions = [False]
activationOptions = ['relu']#, 'sigmoid']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
trainOptions = [(10, 64)]
earlyStopOptions = [(0.01, 10)]#(earlyStopMinDelta, earlyStopPatience)
reduceLROptions = [(0.2, 5, 0.001)]#(ReduceLRfactor, ReduceLRpatience, ReduceLRmin_lr)
configurations.extend(buildConfigurationList(runDepthOptions,
                                             numLSTMnodeOptions,
                                             numHiddenNodeOptions, 
                                             useConvolutionOptions,
                                             activationOptions, 
                                             embeddingOptions,
                                             balanceOptions,
                                             trainOptions,
                                             earlyStopOptions,
                                             reduceLROptions))

# List of model configurations with NO LSTM layer
runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [100]#, 50, 10]
useConvolutionOptions = [False]
activationOptions = ['relu']#, 'sigmoid']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
trainOptions = [(10, 64)]
earlyStopOptions = [(0.01, 10)]#(earlyStopMinDelta, earlyStopPatience)
reduceLROptions = [(0.2, 5, 0.001)]#(ReduceLRfactor, ReduceLRpatience, ReduceLRmin_lr)
configurations.extend(buildConfigurationList(runDepthOptions,
                                             numLSTMnodeOptions,
                                             numHiddenNodeOptions, 
                                             useConvolutionOptions,
                                             activationOptions, 
                                             embeddingOptions,
                                             balanceOptions, 
                                             trainOptions,
                                             earlyStopOptions,
                                             reduceLROptions))
# Run all tests
for i in range(len(testType)):
    for j in range(len(configurations)):    # Skip nested cross validation, run individual tests
        currentConfig = list()
        currentConfig.append(configurations[j])
        runTestCase(testType[i], currentConfig)