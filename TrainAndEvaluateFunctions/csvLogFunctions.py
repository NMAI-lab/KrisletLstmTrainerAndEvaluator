# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:21:07 2018

@author: patrickgavigan
"""

import csv
import os.path
from evaluationMetrics import getSummaryStatistics


def writeSingleResult(testType, configuration, result, fileName = 'names.csv'):
    
    (balancedResult, unbalancedResult, configuration) = result;
    balancedSummary = getSummaryStatistics(balancedResult);
    unbalancedSummary = getSummaryStatistics(unbalancedResult);

    # Check if the file exists (in case we need a header line or not)
    fileExists = os.path.isfile(fileName);

    # Define the fieldnames for the file
    fieldnames = ['testType',
                  'runDepthOptions',
                  'numLSTMnodeOptions',
                  'numHiddenNodeOptions',
                  'useConvolutionOptions',
                  'activationOptions',
                  'embeddingOptions',
                  'balanceOptions',
                  'balancedAccuracyMean',
                  'balancedAccuracyStandardDeviation',
                  'balancedPrecisionMeanTurn',
                  'balancedPrecisionDeviationTurn',
                  'balancedPrecisionMeanDash',
                  'balancedPrecisionDeviationDash',
                  'balancedPrecisionMeanKick',
                  'balancedPrecisionDeviationKick',
                  'balancedSensitivityMeanTurn',
                  'balancedSensitivityDeviationTurn',
                  'balancedSensitivityMeanDash',
                  'balancedSensitivityDeviationDash',
                  'balancedSensitivityMeanKick',
                  'balancedSensitivityDeviationKick',
                  'balancedSpecificityMeanTurn',
                  'balancedSpecificityDeviationTurn',
                  'balancedSpecificityMeanDash',
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
                  'unbalancedFMeasureDeviationKick',
                  ];
    
    # Open the file (or create it if it isn't there). Append mode
    with open(fileName, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file did not exist, print the header    
        if fileExists == False:
            writer.writeheader();
        
        # Write the row
        writer.writerow({'testType': testType,
                         'runDepthOptions': configuration[0],
                         'numLSTMnodeOptions': configuration[1],
                         'numHiddenNodeOptions': configuration[2],
                         'useConvolutionOptions': configuration[3],
                         'activationOptions': configuration[4],
                         'embeddingOptions': configuration[5],
                         'balanceOptions': configuration[6],
                         'balancedAccuracyMean',
                         'balancedAccuracyStandardDeviation',
                         'balancedPrecisionMeanTurn',
                         'balancedPrecisionDeviationTurn',
                         'balancedPrecisionMeanDash',
                         'balancedPrecisionDeviationDash',
                         'balancedPrecisionMeanKick',
                         'balancedPrecisionDeviationKick',
                         'balancedSensitivityMeanTurn',
                         'balancedSensitivityDeviationTurn',
                         'balancedSensitivityMeanDash',
                         'balancedSensitivityDeviationDash',
                         'balancedSensitivityMeanKick',
                         'balancedSensitivityDeviationKick',
                         'balancedSpecificityMeanTurn',
                         'balancedSpecificityDeviationTurn',
                         'balancedSpecificityMeanDash',
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
                         'unbalancedFMeasureDeviationKick',
                         
                         'result': result});
        
        
   
# Accuracy:  0.732739514182  +/-  0.0293960406469
# Precision:  [ 0.30056512  0.97715885  0.02421726]  +/-  [ 0.04352671  0.00526345  0.00245817]
# Sensitivity:  [ 0.66086318  0.74189452  0.825     ]  +/-  [ 0.03895942  0.03619155  0.06844864]
# Specificity:  [ 0.79340036  0.86844798  0.93083106]  +/-  [ 0.04434359  0.03303544  0.01042574]
# F-Measure:  [ 0.41033715  0.84288376  0.04702433]  +/-  [ 0.03587286  0.02235951  0.00460275]