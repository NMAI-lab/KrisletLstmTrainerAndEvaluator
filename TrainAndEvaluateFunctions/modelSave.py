# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:43:31 2018

@author: patrickgavigan
"""
import datetime

def saveModel(model, currentResult, configurationNumber, note = None):
    fileName = getModelFileName(currentResult, configurationNumber, note)
    model.save(fileName)  # creates a HDF5 file 'my_model.h5'

# Need to update this to include some sort of summary statistic in the file name
def getModelFileName(result, configurationNumber, note = None):
    fileExtension = '.h5'
    (scoreOfFoldsBalanced, scoreOfFoldsUnbalanced, configuration) = result
    
    fileNameSuffix = 'Configuration_' + str(configurationNumber) + '_'# + 'Accuracy' + str(accuracy) + 'Deviation' + str(deviation)
    
    if note != None:
        fileNameSuffix = fileNameSuffix + str(note)
    fileNameSuffix = fileNameSuffix + fileExtension
    
    fileName = timeStamped(fileNameSuffix)
    return fileName  

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)