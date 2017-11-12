import numpy as np
import math

weights = None

def perceptron(x1, x2, layer, num):
    global weights
    global biases
    y = weights[(layer-1)*2+num-1][0]*x1 + weights[(layer-1)*2][1]*x2 + biases[layer]
    return y

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Mean Square Error
def loss_func(t,z):
    return (t-z)*(t-z)/2

if __name__ == '__main__':
    # Init all variable
    global weights
    np.random.seed()
    weights = np.random.rand(3,2)
    biases = np.random.rand(3,1)
    learning_rate = 0.01
    # Data of XOR
    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])
    y  = np.array([0, 1, 1, 0])
    for i in range(0,1000):
        n = np.random.random_integers(0,3)
        # Build net
        y1_1 = perceptron(x1[n], x2[n], 1, 1)
        y1_2 = perceptron(x1[n], x2[n], 1, 2)
        y2_1 = perceptron(y1_1, y1_2, 2, 1)
        z = sigmoid(y2_1)
        ms_error = loss_func(y[n],z)
        [weights[2][0], weights[2][1]] = np.array([weights[2][0], weights[2][1]]) + np.dot([y1_1[0], y1_2[0]], learning_rate*ms_error)
        [weights[1][0], weights[1][1]] = np.array([weights[1][0], weights[1][1]]) + np.dot([x1[n], x1[n]], learning_rate*ms_error)
        [weights[0][0], weights[0][1]] = np.array([weights[0][0], weights[0][1]]) + np.dot([x1[n], x1[n]], learning_rate*ms_error)

