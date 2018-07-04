# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:18:04 2018

@author: patrickgavigan
"""

def buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions):
    configList = list()
    for i in range(len(runDepthOptions)):
        for j in range(len(numLSTMnodeOptions)):
            for k in range(len(numHiddenNodeOptions)):
                for l in range(len(useConvolutionOptions)):
                    for m in range(len(activationOptions)):
                        configList.append(setConfiguration(runDepthOptions[i], numLSTMnodeOptions[j], numHiddenNodeOptions[k], useConvolutionOptions[l], activationOptions[m]))
    return configList

# Build the touple with configuration parameters
def setConfiguration(runDepth, numLSTMnodes, numHiddenNodes, useConvolution, activation):
    return (runDepth, numLSTMnodes, numHiddenNodes, useConvolution, activation)