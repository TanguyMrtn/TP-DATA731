import numpy as np
import matplotlib.pyplot as PLOT


N = 10000 #Nb d'échantillons
mean = 0 #Moyenne
std = 1 #Variance (sigma²)

#Pour moyenne = 0 et variance = 1, on remarque que pour un grand nombre d'échantillons, la densité de proba théorique suit la loi normal,
#On peut valider le modèle

#Pour un nombre d'échantillon plus faible, le modèle n'est pas valide : la densité de proba théorique ne suit pas du tout la loi normal


array = np.random.normal(mean, np.sqrt(std), N)

print("BBG : \n",array)

#Histogram avec superposition de la vrai loi

count,bins,ignored = PLOT.hist(array,30,normed=True) #En bleu, l'équivalent de la densité de probabilité des données
PLOT.plot(bins, 1/(std*np.sqrt(2*np.pi))*np.exp(-(bins-mean)**2/(2*std**2)), linewidth=2, color="r") #En rouge, la densité de proba théorique
PLOT.show()

