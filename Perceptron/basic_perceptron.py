
#takes 2 inputs 2 weights and sums them together
#
class perceptron:
    def __init__(self,x1,x2,w1,w2,b):
        self.x1 = x1
        self.x2 = x2
        self.w1 = w1
        self.w2 = w2
        self.b = b

    def sum(self):
        return ((((self.x1*self.w1) + (self.x2*self.w2))) + self.b)

    def activation(self):
        if self.sum() > 0:
            return 1
        else:
            return 0

def XOR_perceptron(x1,x2):
    p1 = perceptron(x1,x2,1,1,-1.5)
    p2 = perceptron(x1,x2,1,1,-0.5)

    p3 = perceptron(p1.activation(),p2.activation(),-1,1,-0.5)
    return p3.activation()


#takes inputs and runs XOR perceptron
def run():
    inputs = getInput()
    print(XOR_perceptron(inputs[0],inputs[1]))

#gets inputs x1 and x2 and returns a tuple
def getInput():
    x1 = input("Please enter x1: ")
    x2 = input("Please enter x2: ")

    x1 = int(x1)
    x2 = int(x2)

    return x1,x2

run()