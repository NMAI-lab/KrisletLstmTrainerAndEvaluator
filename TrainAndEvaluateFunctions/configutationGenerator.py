# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:18:04 2018

@author: patrickgavigan
"""

# Returns a list of tuples.
def buildConfigurationList(runDepthOptions,
                           numLSTMnodeOptions,
                           numHiddenNodeOptions,
                           useConvolutionOptions,
                           activationOptions,
                           embeddingOptions,
                           balanceOptions,
                           earlyStopOptions,
                           reduceLROptions):
    configList = list()
    configCount = 0;
    for i in range(len(runDepthOptions)):
        for j in range(len(numLSTMnodeOptions)):
            for k in range(len(numHiddenNodeOptions)):
                for l in range(len(useConvolutionOptions)):
                    for m in range(len(activationOptions)):
                        for n in range(len(embeddingOptions)):
                            for o in range(len(balanceOptions)):
                                for p in range(len(earlyStopOptions)):
                                    for q in range(len(reduceLROptions)):
                                        configList.append((runDepthOptions[i], 
                                                           numLSTMnodeOptions[j], 
                                                           numHiddenNodeOptions[k], 
                                                           useConvolutionOptions[l], 
                                                           activationOptions[m], 
                                                           embeddingOptions[n], 
                                                           balanceOptions[o],
                                                           earlyStopOptions[p],
                                                           reduceLROptions[q],
                                                           configCount))
                                        configCount = configCount + 1;
    return configList


def getMaxDepth(configurations):

    # Get the number of configurations in the list
    numConfigurations = len(configurations)
    
    # Cropper doesn't work properly if the depth is less than 2. This helps
    # prevent a known issue from occuring.
    maxDepth = 2
    
    # Index of the configuration touple for the depth
    depthIndex = 0

    # Check all configurations to find the largest depth    
    for i in range(numConfigurations):
        currentConfiguration = configurations[i]
        currentDepth = currentConfiguration[depthIndex]
        if currentDepth > maxDepth:
            maxDepth = currentDepth
    
    # Return result
    return maxDepth

def getBalanceOption(configuration):
    (_, _, _, _, _, _, balanceOption) = configuration
    return balanceOption