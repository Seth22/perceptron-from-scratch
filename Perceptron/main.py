import perceptron


#takes inputs and runs XOR perceptron
def run():
    inputs = getInput()
    print(perceptron.XOR_perceptron(inputs))

#gets inputs x1 and x2 and returns a tuple
def getInput():
    x1 = input("Please enter x1: ")
    x2 = input("Please enter x2: ")

    x1 = int(x1)
    x2 = int(x2)

    return x1,x2

run()