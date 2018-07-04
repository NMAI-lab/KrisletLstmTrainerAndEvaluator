# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:04:38 2018

@author: patrickgavigan
"""
from parsingFunctions import loadData, replacePlaceholder
#from dataManagement import convertToCategorical
from balancingFunctions import underSample, checkBalance

from dataManagement import getData
from modelTrainEvaluateFunctions import trainWithCrossValidation, crossValidateModelConfiguration
from modelTrainEvaluateFunctions import evaluateModel
from modelGenerators import getNumConfigurations
from modelSave import saveModel


def runTestCase(testType):
    
    


depth = 2
data = loadData(testType, depth)

balancedData = underSample(data)

originalBalance = checkBalance(data)
newBalance = checkBalance(balancedData)

finalData = replacePlaceholder(balancedData[0])

#yCategorical = convertToCategorical(data[1])