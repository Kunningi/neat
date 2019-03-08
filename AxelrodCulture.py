import numpy as np
import matplotlib.pyplot as plt


class Axelrod():
    """Based on Axelrod 1997, with a counterculture mechanic added (optional).
    
    This mechanic, after each event, takes the active cell, picks a random feature, 
    and calculate the global proportion of cells with the same trait within that feature. 
    This proportion is then used as the probability that that feature will be changed, 
    with a greater abundance corresponding to a greater probability of being changed. 
    The trait value is then changed to the least abundant trait value in the global
    population. """
    
    
    
    #tested, working as expected
    def __init__(self, enable_cc, size, n_features, n_traits):
        
        self.cc = enable_cc    #enable counterculture method? (boolean)
        self.nf = n_features    #number of features, or types of traits (int)
        self.nt = n_traits    #number of possible traits within each feature (int)
        self.sz = size    #spatial size of grid (int)
        self.age = 0    #counter for number of steps
        
        self.grid = np.random.randint(self.nt, size = (self.sz, self.sz, self.nf))    #create 3D array of random traits 

        
        return
    
        
        
    #something is wrong with age though...
    def steps(self, n):
       
       for step in range(n):
           
           ai, aj = np.random.randint(self.sz, size=2)    #randomly select active cell
           ni, nj = self.select_neighbor(ai,aj)    #randomly select neighbor, wrapping around edges
           if np.random.random() < self.interact_prob(ai, aj, ni, nj):    #determine if a feature will change based on interaction probability/similarity
              
               self.adopt_feature(ai, aj, ni, nj)    #modify feature in self.grid
           
           if self.cc == True:    #if counterculture enabled, do that too
               
               self.counterculture()
               
           self.age += 1    #keep track of how many steps have been run
                       
       
        
    #not testing for now
    def counterculture(self):
       
        ai, aj = np.random.randint(self.sz, size=2)    #randomly select active cell
        f = np.random.randint(self.nf)    #pick a feature
        tc = np.zeros(self.nt)    #count variable for traits within feature
        
        for i in range(self.sz):    #traverse grid 
            for j in range(self.sz):
                
                t = self.grid[i][j][f]    #extract trait for given feature f
                tc[t] += 1    #count trait in tc
            
        at = self.grid[ai][aj][f]    #extract trait of active cell        
        pat = (tc[at] / sum(tc) )    #calculate proportion of cells that match active cell trait
        
        if np.random.random() < pat:    #likelihood of trait change based on abundance of trait, the more abundant the trait the more likely the change
            tc = list(tc)    #convert to list for indexing
            mt = tc.index(min(tc))    #find least common trait in trait count list (first available if ties)
            self.grid[ai][aj][f] = mt    #change active cell trait to the least common trait
    
        
        
    #tested, working as expected
    def adopt_feature(self, ai, aj, ni, nj):
        
        f = np.random.randint(self.nf)    #randomly determine feature to be modified
        self.grid[ai][aj][f] = self.grid[ni][nj][f]    #modify feature of active cell to match that of neighbor cell
            
        
        
    #tested, working as expected
    def select_neighbor(self, ai, aj):
           
       valid = False    
       while valid == False:    #this loops will break when a valid neighbor is found
           
           ri = np.random.randint(-1,2)   #will return relative coordinate: -1, 0, 1
           rj = np.random.randint(-1,2)
           if (ri != 0) or (rj != 0):    #if the selected neighbor isn't the active cell...
               
               valid = True    #...then break loop
                
       ni = (ai+ri) % self.sz    #convert to neighbor coordinate, then give valid coordinate using modulus (wraparound edge)
       nj = (aj+rj) % self.sz
       
       return ni, nj
       
           
           
    #tested, working as expected
    def interact_prob(self, ai, aj, ni, nj):
        
        at = self.grid[ai][aj]    #get trait vector for active cell
        nt = self.grid[ni][nj]    #get trait vector for neighbor cell
        cfc = 0    #for counting features with common trait
        for f in range(self.nf):   #iterate through the features in trait vectors
            
            if at[f] == nt[f]:    #if the traits for the given feature are the same...
                
                cfc += 1    #then add feature to count
                
        return (cfc / self.nf)    #return proportion of common features to total features
        
    
    
    
    def similarity_index(self, i, j):
        
        ss = 0    #similarity sum, sums up similarity with all neighbors (including self) for averaging later
        for ri in range(-1, 2):    #traverse through relative neighbor coordinates
            for rj in range(-1, 2):
                
                ni = (i+ri) % self.sz    #convert to neighbor coordinate, then give valid coordinate using modulus (wraparound edge)
                nj = (j+rj) % self.sz   
                ss += self.interact_prob(i, j, ni, nj)    #interaction probability can also be thought of as the proportion of similar traits to a given neighbor
        
        return ss/9    #return average similarity (9 being number of neighbors (including self))
        
    
    
    
    def show_similarity(self):
        
        data = np.zeros((self.sz, self.sz))    #initialize grid for graphing
        for i in range(self.sz):    #traverse through grid for populating
            for j in range(self.sz):
                
                data[i][j] = self.similarity_index(i,j)    #populate cell with similarity_index
                
        plt.imshow(data, cmap='binary')
        plt.title('Similarity After %s Events (CC = %s)' % (self.age, self.cc))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        
    
    
    
    def show_feature(self, f):
        data = np.zeros((self.sz, self.sz))    #initialize grid for graphing
        for i in range(self.sz):    #traverse through grid for populating
            for j in range(self.sz):
                
                data[i][j] = self.grid[i][j][f]  #populate cell with trait of feature 0
                
        plt.imshow(data, cmap='Set1')
        plt.title('Feature %s After %s Events (CC = %s)' % (f, self.age, self.cc))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()