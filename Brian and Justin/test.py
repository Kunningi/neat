# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:27:13 2019

@author: Brian
"""

from Card_Generational import Card_Generational

population_size = 25
p_mutation = 0.1
p_reproduce = 0.5
generations = 100

ea = Card_Generational(fitnessFunction, population_size, p_mutation, p_reproduce)

def step(simulations):

    avgFitnessBeginning = []
    bestFitnessBeginning = []
    avgFitnessEnd = []
    bestFitnessEnd = []

    while simulations > 0:
        for i in range(generations):
            ea.generation()
        ea.p_mutation -= .01
        ea.p_reproduce += .075

        #print(ea.evolved_gene_pool)

        avgFitnessBeginning.append(ea.avgHistory[0])
        bestFitnessBeginning.append(ea.bestHistory[0])
        avgFitnessEnd.append(ea.avgHistory[-1])
        bestFitnessEnd.append(ea.bestHistory[-1])
        ea.showFitness()
        simulations -= 1

        print("Average Fitness at Start:", avgFitnessBeginning)
        print("Best Fitness at Start:", bestFitnessBeginning)
        print("Average Fitness at End:", avgFitnessEnd)
        print("Best Fitness at End:", bestFitnessEnd)

    return step(simulations)

step(5)