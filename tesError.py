from random import randint,random

def sign_func(x):
    if x >= 0:
        return 1
    elif x < 0:
        return -1

class Preceptron:
    def __init__(self, x, learningRate = 0.1, func = sign_func):
        self.input = []
        self.weight = [random() for i in range(x+1)]
        self.learnigRate = learningRate
        self.func = func
	
    def set_input(self, x):
        if len(x) == len(self.weight)-1:
            self.input = x.copy()
            self.input.append(1)

if __name__ == "__main__":
    pc = Preceptron(2, func = sign_func)
    x1 = [randint(1,10), randint(1,10)]
    y1 = 1 if x1[0] <= x1[1] else -1 
    print(x1)
    pc.set_input(x1)
    print(x1)