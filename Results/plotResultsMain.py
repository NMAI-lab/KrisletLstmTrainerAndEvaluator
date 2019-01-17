# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:16 2019

@author: Patrick
"""

from resultsUtility import getResults
from plotUtilities import generatePlot


fileName = 'results.pdf'

# Set the types of tests that need to be plotted
testType = list()
testType.append('finite turn LSTM')
testType.append('finite turn baseline')
testType.append('kick spin LSTM')
testType.append('kick spin baseline')
testType.append('turn direction LSTM')
testType.append('turn direction baseline')

for test in testType:
    # Get specific results
    (results, resultLabels, categories) = getResults(test)
    
    # Generate the plot
    generatePlot(results, resultLabels, categories, fileName, test)
