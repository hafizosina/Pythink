import numpy as np

class Preceptron:
    def __init__(self, x):
        self.input = []
        self.weight = [np.random.random() for i in range(x+1)]
        self.learnigRate = 1
	
    def set_input(self, x):
        print(x,"\t")
        if len(x) == len(self.weight)-1:
            self.input = x
            self.input.append(1)
            
    def set_learnigRate(self, x):
        self.learnigRate = x
        
    def get_output(self):
        # learn NUMPY MATRIX BITCH !!!
        self.output = sum(self.input[i]*self.weight[i] for i in range(len(self.input)))
        self.output = sigmoid_func(self.output)
        print(self.input,' guest ',self.output)
        return self.output
        
    def learn(self, y, t):
        self.e = -(self.output-y)
        if self.e > t:
            dW = []
            for i in range(len(self.input)):
                dW.append(self.learnigRate*self.e*self.input[i])
            print('-----------')    
            print(dW)
            print('-----------')     
            self.weight = [self.weight[i]+dW[i] for i in range(len(self.weight))]
            print(self.weight)
            print('-----------') 
        elif self.e < t:
            pass
        print('error : ',self.e)
        print('============================ ')    
        print(' ')    
            
def sigmoid_func(x):
    return 1/(1+np.power(np.e, -x))
    
    
    
    
    
    
if __name__ == '__main__':
    p = Preceptron(2)
    width = 600
    height = 400
    x1 = [[np.random.randint(0,width),np.random.randint(0,height)] for i in range(100)]
    for i in range(len(x1)):
        p.set_input(x1[i])
        y = p.get_output()
        if x1[i][0]<x1[i][1]:
            y = 1
        if x1[i][0]>x1[i][1]:
            y = 0
        print(x1[i],' >>>>>> ', y)
        print(' ')
        p.learn(y,0.01)
#end