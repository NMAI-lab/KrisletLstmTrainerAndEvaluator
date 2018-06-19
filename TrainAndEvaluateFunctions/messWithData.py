# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from parsingFunctions import parseFile, buildHistory

(x,y) = parseFile()
(newX, newY) = buildHistory(x, y)