# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:59:50 2018

@author: patrickgavigan
"""

from evaluationMetrics import getSummaryStatistics

def printConfigurationParameters(configuration):
    (runDepthOption, numLSTMnodeOption, numHiddenNodeOption, useConvolutionOption, activationOption, embeddingOption, balanceOption) = configuration
    print("Configuration parameters")
    print(" Run depth: ", runDepthOption)
    print(" Number of LSTM nodes: ", numLSTMnodeOption)
    print(" Number of hidden nodes: ", numHiddenNodeOption)
    print(" Using convolution: ", useConvolutionOption)
    print(" Activation option: ", activationOption)
    print(" Using embedding layer: ",  embeddingOption)
    print(" Balance option: ",  balanceOption)
    return

def printSingleResult(result, fold):
    (accuracy, precision, sensitivity, specificity, fMeasure) = result
    print("Fold ", fold)
    print(" Accuracy: ", accuracy)
    print(" Precision: ", precision)
    print(" Sensitivity: ", sensitivity)
    print(" Specificity: ", specificity)
    print(" F-Measure: ", fMeasure)
    return

def printConfigurationResultSummary(result):
    (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configuration) = result
    print("Summary of configuration")
    printConfigurationParameters(configuration)
    
    print("Balanced results")
    for i in range(len(scoreOfFoldsBalanced)):
        printSingleResult(scoreOfFoldsBalanced[i], i)
    printSummaryStatistic(getSummaryStatistics(scoreOfFoldsBalanced))
    
    print("Unbalanced results")
    for i in range(len(scoreOfFoldsUnbalanced)):
        printSingleResult(scoreOfFoldsUnbalanced[i], i)
    printSummaryStatistic(getSummaryStatistics(scoreOfFoldsUnbalanced))
    return

def printSummaryStatistic(summaryStatistic):
    (accuracySummary, precisionSummary, sensitivitySummary, specificitySummary, fMeasureSummary) = summaryStatistic
    print('Summary Statistics')
    print(' Accuracy: ', accuracySummary[0], ' +/- ', accuracySummary[1])
    print(' Precision: ', precisionSummary[0], ' +/- ', precisionSummary[1])
    print(' Sensitivity: ', sensitivitySummary[0], ' +/- ', sensitivitySummary[1])
    print(' Specificity: ', specificitySummary[0], ' +/- ', specificitySummary[1])
    print(' F-Measure: ', fMeasureSummary[0], ' +/- ', fMeasureSummary[1])

# Print a summary of the test run
def printResultSummary(testType, results):
    print('--------------------------------')
    print('Summary of ' + testType + ' test')

    for i in range(len(results)):
        print('Configuration ', i)
        printConfigurationResultSummary(results[i])
    print('--------------------------------')