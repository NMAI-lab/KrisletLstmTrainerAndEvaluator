# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:09:11 2019

@author: Patrick
"""

from finiteTurnResults import getLstmFiniteTurnRaw, getBaselineFiniteTurnRaw, getFiniteTurnClassBalance
from kickSpinResults import getLstmKickSpinRaw, getBaselineKickSpinRaw, getKickSpinClassBalance
from turnDirectionResults import getLstmTurnDirectionRaw, getBaselineTurnDirectionRaw, getTurnDirectionBalance


"""
Get the test results that need to be plotted
"""
def getResults(testType):
    # Get the data
    if testType == 'reactive LSTM':
        result = getLstmFiniteTurnRaw()
        labels = ('LSTM 1', 'LSTM 2', 'LSTM 3', 'LSTM 4', 'LSTM 5', 'LSTM 6')
    elif testType == 'reactive baseline':
        result = getBaselineFiniteTurnRaw()
        labels = ('Dense 1', 'Dense 2', 'Dense 3', 'jLOAF 1', 'jLOAF 2', 'jLOAF 3', 'jLOAF 4')
    elif testType == 'kick spin LSTM':
        result = getLstmKickSpinRaw()
        labels = ('LSTM 1', 'LSTM 2', 'LSTM 3', 'LSTM 4', 'LSTM 5', 'LSTM 6')
    elif testType == 'kick spin baseline':
        result = getBaselineKickSpinRaw()
        labels = ('Dense 1', 'Dense 2', 'Dense 3', 'jLOAF 1', 'jLOAF 2', 'jLOAF 3', 'jLOAF 4')
    elif testType == 'turn direction LSTM':
        result = getLstmTurnDirectionRaw()
        labels = ('LSTM 1', 'LSTM 2', 'LSTM 3', 'LSTM 4', 'LSTM 5', 'LSTM 6')
    elif testType == 'turn direction baseline':
        result = getBaselineTurnDirectionRaw()
        labels = ('Dense 1', 'Dense 2', 'Dense 3', 'jLOAF 1', 'jLOAF 2', 'jLOAF 3', 'jLOAF 4')
        
    categories = ('turn+', 'turn-', 'dash', 'kick')
        
    # Format it and return it
    return (formatResult(result), labels, categories)

"""
Format the data properly
"""
def formatResult(data):
    (result, error) = data
    
    # Set index locations (these are constants)
    turnPindex = 0
    turnMindex = 1
    dashIndex = 2
    kickIndex = 3
    
    # Make lists for the results
    turnPvalue = list()
    turnPerror = list()
    turnMvalue = list()
    turnMerror = list()
    dashValue = list()
    dashError = list()
    kickValue = list()
    kickError = list()
    
    # Process the data
    for i in range(len(result)):
        turnPvalue.append(result[i][turnPindex])
        turnPerror.append(error[i][turnPindex])
        turnMvalue.append(result[i][turnMindex])
        turnMerror.append(error[i][turnMindex])
        dashValue.append(result[i][dashIndex])
        dashError.append(error[i][dashIndex])
        kickValue.append(result[i][kickIndex])
        kickError.append(error[i][kickIndex])
        
    # format the output
    turnP = (tuple(turnPvalue), tuple(turnPerror))
    turnM = (tuple(turnMvalue), tuple(turnMerror))
    dash = (tuple(dashValue), tuple(dashError))
    kick = (tuple(kickValue), tuple(kickError))
    
    results = (turnP, turnM, dash, kick)
    return results


def getClassBalance():
    finiteTurn = getFiniteTurnClassBalance()
    kickSpin = getKickSpinClassBalance()
    turnDirection = getTurnDirectionBalance()
    
    # Set index locations (these are constants)
    turnPindex = 0
    turnMindex = 1
    dashIndex = 2
    kickIndex = 3
    
    # Convert everything to a percentage
    finiteTurn = convertToPercentage(finiteTurn)
    kickSpin = convertToPercentage(kickSpin)
    turnDirection = convertToPercentage(turnDirection)
    
    # Make lists for the results
    turnP = (finiteTurn[turnPindex], kickSpin[turnPindex], turnDirection[turnPindex])
    turnM = (finiteTurn[turnMindex], kickSpin[turnMindex], turnDirection[turnMindex])
    dash = (finiteTurn[dashIndex], kickSpin[dashIndex], turnDirection[dashIndex])
    kick = (finiteTurn[kickIndex], kickSpin[kickIndex], turnDirection[kickIndex]) 
    
    balance = (turnP, turnM, dash, kick)
    labels = ('Reactive','Kick Spin','Turn Direction')
    categories = ('turn+', 'turn-', 'dash', 'kick')
    
    return (balance, labels, categories)

def convertToPercentage(data):
    total = sum(data)
    percentage = list()
    for i in range(len(data)):
        percentage.append((data[i] * 100) / total)
    return tuple(percentage)
