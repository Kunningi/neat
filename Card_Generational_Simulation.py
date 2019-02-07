# Q-700 Project 1
#@author: Brian Dahlberg & Justin Slattery
"""
Created on Tuesday Feb 5 8:33 2019

@author: Brian & Justin
"""

import matplotlib.pyplot as plt

from config.scratches.Card_Generational import *


def fitnessFunction(x):
    """Uses fitness function to calculate fitness for a given individual."""
    s = 0
    m = 1
    card = 1

    for gene in ea.initial_gene_pool[x]:
            if gene == True:
                s += card
            elif gene == False:
                m *= card
            card += 1
    s_error = abs((s - 36) / 36)
    m_error = abs((m - 360) / 360)
    for n in range(ea.population_size):
        ea.fit[n] = 1 - (s_error + m_error) / 2

    return ea.fit

population_size = 100
p_mutation = 0.1
p_reproduce = 0.5
generations = 10

ea = Card_Generational(fitnessFunction, population_size, p_mutation, p_reproduce)

for i in range(generations):
    ea.generation()

ea.showFitness()