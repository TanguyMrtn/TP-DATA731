# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:25:03 2019

@author: tangu
"""

import scipy.io
import scipy.stats
import numpy as np
import matplotlib.pyplot as PLOT
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

mat = scipy.io.loadmat('X_pluv_100Villes.mat')
data = mat['X_pluv']

X1 = data[0]
X2 = data[1]
X3 = data[2]

n = 20





for X in [X1,X2,X3] :
    
    final = [X[i * n:(i + 1) * n] for i in range((len(X) + n - 1) // n )]  
    total_entropy = []
    for i in range(0,len(final)-1):
        entropy = scipy.stats.entropy(final[i],final[i+1])
        total_entropy.append(entropy)
        
    PLOT.plot(total_entropy)

    print("max value at : ", total_entropy.index(max(total_entropy)), " : ", max(total_entropy))
PLOT.show()


