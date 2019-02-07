# -*- coding: utf-8 -*-
#@author: Brian Dahlberg


import numpy as np


class Card():
    """Steady state microbial genetic algorithm without demes. Based on Harvey 
    2009, which suggests that p_inherit = 0.5."""
    
    
    def __init__(self, population, p_mutation, p_inherit):
        
        #number of individuals in population
        self.population = population
        
        #length of genotype - this is hard-coded because it will only need 
        #changing if the fitness function is also changed
        self.genotype_length = 9
        
        #initializes gene pool with booleans for each gene
        self.gene_pool = np.random.choice(a=[False,True], size=(self.population, self.genotype_length))
        #self.gene_pool = np.random.random((self.population, self.genotype_length)) 
        
        #probability of a given gene mutating during mutate()
        self.p_mutation = p_mutation
        
        #probability of a given gene being inherited during inherit()
        self.p_inherit = p_inherit
        
        

        
    def sample(self):
        """Returns tuple with two random, different individuals (indices) from
        the population."""
        
        valid = False
        while valid == False:
            
            s1 = np.random.randint(self.population-1)
            s2 = np.random.randint(self.population-1)
        
            if s1 != s2:
                valid = True
            
        return (s1, s2)
        
    
    
    
    def fitness(self, i):
        """Uses fitness function to calculate fitness for a given individual."""
        
        s = 0
        m = 1
        card = 1
        
        for gene in self.gene_pool[i]:
            
            if gene == True:
                s += card
            elif gene == False:
                m *= card
            card += 1

        s_error = abs((s-36)/36)
        m_error = abs((m-360)/360)
        fitness = 1 - ((s_error + m_error)/2)

        return fitness
        
    
    
    
    def mutate(self, i):
        """Randomly mutates genes in a given individual according to p_mutate."""
        
        for gene in range(self.genotype_length):
            
            if self.p_mutation > np.random.random():
                self.gene_pool[i][gene] = np.random.choice(a=[True,False])
                
        return
    
    
    
    
    def inherit(self, loser, winner):
        """Randomly rewrites genes in a loser/child with the genes of the 
        winner/parent according to p_inherit. Accepts loser/winner index in as
        self.gene_pool as argument."""        
        
        for gene in range(self.genotype_length):
            
            if self.p_inherit > np.random.random():
                self.gene_pool[loser][gene] = self.gene_pool[winner][gene]
        
        return
    
    
    
    
    def step(self):
        """Performs one comparison and then mutates and inherits the loser."""
        
        #sample 
        individuals = self.sample()
        
        #calculate fitness
        fitness_list = []
        for individual in individuals:
            fitness_list.append(self.fitness(individual))
            
        #compare fitness
        if fitness_list[0] > fitness_list[1]:
            loser = individuals[1]
            winner = individuals[0]
            
        else:
            loser = individuals[0]
            winner = individuals[1]
         
        #pass genes from winner to loser according to self.p_inherit
        self.inherit(loser, winner)

        #mutate the loser according to self.p_mutation    
        self.mutate(loser)
        
        return
    
    
    
    
    def output(self): 
        """Writes a file containing the genotypes of the population, sorted by fitness."""
    
        output = open('card_output.txt', 'w')
       
        #create list of fitness values
        fl = []
        for individual in range(self.population):
            fl.append(self.fitness(individual))
        
        #create list of sorted fitness values
        sfl = sorted(fl)
        
        #for value in sfl, find its index in original list (analogous to index 
        #in population)
        sil = []
        for f in sfl:  
            
            i = fl.index(f)
            sil.append(i)
            fl.pop(i)
        
        rank = 1    
        for i in sil:
    
            output.write('Rank:  %s  (f = %s) \n' % (rank, self.fitness(i)))
            output.write('Genotype:  %s \n \n' % (self.gene_pool[i]))
            #output.write(' ')
            rank += 1
            
        output.close()
            
        return
    
        
