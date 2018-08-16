# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:54:51 2018

@author: patrickgavigan
"""

def getRandomSeed():
    seed = 42
    return seed

def setSeeds():
    from numpy.random import seed
    seed(getRandomSeed())
    from tensorflow import set_random_seed
    set_random_seed(getRandomSeed())