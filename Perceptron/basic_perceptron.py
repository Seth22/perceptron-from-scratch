# Implementation of basic perceptron that takes two inputs and two weights with a bias term
# I used this to make sure I understood the math and it worked for exclusive OR before generalizing


class perceptron:
    # x1,x2 represent the inputs; w1, w2 are the weights;b is the bias term
    def __init__(self, x1, x2, w1, w2, b):
        self.x1 = x1
        self.x2 = x2
        self.w1 = w1
        self.w2 = w2
        self.b = b

    # Takes the summation of the inputs(x) and weights(w) then adds bias term
    def sum(self):
        return (self.x1 * self.w1 + self.x2 * self.w2) + self.b

    # Decides if perceptron activates using heavystep activation function of sum
    def activation(self):
        if self.sum() > 0:
            return 1
        else:
            return 0


# Implementation of exclusive OR using our perceptron
def XOR_perceptron(x1, x2):
    # Our first two perceptrons are our hidden layer
    p1 = perceptron(x1, x2, 1, 1, -1.5)
    p2 = perceptron(x1, x2, 1, 1, -0.5)

    # Takes perceptron p1 and p2 activation as inputs in the output layer
    p3 = perceptron(p1.activation(), p2.activation(), -1, 1, -0.5)
    return p3.activation()  # returns output(if our output perceptron activates)


