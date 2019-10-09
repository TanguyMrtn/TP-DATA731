# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:25:03 2019

@author: tangu
"""

import scipy.io
import scipy.stats
import numpy as np
import matplotlib.pyplot as PLOT


mat = scipy.io.loadmat('X_pluv_100Villes.mat')
data = mat['X_pluv']

X1 = data[0]
X2 = data[1]
X3 = data[2]
pas = 150

for X in [X1,X2,X3]:
    total_entropy = []
    iteration = 0
    while iteration+pas*2 != len(X1)+1 :
    
        firstSet = X[iteration:iteration+pas-1]
        secondSet = X[iteration+pas:iteration+pas*2]
        
        print(iteration+pas*2)
        
        firstSetMean = np.mean(firstSet)
        secondSetMean = np.mean(secondSet)
        
        firstSetVar = (np.std(firstSet))
        secondSetVar = (np.std(secondSet))
        
        part1 = ((firstSetMean - secondSetMean)**2)/(firstSetVar**2+secondSetVar**2)
        part2 = ((firstSetVar**2)/(secondSetVar**2))+((secondSetVar**2)/(firstSetVar**2))
        
        entropy = (1/2)*part1 + (1/2)*part2 - 1
        
        total_entropy.append(entropy)
        iteration += 1
    PLOT.plot(total_entropy)

PLOT.show()



