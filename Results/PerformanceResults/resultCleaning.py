# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:39:57 2019

@author: Patrick
"""

def getTestScores(testTypes, scores, scenario, useExpert):
    (neededTestTypes, neededScores) =  getScoreSegment(testTypes, scores, scenario, useExpert)
    cleanTestTypes = cleanLabelNames(neededTestTypes)
    return setTestSequence(cleanTestTypes, neededScores)


def getScoreSegment(testTypes, scores, scenario, useExpert):
    if (useExpert):
        agentType = "Expert"
    else:
        agentType = "Student"
    
    applicableTests = list()
    applicableScores = list()
    
    for i in range(len(testTypes)):
        testCase = testTypes[i]
        if ((scenario in testCase) and (agentType in testCase)):
            #newTestCaseName = testCase.replace(scenario, '').replace(agentType, '')
            
            applicableTests.append(testCase.replace(scenario, '').replace(agentType, ''))
            applicableScores.append(scores[i])
    
    return (applicableTests, applicableScores)

def cleanLabelNames(names):
    newNames = list()
    for name in names:
        if (name.lower() == "lstm1"):
            newNames.append("LSTM 1")
            
        elif (name.lower() == "dense1"):
            newNames.append("Dense 1")
            
        elif (name.lower() == "tb"):
            newNames.append("jLOAF 1")
            
        elif (name.lower() == "kordered"):
            newNames.append("jLOAF 2")
            
        elif (name.lower() == "kunordered"):
            newNames.append("jLOAF 3")
            
        elif (name.lower() == "korderedr"):
            newNames.append("jLOAF 4")
            
    return newNames

def setTestSequence(tests, scores):
    testSequence = ["LSTM 1", "Dense 1", "jLOAF 1", "jLOAF 2", "jLOAF 3", "jLOAF 4"]
    scoresSequence = list()
    
    for test in testSequence:
        i = tests.index(test)
        scoresSequence.append(scores[i])
        
    return (testSequence, scoresSequence)
    
    

