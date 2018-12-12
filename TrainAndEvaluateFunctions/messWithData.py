# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from sEpressionDataExtraction import loadData

testType = "sexpt_tests"
depth = 0

# Setup feature parameters
actionIncludeList = ['turn', 'dash', 'kick']

# ga is short for goal adversary (where we don't want the ball to go)
# go is short for goal own (where we want the ball to go)
featureIncludeList = ['b','ga']#['b','go','ga']


data = loadData(testType, depth, actionIncludeList, featureIncludeList)