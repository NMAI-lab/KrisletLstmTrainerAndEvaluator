# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:33:31 2019

@author: Patrick
"""

from resultLoader import getAllScores
from resultCleaning import getTestScores
from resultPlotting import generatePlot
import numpy as np

(scenarios,scores) = getAllScores("logs")

expert = True;
student = False

plotCases = {("FiniteTurn", expert), ("FiniteTurn", student),
             ("KickSpin", expert), ("KickSpin", student),
             ("TurnDirection", expert), ("TurnDirection", student)}

categories = ("turn+", "turn-", "dash", "kick")

for currentPlotCase in plotCases:
    testName = currentPlotCase[0]
    useExpert = currentPlotCase[1]
    (labels, results) = getTestScores(scenarios, scores, testName, useExpert)
    
    turnP = list()
    turnN = list()
    dash = list()
    kick = list()
    for result in results:
        turnP.append(result[0])
        turnN.append(result[1])
        dash.append(result[2])
        kick.append(result[3])
        
    plotResult = (turnP, turnN, dash, kick)
    
    if useExpert:
        fileName = testName + "Expert"
    else:
        fileName = testName + "Student"
    
    generatePlot(plotResult, labels, categories, fileName)
   