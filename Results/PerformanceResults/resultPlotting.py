# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:09:50 2019

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Generate the plot
"""
def generatePlot(results, labels, categories, fileName):
    
    # Unpack the results
    (turnP, turnM, dash, kick) = results

    # Set parameters for the plot window
    numCategories = len(categories)         # Get the number of categories
    groupLocation = np.arange(len(turnP))   # the x locations for the groups
    width = 0.9                             # the width of the bars (max is 1)
    subBarWidth = width / numCategories     # Width of the sub bars

    # Generate the plot
    fig, ax = plt.subplots()
    barLocation = groupLocation - (2 * subBarWidth) + (0.5 * subBarWidth)
    rects0 = ax.bar(barLocation, turnP, subBarWidth, yerr = 0, label = categories[0])
    
    barLocation = groupLocation - (0.5 * subBarWidth)
    rects1 = ax.bar(barLocation, turnM, subBarWidth, yerr = 0, label = categories[1])
    
    barLocation = groupLocation + (0.5 * subBarWidth)
    rects2 = ax.bar(barLocation, dash, subBarWidth, yerr = 0, label = categories[2])
    
    barLocation = groupLocation + (2 * subBarWidth) - (0.5 * subBarWidth)
    rects3 = ax.bar(barLocation, kick, subBarWidth, yerr = 0, label = categories[3])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    yLabel = 'F measure'
    xLabel = 'Model type'
    fullFileName = fileName + ".pdf"
    
    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)
    ax.set_xticks(groupLocation)
    ax.set_xticklabels(labels)
    plt.grid(which = 'both', axis = 'y')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    #autoLabel(ax, rects0, turnP, "center")
    #autoLabel(ax, rects1, turnM, "center")
    #autoLabel(ax, rects2, dash, "center")
    #autoLabel(ax, rects3, kick, "center")

    # Save the plot
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
    data

    for i in range(len(rects)):
        rect = rects[i]
        height = rect.get_height()
        label = str(round(data[i], 2))
        xPosition = rect.get_x() + rect.get_width()*offset[xpos]
        yPosition = 1.01*height
        ax.text(xPosition, yPosition, label, ha=ha[xpos], va='bottom')