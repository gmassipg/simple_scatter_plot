
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:03:03 2021

@author: Gerard
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as sts

filedata = pd.read_excel("data_to_plot.xlsx", "data")
labels = pd.read_excel("data_to_plot.xlsx", "plot_labels")
filedata_array = filedata.to_numpy()
labels_array = labels.to_numpy()

xx = filedata_array[:, 0]
yy = filedata_array[:, 1]
#error_x = filedata_array[:, 2]
#error_y = filedata_array[:, 3]
title = labels_array[0, 0]
xlabel = labels_array[0, 1]   
ylabel = labels_array[0, 2]
data_legend_label = labels_array[0,3]

#error bars info:
#https://www.youtube.com/watch?v=xhizVO9SPjU&ab_channel=KarinaAdcock


question1 = input("Perform linear regression? [y/n]: ")

if question1 == "y":
    reg = sts.linregress(xx, yy)
    
    plt.figure("Figure 1")
    plt.title(title)
    plt.plot(xx, yy, "r.", label=data_legend_label)
    plt.plot(xx, reg[0]*xx + reg[1], \
             label="y="+str(format(reg[0], '.5g'))+"x+"\
                 +str(format(reg[1], '.5g'))+", $R^2$="+\
                     str(format(reg[2], '.5g')))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid("True")
    plt.tight_layout()
    plt.savefig('chart.svg')
elif question1 == "n":    
    plt.figure("Figure 1")
    plt.title(title)
    plt.plot(xx, yy, "r.")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid("True")
    plt.tight_layout()
    plt.savefig('chart.svg')
    
else:
    print("Error")