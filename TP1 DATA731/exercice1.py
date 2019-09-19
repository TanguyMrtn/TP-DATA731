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

covY1 = np.cov(Y1)
covY2 = np.cov(Y2)
covY3 = np.cov(Y3)

#La matrice de covariance : X1-X1   X2-X1
#                           X1-X2   X2-X2

#On déduit qu'il n'y a pas de lien décevable entre les pluviométries des 3 stations (covariances de X1 X2 X3 très prochent de 0)



def drowPlot(Y,title):
    fig = PLOT.figure()
    fig.suptitle(title)
    ax = fig.add_subplot(111, projection='3d')
    (x, y) = Y
    hist, xedges, yedges = np.histogram2d(x, y, bins=25, range=[[min(Y[0]), max(Y[0])], [min(Y[1]), max(Y[1])]])
    
    # Construct arrays for the anchor positions of the 16 bars.
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    
    # Construct arrays with the dimensions for the 16 bars.
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()
    
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')    


#drowPlot(Y1,"Y1")
#drowPlot(Y2,"Y2")
#drowPlot(Y3,"Y3")
#
#PLOT.figure(figsize=(9,3))
#PLOT.subplot(311)
#mean = np.mean(Y1)
#std = np.std(Y1)
#count,bins,ignored = PLOT.hist(Y1,51,normed=True)
#PLOT.plot(bins, 1/(std*np.sqrt(2*np.pi))*np.exp(-(bins-mean)**2/(2*std**2)), linewidth=2, color="r")
#PLOT.xlim(8,9)
#PLOT.subplot(312)
#mean = np.mean(Y2)
#std = np.std(Y2)
#count,bins,ignored = PLOT.hist(Y2,51,normed=True)
#PLOT.plot(bins, 1/(std*np.sqrt(2*np.pi))*np.exp(-(bins-mean)**2/(2*std**2)), linewidth=2, color="r")
#PLOT.subplot(313)
#mean = np.mean(Y3)
#std = np.std(Y3)
#count,bins,ignored = PLOT.hist(Y3,51,normed=True)
#PLOT.plot(bins, 1/(std*np.sqrt(2*np.pi))*np.exp(-(bins-mean)**2/(2*std**2)), linewidth=2, color="r")
#PLOT.show()


PLOT.figure(figsize=(9,3))
PLOT.subplot(311)
PLOT.plot(X1)
PLOT.subplot(312)
PLOT.plot(X2)
PLOT.subplot(313)
PLOT.plot(X3)
PLOT.show()
