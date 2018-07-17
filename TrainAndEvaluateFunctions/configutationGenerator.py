# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:18:04 2018

@author: patrickgavigan
"""

# Returns a list of tuples. Tuple format: (runDepthOptions, numLSTMnodeOptions,
# numHiddenNodeOptions, useConvolutionOptions, activationOptions, 
# embeddingOptions)
def buildConfigurationList(runDepthOptions, numLSTMnodeOptions, numHiddenNodeOptions, useConvolutionOptions, activationOptions, embeddingOptions):
    configList = list()
    for i in range(len(runDepthOptions)):
        for j in range(len(numLSTMnodeOptions)):
            for k in range(len(numHiddenNodeOptions)):
                for l in range(len(useConvolutionOptions)):
                    for m in range(len(activationOptions)):
                        for n in range(len(embeddingOptions)):
                            configList.append((runDepthOptions[i], numLSTMnodeOptions[j], numHiddenNodeOptions[k], useConvolutionOptions[l], activationOptions[m], embeddingOptions[n]))
    return configList

def getMaxDepth(configurations):
    maxDepth = max(configurations[0])
    
    # Cropper doesn't work properly if the depth is less than 2. This helps
    # prevent a known issue from occuring.
    if maxDepth < 2:
        maxDepth = 2
    
    return maxDepth