import numpy as np
global w1
global w2
global bias

def perceptron(x1,x2,y):
    global w1
    global w2
    global bias
    for i in range(1,1000):
        np.random.seed()
        n = np.random.random_integers(0,3)
        # n = i%4
        pred_y = w1*x1[n] + w2*x2[n] + bias
        if pred_y>=0:
            pred_y=1
        else:
            pred_y=0
        error = y[n]-pred_y
        # print y[n]
        # print pred_y
        [w1,w2] = [w1, w2] + np.dot([x1[n], x2[n]],learning_rate*error)
        bias = bias + learning_rate*error
        index =0.0
        for j in range(0,4):
            val_pred_y = w1*x1[j]+w2*x2[j] + bias
            if val_pred_y>=0:
                val_pred_y=1
            else:
                val_pred_y=0
            e = y[j]-val_pred_y
            index = index+e*e
        index = index/4
        print index
        if index < 0.04:
            print('index = 0')
            print(str(i)+' times')
            break
        elif i==999:
            print 'Iteration times: '+str(i)
            print 'Divergent!'
            print ':('

def func(a,b):
    global w1
    global w2
    global bias
    c = a*w1+b*w2+bias
    if c>=0:
        c=1
    else:
        c=0
    print(str(a)+' '+str(b)+' '+str(c))

def NAND_gate():
    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])
    y  = np.array([1, 1, 1, 0])
    return x1,x2,y

def AND_gate():
    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])
    y  = np.array([0, 0, 0, 1])
    return x1,x2,y

def OR_gate():
    x1 = np.array([0, 0, 1, 1])
    x2 = np.array([0, 1, 0, 1])
    y  = np.array([0, 1, 1, 1])
    return x1,x2,y

if __name__ == '__main__':
    np.random.seed()
    [x1,x2,y] = NAND_gate()
    # [x1,x2,y] = AND_gate()
    # [x1,x2,y] = OR_gate()
    global w1
    global w2
    global bias
    w1 = np.random.rand()
    w2 = np.random.rand()
    bias = np.random.rand()
    learning_rate = 0.01
    perceptron(x1,x2,y)
    for i in range(0,4):
        func(x1[i],x2[i])