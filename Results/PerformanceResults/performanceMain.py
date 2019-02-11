# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:33:31 2019

@author: Patrick
"""

from resultLoader import loadResults, getFMeasure

(expertAction, studentAction) = loadResults("result.log")
score = getFMeasure(expertAction, studentAction) 