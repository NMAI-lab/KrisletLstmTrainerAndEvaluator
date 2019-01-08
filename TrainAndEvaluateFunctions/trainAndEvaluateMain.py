# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:02:37 2018

@author: patrickgavigan
"""

from constants import setSeeds
setSeeds()

from testRunFunctions import runTestCase
from configutationGenerator import buildConfigurationList, getMaxConfigCount

# List of test scenarios
testType = ["FiniteTurnKrislet", "StateBasedKickSpin", "StateBasedTurnDirection"] #"ClassicKrislet",  
#testType = ["sexpt_tests"]

# Set action list
actionIncludeList = ['turn+','turn-', 'dash', 'kick'] #['turn', 'dash', 'kick']

# Set feature list
# ga is short for goal adversary (where we don't want the ball to go)
# go is short for goal own (where we want the ball to go)
featureIncludeList = ['b','ga']#['b','go','ga']

configurations = list()

# List of model configurations with an LSTM layer
runDepthOptions = [120, 100, 75]
numLSTMnodeOptions = [120, 100, 75]
numHiddenNodeOptions = [50, 0]
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
                                             reduceLROptions,
                                             getMaxConfigCount(configurations)))

# List of model configurations with NO LSTM layer
runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [75, 50, 40]
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
                                             reduceLROptions,
                                             getMaxConfigCount(configurations)))
# Run all tests
for i in range(len(testType)):
    for j in range(len(configurations)):    # Skip nested cross validation, run individual tests
        currentConfig = list()
        currentConfig.append(configurations[j])
        runTestCase(testType[i], currentConfig, actionIncludeList, featureIncludeList)