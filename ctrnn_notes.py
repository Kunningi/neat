import numpy as np
import math

def sigmoid(x):
    return 1/(1+np.exp(-x))

mu = 0.0
sig = 1.0
def sigmoid2(x):
    return 1./(math.sqrt(2.*math.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)

class CTRNN():

    def __init__(self, size):
        self.Size = size                        # number of neurons in the network
        self.Voltage = np.zeros(size)           # neuron activation vector
        self.TimeConstant = np.ones(size)       # time-constant vector
        self.Bias = np.zeros(size)              # bias vector
        self.Weight = np.zeros((size,size))     # weight matrix
        self.Output = np.zeros(size)            # neuron output vector
        self.Input = np.zeros(size)             # neuron output vector
        
    def randomizeParameters(self):
        self.Weight = np.random.uniform(-10,10,size=(self.Size,self.Size))
        self.Bias = np.random.uniform(-10,10,size=(self.Size))
        self.TimeConstant = np.random.uniform(0.1,5.0,size=(self.Size))
        self.invTimeConstant = 1.0/self.TimeConstant

    def step(self,dt):
        self.Output = sigmoid(self.Voltage+self.Bias)    #analogous to the first loop (36)
        netinput = self.Input + np.dot(self.Weight.T, self.Output)    #analogous to second and third loop
        self.Voltage += dt * (self.invTimeConstant*(-self.Voltage+netinput))

    def stepForLoops(self,dt):
        
        for i in range(self.Size):
            self.Output[i] = sigmoid(self.Voltage[i] + self.Bias[i])    #calculate output for each neuron based on voltage and bias
            
        for i in range(self.Size):
            netinput = self.Input[i]
            for j in range(self.Size):    
                netinput += self.Weight[j][i]*self.Output[j]
                
            dydt = (1/self.TimeConstant[i])*(-self.Voltage[i]+netinput)
            
            self.Voltage[i] += dt * dydt          
            
        self.Output = sigmoid(self.Voltage+self.Bias)
