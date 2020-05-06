import numpy as np
from NeuralNetwork import *
    
def runPreceptron():
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
    
 
def runMultiPreceptron():
    MP = MultiPreceptron(3,4)
    MP.set_input([[2,2,2],[3,3,3],[4,4,4]])
    o = MP.get_output()
    print(o)
            
            
if __name__ == '__main__':
    runMultiPreceptron()
    
            
    
#end