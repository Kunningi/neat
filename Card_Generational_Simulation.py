# Q-700 Project 1
#@author: Brian Dahlberg & Justin Slattery
"""
Created on Tuesday Feb 5 8:33 2019

@author: Brian & Justin
"""

import matplotlib.pyplot as plt

from config.scratches.Card_Generational import *

ea = Card_Generational(100, 0.1, 0.5, 0.5)

def simulation(duration):
    
    #these are each their own list for ease of graphing later
    minlist = []
    q2list = []
    medlist = []
    q3list = []
    maxlist = []
    
    for step in range(duration):
        
        ea.generation()
        
        #create sorted list of fitness after each step
        fitlist = []
        for individual in range(ea.population_size):
            fitlist.append(ea.fitness(individual))
        fitlist.sort()

        minlist.append(fitlist[0])
        q2list.append(fitlist[int(0.25*ea.population_size)])
        medlist.append(fitlist[int(0.50*ea.population_size)])
        q3list.append(fitlist[int(0.75*ea.population_size)])
        maxlist.append(fitlist[-1])
        
    #plot everything
    plt.plot(minlist, color='#d2691e')
    plt.plot(q2list, '#b35919')
    plt.plot(medlist, '#864313')
    plt.plot(q3list, '#592d0d')
    plt.plot(maxlist, '#2d1606')
    plt.xlabel('Tournaments')
    plt.ylabel('Fitness')
    plt.ylim(0,1)
    plt.title('Tournaments vs. Fitness')
    plt.show()

    return
    
    
    
simulation(100)