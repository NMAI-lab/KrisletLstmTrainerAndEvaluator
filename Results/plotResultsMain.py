# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:16 2019

@author: Patrick
"""

from resultsUtility import getResults, getClassBalance
from plotUtilities import generatePlot, plotBalance


fileName = 'results.pdf'

# Prepare the class balance plot
(classBalance, labels, categories) = getClassBalance()
plotBalance(classBalance, labels, categories, fileName, 'class balance')

# Set the types of tests that need to be plotted
testType = list()
testType.append('reactive LSTM')
testType.append('reactive baseline')
testType.append('kick spin LSTM')
testType.append('kick spin baseline')
testType.append('turn direction LSTM')
testType.append('turn direction baseline')

for test in testType:
    # Get specific results
    (results, resultLabels, categories) = getResults(test)
    
    # Generate the plot
    generatePlot(results, resultLabels, categories, fileName, test)

