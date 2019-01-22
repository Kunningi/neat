# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:33:06 2018

@author: Brian
"""

import matplotlib.pyplot as plt

import Card as ea


def simulation(length, population, pm, pi):
    
    sim = ea.Card(population, pm, pi)
    
    #these are each their own list for ease of graphing later
    minlist = []
    q2list = []
    medlist = []
    q3list = []
    maxlist = []
    
    for step in range(length):
        
        sim.step()
        
        #create sorted list of fitness after each step
        fitlist = []
        for individual in range(population):
            fitlist.append(sim.fitness(individual))
        fitlist.sort()
        
        #I know this looks gory, sorry
        minlist.append(fitlist[0])
        q2list.append(fitlist[int(0.25*population)])
        medlist.append(fitlist[int(0.50*population)])
        q3list.append(fitlist[int(0.75*population)])
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
    
    
    
simulation(1000, 100, 0.1, 0.5)