from perceptron import XOR_perceptron

#Tests exclusive OR values
def test_XOR():
    assert XOR_perceptron([0,0]) == 0, "Input 0,0 should equal 0"
    assert XOR_perceptron([1,1]) == 0, "Input 1,1 should equal 0"
    assert XOR_perceptron([0,1]) == 1, "Input 0,1 should equal 1"
    assert XOR_perceptron([1,0]) == 1, "Input 1,0 should equal 1"

