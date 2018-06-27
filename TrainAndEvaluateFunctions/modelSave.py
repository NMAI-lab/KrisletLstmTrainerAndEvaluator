# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:43:31 2018

@author: patrickgavigan
"""
import datetime

def saveModel(model, configuration, accuracy, deviation, note = None):
    fileName = getModelFileName(configuration, accuracy, deviation, note)
    model.save(fileName)  # creates a HDF5 file 'my_model.h5'

def getModelFileName(configuration, accuracy, deviation, note = None):
    fileExtension = '.h5'
    fileNameSuffix = 'Configuration' + str(configuration) + 'Accuracy' + str(accuracy) + 'Deviation' + str(deviation)
    
    if note != None:
        fileNameSuffix = fileNameSuffix + str(note)
    fileNameSuffix = fileNameSuffix + fileExtension
    
    fileName = timeStamped(fileNameSuffix)
    return fileName  

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)