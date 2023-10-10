# Generalized perceptron accepting inputs and weights as a list
class perceptron:
    def __init__(self, x, w, b):
        self.x = x
        self.w = w
        self.b = b

    # Takes sum of weights * inputs for all of the inputs given
    def sum(self):
        sum = 0
        for i in range(len(self.x)):
            sum += ((self.x[i] * self.w[i]))
        sum += self.b
        return sum

    # Our heavyStep activation funciton
    def heavyStep(self):
        if self.sum() > 0:
            return 1
        else:
            return 0

    # A reLu activation function(not sure if implementation is correct)
    def reLu(self):
        if max(0, self.sum()) > 0:
            return 1
        else:
            return 0


# Exclusive OR perceptron accepting inputs and bias as weights
def XOR_perceptron(input):
    # Our first two perceptrons are our hidden layer
    p1 = perceptron(input, [1, 1], -1.5)
    p2 = perceptron(input, [1, 1], -0.5)

    # Takes perceptron p1 and p2 activation as inputs in the output layer
    p3 = perceptron([p1.heavyStep(), p2.heavyStep()], [-1, 1], -0.5)
    return p3.heavyStep()
