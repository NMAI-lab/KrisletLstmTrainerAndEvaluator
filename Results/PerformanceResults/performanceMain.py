# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:33:31 2019

@author: Patrick
"""

from resultLoader import getResults, getFMeasure

(expertAction, studentAction) = getResults("result.txt")
score = getFMeasure(expertAction, studentAction) 