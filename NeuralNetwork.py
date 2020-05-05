import numpy as np

class Preceptron:
    def __init__(self, x):
        self.input = []
        self.weight = [np.random.random() for i in range(x+1)]
        self.learnigRate = 1
	
    def set_input(self, x):
        if len(x) == len(self.weight)-1:
            self.input = x
            self.input.append(1)
            
    def set_learnigRate(self, x):
        self.learnigRate = x
        
    def get_output(self):
        # learn NUMPY MATRIX BITCH !!!
        self.output = sum(self.input[i]*self.weight[i] for i in range(len(self.input)))
        self.output = sigmoid_func(self.output)
        return self.output
        
    def learn(self, y, t):
        self.e = (y-self.output)
        if abs(self.e) > t:
            dW = []
            for i in range(len(self.input)):
                dW.append(self.learnigRate*self.e*self.input[i])
            self.weight = [self.weight[i]+dW[i] for i in range(len(self.weight))]
        elif self.e < t:
            pass
        
            
def sigmoid_func(x):
    return 1/(1+np.power(np.e, -x))
    
    
def run():
    p = Preceptron(2)
    width = 600
    height = 400
    x1 = [[np.random.randint(0,width),np.random.randint(0,height)] for i in range(100)]
    for i in range(len(x1)):
        p.set_input(x1[i])
        y = p.get_output()
        if x1[i][0]<x1[i][1]:
            a = 1
        elif x1[i][0]>x1[i][1]:
            a = 0
        p.learn(a,0.01)
    print('Final Training')
    e = 0
    test = 100
    x1 = [[np.random.randint(0,width),np.random.randint(0,height)] for i in range(test)]
    for i in range(test):
        p.set_input(x1[i])
        y = p.get_output()
        if x1[i][0]<x1[i][1]:
            a = 1
        elif x1[i][0]>x1[i][1]:
            a = 0
        if y != a:
            e +=1 
    print('final error : ',e/test)
    
    
    
if __name__ == '__main__':
    run()
            
    
#end