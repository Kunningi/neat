# Q-700 Project 1
#@author: Brian Dahlberg & Justin Slattery
"""
Created on Tuesday Feb 5 8:33 2019

@author: Brian & Justin
"""
from Card_Generational import Card_Generational 
 
    
    

def simulation(generations, i):

    avgFitnessBeginning = []
    bestFitnessBeginning = []
    avgFitnessEnd = []
    bestFitnessEnd = []

    for gen in range(generations):
        ea_list[i].generation()

    avgFitnessBeginning.append(ea_list[i].avgHistory[0])
    bestFitnessBeginning.append(ea_list[i].bestHistory[0])
    avgFitnessEnd.append(ea_list[i].avgHistory[-1])
    bestFitnessEnd.append(ea_list[i].bestHistory[-1])
    
    ea_list[i].showFitness()

    print("Average Fitness at Start:", avgFitnessBeginning)
    print("Best Fitness at Start:", bestFitnessBeginning)
    print("Average Fitness at End:", avgFitnessEnd)
    print("Best Fitness at End:", bestFitnessEnd)

    return 




def fitnessFunction(x, i):
    """Uses fitness function to calculate fitness for a given individual."""
    s = 0
    m = 1
    card = 1

    for gene in ea_list[i].initial_gene_pool[x]:
            if gene == True:
                s += card
            elif gene == False:
                m *= card
            card += 1
    s_error = abs((s - 36) / 36)
    m_error = abs((m - 360) / 360)
    fitness = 1 - (s_error + m_error) / 2

    return fitness




###############################################################################

population_size = 25
pm_list = [0.10, 0.11, 0.12, 0.13, 0.14]
pr_list = [0.500, 0.575, 0.650, 0.725, 0.800]
ea_list = []

for i in range(5):

    ea_list.append(Card_Generational(fitnessFunction, population_size, pm_list[i], pr_list[i]))
    simulation(100, i)

    
