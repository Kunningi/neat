# Q-700 Project 1
#@author: Brian Dahlberg & Justin Slattery

import numpy as np
import random
import matplotlib.pyplot as plt

class Card_Generational():
    """Generational microbial genetic algorithm without demes. Based on Harvey
    2009, which suggests that p_inherit = 0.5."""
    def __init__(self, fitnessFunction, population_size, p_mutation, p_reproduce):
        self.fitnessFunction = fitnessFunction
        self.population_size = population_size                                                                              #number of individuals in population
        self.genotype_length = 9                                                                                            #length of genotype - this is hard-coded because it will only need
                                                                                                                            #changing if the fitness function is also changed
        self.initial_gene_pool = np.random.choice(a=[False,True], size=(population_size, self.genotype_length))        #initializes gene pool with booleans for each gene

        self.evolved_gene_pool = np.zeros((population_size, self.genotype_length))                                     #updates the gene pool after selection/reproduction
        self.avgHistory = []
        self.bestHistory = []
        self.p_mutation = p_mutation                                                                                        #probability of a given gene mutating during mutate()
        #self.p_inherit = p_inherit                                                                                          #probability of a given gene being inherited during inherit()
        self.p_reproduce = p_reproduce                                                                                      #probability of reproduction based on p_reproduce
        self.rsize = sum(range(population_size))
        self.roulette = np.zeros(self.rsize, dtype=int)                                                                     #roulette array for selection
        self.fit = np.zeros(population_size)                                                                                #fitness value

    def showFitness(self):
        plt.plot(self.bestHistory)
        plt.plot(self.avgHistory)
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.title("Best and Average Fitness")
        plt.show()

    def fitStats(self):
        bestfit = 0
        avgfit = 0
        for fit in self.fit:
            avgfit += fit
            if (fit > bestfit):
                bestfit = fit
        return avgfit/self.population_size, bestfit

    def reportStats(self):
        af, bf = self.fitStats()
        self.avgHistory.append(af)
        self.bestHistory.append(bf)

    def evaluateFitness(self):  ##
        for i in range(self.population_size):
            self.fit[i] = self.fitnessFunction(self.initial_gene_pool[i])

    def rank(self):
        """Ranks the agent after assessing fitness"""
        currentRank = self.population_size - 1
        rouletteIndex = 0
        for x in range(self.population_size):
            highest_fitness = 0
            bestind = -1
            for i in range(self.population_size):
                if (self.fit[i] > highest_fitness):
                    highest_fitness = self.fit[i]
                    bestind = i
            self.fit[bestind] = 0
            for r in range(currentRank):
                self.roulette[rouletteIndex] = bestind
                rouletteIndex += 1
            currentRank -= 1


    def sample(self):
        """Takes a sample of two random individuals from the population"""
        a = random.randint(0,self.rsize-1)
        b = random.randint(0,self.rsize-1)
        while (self.roulette[a]==self.roulette[b]):
            b = random.randint(0,self.rsize-1)
        return self.roulette[a],self.roulette[b]


    def reproduce(self,a,b,i):
        """Selects two individuals for reproduction/recombination"""
        for l in range(self.genotype_length):
            if (random.random() < self.p_reproduce):
                self.evolved_gene_pool[i][l] = self.initial_gene_pool[a][l]
            else:
                self.evolved_gene_pool[i][l] = self.initial_gene_pool[b][l]


    def mutate(self,i):
        """Mutates an individual based on p_mutation"""
        for l in range(self.genotype_length):
            if (random.random() < self.p_mutation):
                if self.evolved_gene_pool[i][l] == 1:
                    self.initial_gene_pool[i][l] = 0
                else:
                    self.initial_gene_pool[i][l] = 1


    def repopulate(self):
        for i in range(self.population_size):
            a,b = self.sample()                                     #Step 1: Select 2 individuals based on their rank
            self.reproduce(a,b,i)                                   #Step 2: Recombine
            self.mutate(i)                                          #Step 3: Mutate
        self.initial_gene_pool = np.copy(self.evolved_gene_pool)    #Step 4: Replace new population


    def generation(self):
        self.evaluateFitness()
        self.reportStats()
        self.rank()
        self.repopulate()