import numpy as np

"""
Pythink

Program by Zhenzhu

"""


def sigmoid_func(x):
    return 1/(1+np.power(np.e, -x))

def sign_func(x):
    if x >= 0:
        return 1
    elif x < 0:
        return -1

class Preceptron:
    def __init__(self, x, learningRate = 0.1, func = sigmoid_func):
        """
        Initiate Preceptron by defining how many input (x) and make random weight
        Preceptron(x, learning rate = 1)
        """


        self.input = []
        self.weight = [np.random.random() for i in range(x+1)]
        self.learnigRate = learningRate
        self.func = func
	
    def set_input(self, x):
        if len(x) == len(self.weight)-1:
            self.input = x.copy()
            self.input.append(1)

    def get_output(self):
        # learn NUMPY MATRIX !!!
        self.output = sum(x*self.weight[i] for i,x in enumerate(self.input))
        self.output = self.func(self.output)
        return self.output
            
    def set_learnigRate(self, x):
        self.learnigRate = x

    def guess(self, x):
        self.set_input(x)
        return self.get_output()
        
    def error_calc(self, y, o = None):
        if o == None:
            o = self.output
        self.e = y - o
        return self.e
        
    def learn(self, x, y, t = 0):
        """
        Preceptron.learn(input, output, toleransi)
        """
        self.guess(x)
        self.error_calc(y)
        if abs(self.e) > t:
            dW = []
            for i in self.input:
                dW.append(self.learnigRate*self.e*i)
            self.weight = [ w + dW[i] for i,w in enumerate(self.weight)]
            return 1
        else:
            return 0

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
        



#end

#test part
if __name__ == "__main__":
    print('================= start =================')
    pc = Preceptron(2, func = sign_func)
    from random import randint
    for i in range(5):
        jum = 0
        for i in range(100):
            x1 = [randint(1,10), randint(1,10)]
            y1 = 1 if x1[0] <= x1[1] else -1 
            jum += pc.learn(x1, y1)
        avg = jum/100
        print(jum, avg)
    print(pc.weight)