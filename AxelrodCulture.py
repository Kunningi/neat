import numpy as np


class Axelrod():
    """Descriptive comment here."""
    
    
    
    
    def __init__(self, size, features, traits):
        
        self.nf = features
        self.nt = traits
        self.sz = size
        self.grid = np.random.randint(traits, size = (self.sz,self.sz,features))
        print(self.grid)
        
for i in range(20):
    print('--------------------------')
    test = Axelrod(5,3,2)