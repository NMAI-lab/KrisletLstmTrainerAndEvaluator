# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:02:52 2019

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Generate the plot
"""
def generatePlot(results, labels, categories, fileName, testType):
    
    # Unpack the results
    (turnP, turnM, dash, kick) = results
    (turnP_means, turnP_std) = turnP
    (turnM_means, turnM_std) = turnM
    (dash_means, dash_std) = dash
    (kick_means, kick_std) = kick

    # Set parameters for the plot window
    numCategories = len(categories)             # Get the number of categories
    groupLocation = np.arange(len(turnP_means)) # the x locations for the groups
    width = 0.9                                 # the width of the bars (max is 1)
    subBarWidth = width / numCategories         # Width of the sub bars

    # Generate the plot
    fig, ax = plt.subplots()
    barLocation = groupLocation - (2 * subBarWidth) + (0.5 * subBarWidth)
    rects0 = ax.bar(barLocation, turnP_means, subBarWidth, yerr = turnP_std, label = categories[0])
    
    barLocation = groupLocation - (0.5 * subBarWidth)
    rects1 = ax.bar(barLocation, turnM_means, subBarWidth, yerr = turnM_std, label = categories[1])
    
    barLocation = groupLocation + (0.5 * subBarWidth)
    rects2 = ax.bar(barLocation, dash_means, subBarWidth, yerr = dash_std, label = categories[2])
    
    barLocation = groupLocation + (2 * subBarWidth) - (0.5 * subBarWidth)
    rects3 = ax.bar(barLocation, kick_means, subBarWidth, yerr = kick_std, label = categories[3])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('F measure')
    ax.set_xlabel('Model type')
    ax.set_title('Results for ' + testType + ' scenario')
    ax.set_xticks(groupLocation)
    ax.set_xticklabels(labels)
    plt.grid(which = 'both', axis = 'y')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    #autoLabel(ax, rects0, turnP, "center")
    #autoLabel(ax, rects1, turnM, "center")
    #autoLabel(ax, rects2, dash, "center")
    #autoLabel(ax, rects3, kick, "center")

    # Save the plot
    fullFileName = testType + ' ' + fileName
    plt.savefig(fullFileName, bbox_inches='tight')
    

"""
Attach a text label above each bar in *rects*, displaying its height.

*xpos* indicates which side to place the text w.r.t. the center of
the bar. It can be one of the following {'center', 'right', 'left'}.
"""
def autoLabel(ax, rects, data, xpos='center'):
    xpos = xpos.lower()     # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
    (mean, std) = data

    for i in range(len(rects)):
        rect = rects[i]
        height = rect.get_height()
        label = str(mean[i]) + '\n±\n' + str(std[i])
        xPosition = rect.get_x() + rect.get_width()*offset[xpos]
        yPosition = 1.01*height
        ax.text(xPosition, yPosition, label, ha=ha[xpos], va='bottom')