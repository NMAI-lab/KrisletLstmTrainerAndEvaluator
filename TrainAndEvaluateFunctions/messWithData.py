# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from csvLogFunctions import writeSingleResult
from configutationGenerator import buildConfigurationList

configurations = list()

testType = "FiniteTurnKrislet"

runDepthOptions = [0]
numLSTMnodeOptions = [0]
numHiddenNodeOptions = [100]
useConvolutionOptions = [False]
activationOptions = ['relu']
embeddingOptions = [False]
balanceOptions = ["randomUndersample"]#['None']
earlyStopOptions = [(0.01, 10)]#(earlyStopMinDelta, earlyStopPatience)
reduceLROptions = [(0.2, 5, 0.001)]#(ReduceLRfactor, ReduceLRpatience, ReduceLRmin_lr)
configurations.extend(buildConfigurationList(runDepthOptions,
                                             numLSTMnodeOptions,
                                             numHiddenNodeOptions,
                                             useConvolutionOptions,
                                             activationOptions,
                                             embeddingOptions,
                                             balanceOptions,
                                             earlyStopOptions,
                                             reduceLROptions))

result = ('Beans', 'Spam', configurations[0]);

#for i in range (len(configurations)):
writeSingleResult(testType, result);
