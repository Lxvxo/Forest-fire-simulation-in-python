# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:27:58 2021

@author: singl
"""

# Import necessary libraries
from math import exp
import numpy as np
from random import *
import random
from matplotlib import pyplot as plt

# Parameters for fire spread model
a = 7.255
b = 0.092
c = 0.067
d = 0.932

# Function to calculate fire spread velocity
def vitesse(Ve=20.725, Mv=0.8):
    L = [k for k in range(4, 11)]
    i = randint(0, 6)
    h = L[i]
    return a * Ve**b * h**c * exp(-d * Mv) 

# Calculate velocity and time
V = vitesse() / 3.6
t = 1
case = 10
while t * V < case:
    t += 1
t = round(t / 2)

# Define different states for the cells
etat = {"SOL": [0], "ARBRE": [1], 
        "FEU 1": [k for k in range(2, int((2 + t) / 2) + 1)],
        "FEU 2": [k for k in range(int((2 + t) / 2 + 1), 3 + t)],
        "FEU 3": [k for k in range(3 + t, (3 + t) * 3 + 1)], 
        "CENDRE": [(3 + t) * 3 + 1]}

# Function to initialize the grid with trees and initial fire
def init(n=20, p=2/3, f=1):
    g = np.zeros((n, n))
    for k in range(n):
        for i in range(n):
            g[k, i] = random.choices([etat["SOL"][0], 
                                      etat["ARBRE"][0]], [1 - p, p], k=1)[0]
    A = []
    for k in range(n):
        for i in range(n):
            if g[k, i] == 1:
                A.append([k, i])
    for a in range(f):
        feu = random.choices(A, k=1)
        g[feu[0][0], feu[0][1]] += etat["FEU 1"][0]
    return g

# Function to plot the grid
def hinton(matrix, max_weight=None, ax=None):
    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2 ** np.ceil(np.log2(np.abs(matrix).max()))

    ax.patch.set_facecolor('peru')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x, y), w in np.ndenumerate(matrix):
        if w in etat['SOL']:
            color = 'peru'
        if w in etat['ARBRE']:
            color = 'forestgreen'
        if w in etat['FEU 1']:
            color = 'yellow'
        if w in etat['FEU 2']:
            color = 'orange'
        if w in etat['FEU 3']:
            color = 'red'
        if w >= etat['CENDRE'][0]:
            color = 'gray'
        
        size = np.sqrt(abs(w) / max_weight)
        rect = plt.Rectangle([x - size / 1.5, y - size / 1.5], size, 
                             size, facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()

# Function to compute the next state of the grid
def suivant(M):
    taille = M.shape[0]
    P = M.copy()
    
    for k in range(taille):
        for i in range(taille):
            s=0
            L = [[k+1,i],[k-1,i],[k,i+1],[k,i-1]]
            
            for q in L:
                if (0 < q[0] < taille) & (0 < q[1] < taille) :
                    if M[q[0],q[1]] in etat['FEU 3']:
                        s+= 1
            v =0
            if M[k,i] >= etat['CENDRE'][0]:
                    P[k,i] = etat["CENDRE"][0]
                    s = 0
                    v += 1
            if M[k,i] == etat['SOL'][0] :
                v += 1
                s = 0

            for p in etat['FEU 3']:
                if v != 0:
                    break
                if M[k,i] == p:
                    s+= 1
                    v += 1
                    break
                  
            for p in etat['FEU 2']:
                    if v != 0:
                        break
                    if M[k,i] == p:
                        s+= 1
                        v += 1
                        break
            for p in etat['FEU 1']:
                if v != 0:
                    break
                if M[k,i] == p:
                    s+= 1
                    break
            if M[k,i] >= etat['CENDRE'][0]:
                    P[k,i] = etat["CENDRE"][0]
                    s = 0
            P[k,i] += s
    return P

# Function to simulate the fire spread
def simulation(n=20,p=1/2,f=1,t=1):
    P = init(n,p,f)
    hinton(P)
    nb_feu = 1
    while nb_feu != 0:
        nb_feu = 0
        P = suivant(P)
        hinton(P)
        plt.pause(t)
        #plt.show()
        for x in range(n):
            for y in range(n):
                if P[x,y] in etat['FEU 1']:
                    nb_feu += 1
                elif P[x,y] in etat['FEU 2']: 
                    nb_feu += 1
                elif P[x,y] in etat['FEU 3']:
                    nb_feu += 1
       
                            

simulation(t=0.5,p =1)