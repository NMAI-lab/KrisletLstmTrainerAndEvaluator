# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from sEpressionDataExtraction import loadData
import numpy as np


# List of test scenarios
testType = ["FiniteTurnKrislet", "StateBasedKickSpin", "StateBasedTurnDirection"] #"ClassicKrislet",  
#testType = ["sexpt_tests"]
depth = 0

# Setup feature parameters
actionIncludeList = ['turn+','turn-', 'dash', 'kick']

# ga is short for goal adversary (where we don't want the ball to go)
# go is short for goal own (where we want the ball to go)
featureIncludeList = ['b','ga']#['b','go','ga']

for test in testType:
    data = loadData(test, depth, actionIncludeList, featureIncludeList)
    (x,y) = data
    fileName = test + ".csv"
    dataFile = open(fileName,'w')
    dataFile.write('ballDist,ballDir,goalDist,goalDir,action\n')
    for i in range(len(y)):
        dataFile.write(str(x[i][0]) + "," + str(x[i][1]) + "," + str(x[i][2]) + "," + str(x[i][3]) + "," + str(y[i]) + "\n")
    dataFile.close()
    
    #unique, counts = np.unique(y, return_counts=True)
    #print(test)
    #print(actionIncludeList)
    #print(dict(zip(unique, counts)))
    #print('----------------------------')