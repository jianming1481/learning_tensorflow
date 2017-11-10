import numpy as np

weights = None

def perceptron(x1, x2, y, layer, num):
    global weights
    global biases
    y = weights[(layer-1)*2+num-1][0]*x1 + weights[(layer-1)*2][1]*x2 + biases[layer]

if __name__ == '__main__':
    # Init all variable
    global weights
    np.random.seed()
    weights = np.random.rand(3,2)
    biases = np.random.rand(3,1)

    # Data of XOR
    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])
    y  = np.array([0, 1, 1, 0])

    # Build net
    perceptron(x1, x2, y, 1, 1)
    perceptron(x1, x2, y, 1, 2)
    perceptron(x1, x2, y, 2, 1)