# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:05:27 2019

@author: Patrick
"""

def getLstmKickSpinRaw():
    result = list()
    error = list()
    
    # Configuration 0
    # F-Measure:  [ ]
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # Configuration 1
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    # Configuration 8
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # Configuration 9
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    # Configuration 16
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # Configuration 17
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    return (result, error)
    
def getBaselineKickSpinRaw():
    result = list()
    error = list()
    
    # Configuration 18
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # Configruation 19
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    # Configuration 20
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # TB
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    # K ordered
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    # K unordered
    # F-Measure:  []
    result.append((0.84387518, 0.90788048, 0.86028083, 0.85490484))
    error.append((0.02833899, 0.01990184, 0.03829741, 0.0281164))
    
    # K ordered r
    # F-Measure:  []
    result.append((0.87083069, 0.9175893, 0.88383731, 0.88274466))
    error.append((0.01980862, 0.03022737, 0.02652221, 0.02979861))
    
    return (result, error)
