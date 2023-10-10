class perceptron:
    def __init__(self,x,w,b):
        self.x = x
        self.w = w
        self.b = b

    def sum(self):
        sum = 0
        for i in range(len(self.x)):
            sum += ((self.x[i] * self.w[i]))
        sum += self.b
        return sum

    def heavyStep(self):
        if self.sum() > 0:
            return 1
        else:
            return 0

    def reLu(self):
        if max(0,self.sum()) > 0:
            return 1
        else:
            return 0

def XOR_perceptron(input):
    p1 = perceptron(input,[1,1],-1.5)
    p2 = perceptron(input,[1,1],-0.5)

    p3 = perceptron([p1.heavyStep(),p2.heavyStep()],[-1,1],-0.5)
    return p3.heavyStep()


