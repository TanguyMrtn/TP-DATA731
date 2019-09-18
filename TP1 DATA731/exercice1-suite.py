# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:25:03 2019

@author: tangu
"""

import scipy.io
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

Y1 = (X1,X2)
Y2 = (X2,X3)
Y3 = (X3,X1)

fig = PLOT.figure()
#fig.suptitle(title)
ax = fig.add_subplot(111, projection='3d')
(x, y) = Y1
hist, xedges, yedges = np.histogram2d(x, y, bins=25, range=[[min(Y1[0]), max(Y1[0])], [min(Y1[1]), max(Y1[1])]])
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
PLOT.show()

# Construct arrays for the anchor positions of the 16 bars.
#xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
#xpos = xpos.ravel()
#ypos = ypos.ravel()
#zpos = 0

# Construct arrays with the dimensions for the 16 bars.
#dx = dy = 0.5 * np.ones_like(zpos)
#dz = hist.ravel()
#
#ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')