# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:33:06 2018

@author: Brian
"""

import matplotlib.pyplot as plt
import numpy as np
import Card as ea
import Cardmp as ea_mi
import time


#tracking runtime
start_time = time.time()


def single_graph(length, population, pm, pi):
    
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

    #write output
    sim.output()
    return
    
    
  
    
def covary_fixed_population(population, metapopulation, generations):
    
    fitness_array = np.zeros((11,11))
    
    for pi_index in range(11):
        
        for pm_index in range(11):
            
            pm = pm_index / 50
            pi = pi_index / 10
            emilie = []
            fitlist = []
            
            for trial in range(metapopulation):
            
                 emilie.append(ea.Card(population, pm, pi))
                 
                 for step in range(generations*population):
                     emilie[trial].step()
             
                 trial_fitlist = []
                 for individual in range(population):
                     trial_fitlist.append(emilie[trial].fitness(individual))
                 trial_fitlist.sort()
                 
                 median = trial_fitlist[int(population/2)]
                 fitlist.append(median)
         
            fitness_array[pi_index][pm_index] = sum(fitlist)/len(fitlist)


    plt.imshow(fitness_array)
    plt.xlabel('Gene-wise Probability of Mutation')
    plt.ylabel('Gene-wise Probability of Recombination')
    plt.title('Population = %s, Generations = %s, Metapopulation = %s' % (population, generations, metapopulation))
    plt.show()
    



def covary_fixed_pi(pi, metapopulation, generations):
    
    fitness_array = np.zeros((11,11))
    
    for pop_index in range(0,11):
        
        for pm_index in range(0,11):
            
            
            pm = pm_index / 50
            population = (pop_index+1) * 5
            emilie = []
            fitlist = []
            
            for trial in range(metapopulation):
            
                 emilie.append(ea.Card(population, pm, pi))
                 
                 for step in range(generations*population):
                     emilie[trial].step()
             
                 trial_fitlist = []
                 for individual in range(population):
                     trial_fitlist.append(emilie[trial].fitness(individual))
                 trial_fitlist.sort()
                 
                 median = trial_fitlist[int(population/2)]
                 fitlist.append(median)
         
            fitness_array[pop_index][pm_index] = sum(fitlist)/len(fitlist)            

    plt.imshow(fitness_array)
    plt.xlabel('Gene-wise Probability of Mutation')
    plt.ylabel('Population')
    plt.title('Probability of Recombination = %s, Generations = %s, Metapopulation = %s' % (pi, generations, metapopulation))
    plt.show()




def compare_cards(population):
    
    c_mi = []
    c_im = []    
        
    for pm_index in range(0, 101):
        
        pm = pm_index * 0.01
        
        #edit this to ea.Cardmp if you want to switch the order of mutation and recombination
        emilie = ea.Card(population, pm, 0.5)        
        for step in range(0, (population * 5) ):
            
            emilie.step()
        
        fitlist = []
        for individual in range(population):
            fitlist.append(emilie.fitness(individual))
        fitlist.sort()
        
        c_im.append(fitlist[int(population/2)])


        brian = ea_mi.Card(population, pm, 0.5)
        for step in range(0, (population * 5) ):
            
            brian.step()
        
        fitlist = []
        for individual in range(population):
            fitlist.append(emilie.fitness(individual))
        fitlist.sort()
        
        c_mi.append(fitlist[int(population/2)])


    plt.plot(c_mi)
    #plt.plot(c_im)
    plt.xlabel('Probability of Mutation')
    plt.ylabel('Median Fitness')
    plt.title('Population = %s, 5 generations' % population)
    plt.show()


<<<<<<< HEAD
covary_fixed_population(20)

covary_fixed_pi(0.5)

#compare_cards(20)

#single_graph(1000, 100, 0.1, 0.5)
=======
#----------------------- CALLS ------------------------------------------------



start_time = time.time()
#covary_fixed_population(25, 10, 100)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
covary_fixed_pi(0.5, 10, 100)
print("--- %s seconds ---" % (time.time() - start_time))

#compare_cards(20)

single_graph(1000, 100, 0.1, 0.5)
>>>>>>> f06821c42686ba0312182052ec1aac74e464bcdb
