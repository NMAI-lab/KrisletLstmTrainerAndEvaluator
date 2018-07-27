# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:59:50 2018

@author: patrickgavigan
"""

def printConfigurationParameters(configuration):
    (runDepthOption, numLSTMnodeOption, numHiddenNodeOption, useConvolutionOption, activationOption, embeddingOption, balanceOption) = configuration
    print("Configuration parameters")
    print("Run depth: ", runDepthOption)
    print("Number of LSTM nodes: ", numLSTMnodeOption)
    print("Number of hidden nodes: ", numHiddenNodeOption)
    print("Using convolution: ", useConvolutionOption)
    print("Activation option: ", activationOption)
    print("Using embedding layer: ",  embeddingOption)
    print("Balance option: ",  balanceOption)
    return

def printSingleResult(result, fold):
    (accuracy, precision, sensitivity, specificity) = result
    print("Fold ", fold)
    print("Accuracy: ", accuracy)
    print(" Precision: ", precision)
    print(" Sensitivity: ", sensitivity)
    print("Specificity: ", specificity)
    return

def printConfigurationResultSummary(result):
    (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configuration) = result
    print("Summary of configuration")
    printConfigurationParameters(configuration)
    
    print("Balanced results")
    for i in range(len(scoreOfFoldsBalanced)):
        printSingleResult(scoreOfFoldsBalanced[i], i)
    
    print("Unbalanced results")
    for i in range(len(scoreOfFoldsUnbalanced)):
        printSingleResult(scoreOfFoldsUnbalanced[i], i)
        
    # Need to print summary statistics of each parameter    
    
    return

# Print a summary of the test run
def printResultSummary(testType, results, configurations): 
    scoreOfFoldsBalanced, scoreOfFoldsUnbalanced = results
    print('--------------------------------')
    print('Summary of ' + testType + ' test')

    for i in range(len(configurations)):
        print('Configuration ', i)
        printConfigurationResultSummary(scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configurations[i])
    print('--------------------------------')