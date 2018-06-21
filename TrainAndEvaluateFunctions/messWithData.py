# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:54:43 2018

@author: patrickgavigan
"""

from parsingFunctions import parseFile, buildSequenceDataSet

(x,y) = parseFile()

depth = 2
(newX, newY) = buildSequenceDataSet(x, y, depth)