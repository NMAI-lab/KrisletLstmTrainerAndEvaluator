# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:33:31 2019

@author: Patrick
"""

from resultLoader import getAllScores
from resultCleaning import getTestScores

(scenarios,scores) = getAllScores("logs")

(FiniteTurnExpertTests, FiniteTurnExpertScores) = getTestScores(scenarios, scores, "FiniteTurn", True)
