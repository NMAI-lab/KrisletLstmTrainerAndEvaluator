# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:21:07 2018

@author: patrickgavigan
"""

import csv
import os.path
from evaluationMetrics import getSummaryStatistics

# Write a single result row to the CSV. Will vreate the CSV if it does not exist
def writeSingleResult(testType, result, fileName = 'names.csv'):
    
    (balancedResult, unbalancedResult, configuration) = result;
    #balancedSummary = getSummaryStatistics(balancedResult);
    #unBalancedSummary = getSummaryStatistics(unbalancedResult);
    balancedSummary = tempGetResult();
    unBalancedSummary = tempGetResult();
    
    # Check if the file exists (in case we need a header line or not)
    fileExists = os.path.isfile(fileName);

    # Define the fieldnames for the file
    fieldnames = getFieldNames();
    
    # Open the file (or create it if it isn't there). Append mode
    with open(fileName, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file did not exist, print the header    
        if fileExists == False:
            writer.writeheader();
        
        # Write the row
        rowContents = getRowContents(testType, configuration, balancedSummary, 
                                     unBalancedSummary);
        writer.writerow(rowContents);

# Get the fieldnames for the CSV file 
def getFieldNames():
    return ['Test Type',
            'Configuration Number',
            'Run Depth',
            '# LSTM Nodes',
            '# Hidden Nodes',
            'Convolution Used',
            'Activation',
            'Embedding Used',
            'Class Resampling',
            'Early Stop Min Delta',
            'Early Stop Patience',
            'Reduce LR Factor',
            'Reduce LR Patience',
            'Reduce LR min_lr',            
            'Balanced Accuracy Mean',
            'Balanced Accuracy Standard Deviation',
            'Balanced Precision Mean Turn',
            'Balanced Precision Deviation Turn',
            'Balanced Precision Mean Dash',
            'Balanced Precision Deviation Dash',
            'Balanced Precision Mean Kick',
            'Balanced Precision Deviation Kick',
            'Balanced Sensitivity Mean Turn',
            'Balanced Sensitivity Deviation Turn',
            'Balanced Sensitivity Mean Dash',
            'Balanced Sensitivity Deviation Dash',
            'Balanced Sensitivity Mean Kick',
            'Balanced Sensitivity Deviation Kick',
            'Balanced Specificity Mean Turn',
            'Balanced Specificity Deviation Turn',
            'Balanced Specificity Mean Dash',
            'balancedSpecificityDeviationDash',
            'balancedSpecificityMeanKick',
            'balancedSpecificityDeviationKick',
            'balancedFMeasureMeanTurn',
            'balancedFMeasureDeviationTurn',
            'balancedFMeasureMeanDash',
            'balancedFMeasureDeviationDash',
            'balancedFMeasureMeanKick',
            'balancedFMeasureDeviationKick',
            'unbalancedAccuracyMean',
            'unbalancedAccuracyStandardDeviation',
            'unbalancedPrecisionMeanTurn',
            'unbalancedPrecisionDeviationTurn',
            'unbalancedPrecisionMeanDash',
            'unbalancedPrecisionDeviationDash',
            'unbalancedPrecisionMeanKick',
            'unbalancedPrecisionDeviationKick',
            'unbalancedSensitivityMeanTurn',
            'unbalancedSensitivityDeviationTurn',
            'unbalancedSensitivityMeanDash',
            'unbalancedSensitivityDeviationDash',
            'unbalancedSensitivityMeanKick',
            'unbalancedSensitivityDeviationKick',
            'unbalancedSpecificityMeanTurn',
            'unbalancedSpecificityDeviationTurn',
            'unbalancedSpecificityMeanDash',
            'unbalancedSpecificityDeviationDash',
            'unbalancedSpecificityMeanKick',
            'unbalancedSpecificityDeviationKick',
            'unbalancedFMeasureMeanTurn',
            'unbalancedFMeasureDeviationTurn',
            'unbalancedFMeasureMeanDash',
            'unbalancedFMeasureDeviationDash',
            'unbalancedFMeasureMeanKick',
            'unbalancedFMeasureDeviationKick']

def getRowContents(testType, configuration, balancedSummary, unBalancedSummary):
    
    (runDepth, numLSTMnodes, numHiddenNodes, useConvolution, activation,
     embedding, balance, earlyStopOptions, reduceLROptions, 
     configCount) = configuration
    (earlyStopMinDelta, earlyStopPatience) = earlyStopOptions
    (ReduceLRfactor, ReduceLRpatience, ReduceLRmin_lr) = reduceLROptions
    
    (balancedAccuracySummary, balancedPrecisionSummary, 
     balancedSensitivitySummary, balancedSpecificitySummary, 
     balancedFMeasureSummary) = balancedSummary

    (unBalancedAccuracySummary, unBalancedPrecisionSummary, 
     unBalancedSensitivitySummary, unBalancedSpecificitySummary, 
     unBalancedFMeasureSummary) = unBalancedSummary         
     
    return {'testType': testType,
            'Configuration Number': configCount,
            'runDepthOptions': runDepth,
            'numLSTMnodeOptions': numLSTMnodes,
            'numHiddenNodeOptions': numHiddenNodes,
            'useConvolutionOptions': useConvolution,
            'activationOptions': activation,
            'embeddingOptions': embedding,
            'balanceOptions': balance,
            'earlyStopMinDelta': earlyStopMinDelta,
            'earlyStopPatience': earlyStopPatience,
            'ReduceLRfactor': ReduceLRfactor,
            'ReduceLRpatience': ReduceLRpatience,
            'ReduceLRmin_lr': ReduceLRmin_lr,
            'balancedAccuracyMean': balancedAccuracySummary[0],
            'balancedAccuracyStandardDeviation': balancedAccuracySummary[1],
            'balancedPrecisionMeanTurn': balancedPrecisionSummary[0][0],
            'balancedPrecisionDeviationTurn': balancedPrecisionSummary[1][0],
            'balancedPrecisionMeanDash': balancedPrecisionSummary[0][1],
            'balancedPrecisionDeviationDash': balancedPrecisionSummary[1][1],
            'balancedPrecisionMeanKick': balancedPrecisionSummary[0][2],
            'balancedPrecisionDeviationKick': balancedPrecisionSummary[1][2],
            'balancedSensitivityMeanTurn': balancedSensitivitySummary[0][0],
            'balancedSensitivityDeviationTurn': balancedSensitivitySummary[1][0],
            'balancedSensitivityMeanDash': balancedSensitivitySummary[0][1],
            'balancedSensitivityDeviationDash': balancedSensitivitySummary[1][1],
            'balancedSensitivityMeanKick': balancedSensitivitySummary[0][2],
            'balancedSensitivityDeviationKick': balancedSensitivitySummary[1][2],
            'balancedSpecificityMeanTurn': balancedSpecificitySummary[0][0],
            'balancedSpecificityDeviationTurn': balancedSpecificitySummary[1][0],
            'balancedSpecificityMeanDash': balancedSpecificitySummary[0][1],
            'balancedSpecificityDeviationDash': balancedSpecificitySummary[1][1],
            'balancedSpecificityMeanKick': balancedSpecificitySummary[0][2],
            'balancedSpecificityDeviationKick': balancedSpecificitySummary[1][2],
            'balancedFMeasureMeanTurn': balancedFMeasureSummary[0][0],
            'balancedFMeasureDeviationTurn': balancedFMeasureSummary[1][0],
            'balancedFMeasureMeanDash': balancedFMeasureSummary[0][1],
            'balancedFMeasureDeviationDash': balancedFMeasureSummary[1][1],
            'balancedFMeasureMeanKick': balancedFMeasureSummary[0][2],
            'balancedFMeasureDeviationKick': balancedFMeasureSummary[1][2],
            'unbalancedAccuracyMean': unBalancedAccuracySummary[0],
            'unbalancedAccuracyStandardDeviation': unBalancedAccuracySummary[1],
            'unbalancedPrecisionMeanTurn': unBalancedPrecisionSummary[0][0],
            'unbalancedPrecisionDeviationTurn': unBalancedPrecisionSummary[1][0],
            'unbalancedPrecisionMeanDash': unBalancedPrecisionSummary[0][1],
            'unbalancedPrecisionDeviationDash': unBalancedPrecisionSummary[1][1],
            'unbalancedPrecisionMeanKick': unBalancedPrecisionSummary[0][2],
            'unbalancedPrecisionDeviationKick': unBalancedPrecisionSummary[1][2],
            'unbalancedSensitivityMeanTurn': unBalancedSensitivitySummary[0][0],
            'unbalancedSensitivityDeviationTurn': unBalancedSensitivitySummary[1][0],
            'unbalancedSensitivityMeanDash': unBalancedSensitivitySummary[0][1],
            'unbalancedSensitivityDeviationDash': unBalancedSensitivitySummary[1][1],
            'unbalancedSensitivityMeanKick': unBalancedSensitivitySummary[0][2],
            'unbalancedSensitivityDeviationKick': unBalancedSensitivitySummary[1][2],
            'unbalancedSpecificityMeanTurn': unBalancedSpecificitySummary[0][0],
            'unbalancedSpecificityDeviationTurn': unBalancedSpecificitySummary[1][0],
            'unbalancedSpecificityMeanDash': unBalancedSpecificitySummary[0][1],
            'unbalancedSpecificityDeviationDash': unBalancedSpecificitySummary[1][1],
            'unbalancedSpecificityMeanKick': unBalancedSpecificitySummary[0][2],
            'unbalancedSpecificityDeviationKick': unBalancedSpecificitySummary[1][2],
            'unbalancedFMeasureMeanTurn': unBalancedFMeasureSummary[0][0],
            'unbalancedFMeasureDeviationTurn': unBalancedFMeasureSummary[1][0],
            'unbalancedFMeasureMeanDash': unBalancedFMeasureSummary[0][1],
            'unbalancedFMeasureDeviationDash': unBalancedFMeasureSummary[1][1],
            'unbalancedFMeasureMeanKick': unBalancedFMeasureSummary[0][2],
            'unbalancedFMeasureDeviationKick': unBalancedFMeasureSummary[1][2]}
   

def tempGetResult(data = 'blah'):
    accuracy = 0
    accuracyDeviation = 1
    precision = [2, 4, 6]
    precisionDeviation = [3, 5, 7]
    sensitivity = [8, 10, 12]
    sensitivityDeviation = [9, 11, 13]
    specificity = [14, 16, 18]
    specificityDeviation = [15, 17, 19]
    FMeasure = [20, 22, 24]
    FMeasureDeviation = [21, 23, 25]

    accuracySummary = (accuracy, accuracyDeviation)
    precisionSummary = (precision, precisionDeviation)
    sensitivitySummary = (sensitivity, sensitivityDeviation)
    specificitySummary = (specificity, specificityDeviation)
    fMeasureSummary = (FMeasure, FMeasureDeviation)
    
    summaryStatistic = (accuracySummary, precisionSummary, sensitivitySummary, specificitySummary, fMeasureSummary)
    return summaryStatistic