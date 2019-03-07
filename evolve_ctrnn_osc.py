import mga
import ctrnn
import numpy as np
import matplotlib.pyplot as plt

# NN Params
nnsize = 3
duration = 20
stepsize = 0.1
WeightRange = 15
BiasRange = 15
TimeConstMin = stepsize*10
TimeConstMax = 5.0

# Fitness function
def fitnessFunction(genotype):
    time = np.arange(0.0,duration,stepsize)
    nn = ctrnn.CTRNN(nnsize)
    nn.setParameters(genotype,WeightRange,BiasRange,TimeConstMin,TimeConstMax)
    nn.initializeState(np.zeros(nnsize))

    
    ip_count = 0    #count of (i)nflection (p)oints
    slope_list = []
    
    for t in time:    #simulate network
        pastOutput = nn.Output[0]    #get output at current step (soon to be past)
        nn.step(stepsize)    #run one step
        currentOutput = nn.Output[0]    #get output at current step
        if (currentOutput - pastOutput) > 1:    #this will populate slope list
            
            slope = True    #positive slope
        else: 
            
            slope = False    #negative slope
            
        slope_list.append(slope)
        
    for s in range((len(slope_list)-1)):    #this loop will count the number of inflection points
       
        if slope_list[s] != slope_list[s+1]:
        
            ip_count += 1
        
    return ip_count



# EA Params
popsize = 10
genesize = nnsize*nnsize + 2*nnsize
recombProb = 0.5
mutatProb = 0.1
generations = 50
tournaments = generations * popsize

# Evolve and visualize fitness over generations
ga = mga.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb)
ga.run(tournaments)
ga.showFitness()

# Get best evolved network and show its activity 
af,bf,bi = ga.fitStats()
time = np.arange(0.0,duration,stepsize)
nn = ctrnn.CTRNN(nnsize)
nn.setParameters(ga.pop[bi],WeightRange,BiasRange,TimeConstMin,TimeConstMax)    #edited to give genotype of bi rather than just bi, which is an address in ga.pop
nn.initializeState(np.zeros(nnsize))
outputs = np.zeros((len(time),nnsize))
step = 0
for t in time:
    nn.step(stepsize)
    outputs[step] = nn.Output
    step += 1
#for i in range(nnsize):
plt.plot(time, outputs.T[0])    #changed this
plt.xlabel("Time")
plt.ylabel("Output")
plt.title("Neural activity")
plt.show()

