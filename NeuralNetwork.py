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

class MultiPreceptron:
    def __init__(self,i, o):
        
        self.input = []
        self.learnigRate = 0.1
        self.weight = [[np.random.random() for i in range(i+1)] for j in range(o)]
        # self.weight= [
                      # [3,3,3,1],
                      # [4,4,4,1],
                      # [5,5,5,1],
                      # [6,6,6,1]
                      # ]
        self.weightT = np.transpose(self.weight)
        
    def set_learnigRate(self, x):
        self.learnigRate = x
        
    def set_input(self, i = []):
        '''
         format input in this module is following format on sentdex youtube tutorial
            checkout https://youtube.com/sentdex
            
            if just one input so
                
                MP = MultiPreceptron(4, 3)
                
                x =[x1, x2, x3, x4]
                MP.set_input(x)
                
            if you sending bacth of input so
                exmaple with 3 batch
                
                MP = MultiPreceptron(4, 3)
                
                x1 = [x11, x12, x13, x14] 
                x2 = [x21, x22, x23, x24] 
                x3 = [x31, x32, x33, x34] 
                x = [xx1, x2, x3]
                MP.set_input(x)
        '''
        
        if len(np.shape(i)) == 2:
            if len(i[0]) == len(self.weight[0])-1:
                self.input = i
                for i, _ in enumerate(self.input):
                    self.input[i].append(1)
            else:
                print('Jumlah input tidak cocok !')
        if np.shape(i) == 1:
            if len(i) == len(self.weight[0])-1:
                self.input = i
                self.input.append(1)
            else:
                print('Jumlah input tidak cocok !')
    def get_output(self):
        self.output = np.dot(self.input, self.weightT)
        self.output = sigmoid_func(self.output)
        return self.output
        
    def learn(self, y, t): #y gonna be the true answer and tis minimun tolerance 
        self.error = np.min(self.output,y)
        
def sigmoid_func(x):
    return 1/(1+np.power(np.e, -x))


#end