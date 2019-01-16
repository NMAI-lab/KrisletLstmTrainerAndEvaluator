# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:16 2019

@author: Patrick
"""

from resultsUtility import getResults
from plotUtilities import generatePlot

fileName = 'results.pdf'

# Get the results that need to be plotted
testType = 'finie turn LSTM'
#testType = 'finie turn baseline'
#testType = 'kick spin LSTM'
#testType = 'kick spin baseline'
#testType = 'turn direction LSTM'
#testType = 'turn direction baseline'
(results, resultLabels, categories) = getResults(testType)

# Generate the plot
generatePlot(results, resultLabels, categories, fileName, testType)
