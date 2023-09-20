import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from array import *
import math


# x_values = np.linspace(x_min, x_max, 100)
# Renvoie des nombres espacés régulièrement sur un intervalle spécifié.
# Renvoie un nombre d'échantillons régulièrement espacés, calculés sur l'intervalle [ start , stop ].
# Le point final de l’intervalle peut éventuellement être exclu.

def task02():
    # générer un dataset 
    x = [0, 1, 2, 3]
    y = [12, 32, 42, 52]
    # tracer le graphique
    plt.scatter(x,y,s=50)
    plt.ylabel('some numbers')
    plt.grid()
    plt.show()

def task03():

    def show(x, y):
        plt.scatter(x,y,s=50)
        plt.ylabel('some numbers')
        plt.grid()
        plt.show()
    
    x = list(map(int, input("Enter the array X: ").strip().split()))
    y = list(map(int, input("Enter the array Y: ").strip().split()))
    show(x, y)

def task04():
    # Fontion donnée qui calcule la valeur Y pour chaque valeur X
    def f(x):
        return x**2 + x*3 + 1
    
    # Fonction qui affiche le graphique de la fonction f
    def plt_fct(func, x_min, x_max):
        x = np.linspace(x_min, x_max, x_max) #Créer un tableau de x valeurs equidistantes
        y = np.vectorize(func)(x) # Appliquer la fonction func à chaque valeur de x
        plt.plot(x, y)
        plt.show()

    plt_fct(math.sin , 0, 50)
    plt_fct(f, -100, 200)
    plt_fct(lambda x: x**2, -10, 10)
    plt_fct(lambda x: 1/x, -100, 100)




# task02()
# task03()
task04()